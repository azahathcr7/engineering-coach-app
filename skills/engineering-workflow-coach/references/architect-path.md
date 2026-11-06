# The Path to Architect

An architect is not someone who writes the fanciest code. They are the person who makes good decisions about how a system is shaped, can explain them clearly, and who prevents expensive mistakes before they're built. Use this file to write the "level-up note" at the end of a coaching reply and to plan growth.

## Contents
- The ladder
- Architect mindset
- Skills to build, with practice exercises
- Level-up note prompts
- Reading a system like an architect

## The ladder

| Level | Focus | You're ready to move up when... |
|---|---|---|
| Learner | Following the lifecycle correctly with guidance | You can run the loop on a small task without being reminded of steps |
| Practitioner | Delivering reliable changes independently | Your PRs are small, tested, and rarely come back with surprises |
| Senior | Owning a whole feature or pipeline end to end; mentoring | You anticipate failure modes before review and others ask your opinion |
| Staff / lead | Solving problems across teams; setting standards | You change how the team works, not just what it ships |
| Architect | Shaping systems and decisions that last years | You make trade-offs explicit and documented, and systems you designed age well |

The user directs AI to write code; the ladder is the same. What rises with level is judgment: knowing what to ask for, what to distrust and what to decide.

## Architect mindset

1. **Everything is a trade-off.** Speed vs safety, simple vs flexible, build vs buy. Name both sides of every choice.
2. **Think in failure.** Ask "how does this break?" before "how does this work?"
3. **Optimize for change.** Requirements will change. Prefer designs that are easy to modify and easy to delete.
4. **Make decisions visible.** Write short decision records (what we chose, what we rejected, why) so future people understand.
5. **Start from the problem and constraints**, not the technology. Tools are the last decision, not the first.
6. **Know the data.** Systems are mostly about how data is created, moved, stored and trusted.
7. **Keep it as simple as the problem allows.** Remove, don't add, when in doubt.

## Skills to build, with practice exercises

**1. Reading code and systems**
Exercise: pick any repo or system you use; draw a one-page map: components, data flows, who owns what. Ask the AI to check your map.

**2. Debugging method**
Exercise: next bug, write down reproduce, hypothesis, test, result, before asking the AI to fix it. Compare your reasoning to the AI's.

**3. Testing and verification**
Exercise: before approving AI code, write five test cases yourself, including two nasty ones (empty, duplicate, huge, weird characters).

**4. Data modeling**
Exercise: sketch the tables or objects for a small business (orders, customers, products). Then add one change (e.g., bundles) and see what breaks. Learn why keys, relationships and constraints matter.

**5. System design**
Exercise: "Design a nightly product sync between System A and B." Cover scale, failures, retries, monitoring, rollback. Have the AI critique it as a skeptical staff engineer.

**6. Writing design docs and decision records**
Exercise: write a one-page doc for your next change: context, options, decision, risks. Keep a decisions log.

**7. Operations and reliability**
Exercise: for one thing you ship, define "healthy" (3 metrics), the alert, and the first three steps when it breaks.

**8. Security and privacy basics**
Exercise: list every secret and every piece of personal data your task touches; where is each stored, who can see it, how is it rotated or deleted?

**9. Cost and scale thinking**
Exercise: estimate what happens at 10x the data or traffic. What breaks first? What costs more?

**10. Communication and influence**
Exercise: explain your last change in three sentences to a non-technical person and in ten to an engineer. Both should be accurate.

## Level-up note prompts

Pick one that fits the task and write it in 2 to 4 sentences:
- "A senior engineer would also ask: ..." (the question not yet asked)
- "The failure mode to watch: ..."
- "An architect would zoom out and notice: ..." (pattern, dependency, or repeated task that suggests a bigger design)
- "The thing to document so future-you or a teammate doesn't repeat this: ..."
- "Next skill to practice from this task: ..." (link to an exercise above)

## Reading a system like an architect

Ask these five questions of any system:
1. What are the main components and what does each own?
2. Where does data enter, change, and leave?
3. What happens when each part fails or is slow?
4. Who can change what, and how is change controlled?
5. How would we know, quickly, that something is wrong?

If the user can answer these for their live store setup, they are already thinking at design level.
