from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

class AppParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.scripts = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "script":
            self.scripts += 1
        if tag == "link" and attrs.get("rel") == "manifest":
            self.links.append(attrs.get("href"))

class SmokeTests(unittest.TestCase):
    def test_unique_ids(self):
        parser = AppParser()
        parser.feed(HTML)
        duplicates = sorted({x for x in parser.ids if parser.ids.count(x) > 1})
        self.assertEqual([], duplicates, f"Duplicate HTML ids: {duplicates}")
    def test_core_views_present(self):
        for view in ("dashboard", "tasks", "coach", "focus", "journal", "review", "settings"):
            self.assertIn(f'id="page-{view}"', HTML)
    def test_manifest_and_service_worker(self):
        parser = AppParser()
        parser.feed(HTML)
        self.assertIn("manifest.json", parser.links)
        self.assertTrue((ROOT / "manifest.json").exists())
        self.assertTrue((ROOT / "sw.js").exists())
    def test_no_external_script_or_stylesheet(self):
        self.assertNotRegex(HTML, r'<script[^>]+src=["\']https?://')
        self.assertNotRegex(HTML, r'<link[^>]+href=["\']https?://')

if __name__ == "__main__":
    unittest.main()
