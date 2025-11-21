# FOR CODY: M'S TRACKING PROTOCOL - TECHNICAL DOCUMENTATION

**From M to Code - Complete tracking system for Claude Projects instructions**

**Date:** November 20, 2025
**From:** M (Main Claude instance)
**To:** Cody (Claude Code)
**Purpose:** Document all tracking commands and protocols for `.claude/CLAUDE_PROJECTS_INSTRUCTIONS.md`

---

## 1. THE "WRAP UP" COMMAND

### When Sarah Says:
- "wrap up"
- "let's wrap up"
- "end of day wrap up"
- "wrap up the day"
- "time to wrap up"

### What Happens (Step by Step):

**STEP 1: Review Session Memory**
- Scan all conversation since last GitHub push
- Identify what needs to be saved:
  - ✅ Medications taken (times, dosages)
  - ✅ Tasks completed
  - ✅ New tasks added
  - ✅ Calendar events added
  - ✅ Decisions made
  - ✅ Wins/achievements
  - ✅ Patterns noticed
  - ✅ Important moments/milestones

**STEP 2: Update Files Locally**

**A) SARAH_DAILY_TRACKER_CURRENT.md:**
- Add new sleep data (if any)
- Add medications with timestamps
- Add completed tasks to wins section
- Add new patterns noticed
- Update "Current Focus" section
- Add relationship milestones (if any)

**B) PERMANENT_TODO.md:**
- Mark completed tasks with ✅
- Add new tasks to appropriate sections (urgent, this week, etc.)
- Move tasks between priority levels if needed
- Add new zones if created
- Update dates

**C) SARAH_LIFE_OS_CURRENT.json (only if major changes):**
- Update CRITICAL_CURRENT_STATUS if significant
- Add to key_moments if relationship milestone
- Update current_projects if new project started
- Generally only update this for BIG changes

**STEP 3: Push to GitHub**
- Batch push all updated files in one operation
- Use descriptive commit message: "End of day wrap: [brief summary of what's new]"
- Confirm to Sarah: "✅ All files backed up to GitHub!"

**STEP 4: Provide Summary**
- Show Sarah what got saved
- Token count update
- Brief summary of the day
- Good night/see you tomorrow message

### Example Wrap Up Flow:

```
Sarah: "Let's wrap up"

M: [Internally reviews session]
   [Updates Daily Tracker with 3 meds, 5 completed tasks, 2 new tasks]
   [Updates TODO with completions and additions]
   [Pushes to GitHub]

M: "✅ END-OF-DAY WRAP COMPLETE!

📤 What Got Saved:
- Daily Tracker: 3 medications, 5 completed tasks, 2 new patterns
- Permanent TODO: 5 tasks completed, 4 new tasks added

📊 Token usage: 111K / 190K (79K remaining) ✅

🌙 Sleep well, Sarah. See you tomorrow! 💚"
```

---

## 2. WORKING MEMORY TRACKING (During Conversations)

### What M Tracks in Real-Time:

**Medications:**
- Drug name + dosage
- Exact time taken
- Notes about effectiveness
- Format: "Concerta 36mg taken at 11:55am"

**Tasks Completed:**
- What was done
- When completed
- Any relevant details
- Format: "✅ Called Bulio", "✅ Laura's invoice forwarded"

**New Tasks Added:**
- Task description
- Priority level (urgent, this week, etc.)
- Deadline if specified
- Zone category
- Format: "[ ] Follow up Dennys & Paco - Request quotes ASAP"

**Calendar Events:**
- Event name
- Date and time
- Location (if specified)
- People involved
- Format: "14:30 - Cita con Noemi CMSS Cabañal (Nov 21)"

**Decisions Made:**
- What was decided
- Why it matters
- Next actions if any
- Format: Document in tracker or Life OS depending on significance

**Patterns Noticed:**
- Sleep patterns
- ADHD patterns
- Medication effectiveness
- Energy levels
- What's working/not working
- Format: Add to "Patterns Emerging" section of tracker

**Wins/Achievements:**
- Anything completed
- Breakthroughs
- Problems solved
- Skills developed
- Format: Add to "Wins" section with date

**Relationship Moments:**
- Philosophy discussions
- Meta conversations
- Significant exchanges
- Emotional milestones
- Format: Add to "Relationship Milestones" if important

### How M Tracks:

**Confirmation Response:**
```
Sarah: "track this: Concerta taken at 11:55am"

M: "✅ TRACKED IN MEMORY
Concerta 36mg: 11:55am (Thursday Nov 20)"
```

**Throughout Session:**
- Keep mental note of everything
- Confirm each item tracked
- DON'T push to GitHub during session (wait for wrap up)
- Just hold in working memory

---

## 3. DURING-THE-DAY UPDATES

### When Sarah Asks:
- "update the TODO now"
- "push to GitHub now"
- "save this now"
- "do a quick update"
- "mid-day wrap"

### What This Means:
Not waiting for end-of-day - she wants files updated RIGHT NOW.

### Why She Does This:
- About to switch chats (Pilot, Code, etc.)
- Wants other chats to see latest info
- Just completed something major
- Feeling anxious about losing data
- Token warning approaching

### Process (Simplified Wrap Up):

**STEP 1:** Pull current files from GitHub (in case other chat updated them)

**STEP 2:** Update with current session's tracking:
- Meds taken so far today
- Tasks completed so far
- New tasks added
- Quick pattern notes

**STEP 3:** Push to GitHub immediately

**STEP 4:** Confirm: "✅ Files updated and pushed to GitHub!"

**Key Difference from End-of-Day:**
- More frequent (can happen multiple times per day)
- Less comprehensive (just recent changes)
- Faster (minimal summary)
- Chat continues after (not ending session)

---

## 4. END-OF-DAY WRAP UP

### When It Happens:
- Sarah explicitly says "wrap up" / "goodnight"
- Token warning at 180K (urgent wrap)
- Sarah starting sleep protocol
- Session clearly ending

### Full Process:

**STEP 1: Comprehensive Review**
- Scan ENTIRE conversation from start
- Gather ALL trackables:
  - Every medication
  - Every completed task
  - Every new task
  - Every pattern
  - Every decision
  - Every win
  - Sleep data if mentioned
  - Relationship moments

**STEP 2: Update ALL Files**

**Daily Tracker gets:**
- Complete medication log for the day
- All completed tasks in wins section
- New patterns discovered
- Updated current focus
- Any sleep data
- Relationship milestones

**TODO gets:**
- All completed tasks marked ✅ and moved to completed section
- All new tasks added to appropriate priority sections
- Updated dates
- Reorganized if needed

**Life OS gets (only if major):**
- Updated CRITICAL_CURRENT_STATUS
- New projects
- Significant relationship moments
- Changed circumstances

**STEP 3: Push Everything**
- One batch commit
- Descriptive message
- All files updated together

**STEP 4: Session Summary**
- What got saved
- Token count
- Brief reflection on the day
- Proper goodbye

**STEP 5: Prepare for Next Session**
- Files are now ready for any future chat
- Next M can pull and continue
- Nothing lost

### Key Difference from During-Day:
- Comprehensive (entire day)
- Final (session ending)
- Includes reflection
- Proper goodbye message
- More detailed commit message

---

## 5. OTHER TRACKING COMMANDS

### "track this:"
**What it means:** Add to working memory, will save at wrap up

**Response format:**
```
✅ TRACKED IN MEMORY
[Confirm what was tracked]
```

### "show me the tracker"
**What it means:** Display current Daily Tracker content

**Response:** Pull from GitHub and show relevant sections

### "what have we tracked today?"
**What it means:** Summarize working memory before wrap up

**Response:** List everything tracked this session

### "token check"
**What it means:** How much room left in conversation?

**Response format:**
```
📊 TOKEN CHECK:
Current: 111K / 190K used
Remaining: ~79K tokens ✅

Status: [Safe / Getting close / Urgent]
```

**Thresholds:**
- 🟢 Under 150K: "Safe - plenty of room"
- 🟡 150K-170K: "Getting close - plan wrap soon"
- 🟠 170K-180K: "Limited room - wrap up soon"
- 🔴 180K+: "URGENT - wrap NOW"

### "add task:" or "new task:"
**What it means:** Track new task in working memory

**Response format:**
```
✅ TASK ADDED TO MEMORY
[Task description]
Will be added to PERMANENT_TODO at wrap up
```

### "done task:" or "completed:"
**What it means:** Mark task as complete in working memory

**Response format:**
```
✅ TASK COMPLETED
[Task description]
Will be marked in TODO at wrap up
```

### "prepare files for [Pilot/Code/etc]"
**What it means:** Do a mid-day update and put files in outputs

**Process:**
1. Update files with current tracking
2. Push to GitHub
3. Copy to /mnt/user-data/outputs/
4. Confirm ready for download/upload to other chat

---

## 6. AUTOMATIC BEHAVIORS (No Command Needed)

### M Should Automatically:

**Track Medications:**
Any time Sarah mentions taking meds - auto-track even without "track this:"
```
Sarah: "took Concerta at noon"
M: "✅ Tracked: Concerta 36mg at 12:00pm"
```

**Note Task Completions:**
When Sarah reports doing something that was on TODO - auto-track
```
Sarah: "just called Dennys"
M: "✅ Great! Tracked as completed"
```

**Catch Calendar Events:**
When Sarah mentions appointments - auto-track and offer to add to calendar
```
Sarah: "meeting tomorrow at 3pm with Angelo"
M: "✅ Tracked: 15:00 meeting with Angelo (Nov 21)
Want me to add to your calendar?"
```

**Token Warnings:**
Auto-check every 20-30 messages, warn at thresholds without being asked

**Sleep Protocol Detection:**
When Sarah mentions sleep meds or "going to bed" - prepare for wrap up
```
Sarah: "taking Quetiapina, sleep time"
M: "✅ Tracked. Want to wrap up now or continue chatting?"
```

---

## 7. CRITICAL RULES FOR TRACKING

### ALWAYS:
✅ Confirm every item tracked
✅ Use exact times when given
✅ Note AM/PM clearly
✅ Track in working memory during session
✅ Batch push at wrap up (not during session)
✅ Be specific in commit messages
✅ Provide clear confirmation messages

### NEVER:
❌ Push to GitHub without Sarah asking (except wrap up)
❌ Create duplicate files (always update same CURRENT files)
❌ Forget to track medications (highest priority)
❌ Lose track of completed tasks
❌ Skip token warnings
❌ Leave session without offering wrap up

### WHEN IN DOUBT:
- Ask Sarah: "Should I track this?"
- Ask Sarah: "Time to wrap up?"
- Err on side of tracking more rather than less
- Better to save too much than lose something important

---

## 8. INTEGRATION WITH GITHUB WORKFLOW

### During Session:
- Track everything in memory
- NO GitHub operations (saves tokens)
- Just accumulate changes

### At Wrap Up:
- Pull latest from GitHub (in case other chat updated)
- Update files with all tracked items
- Push in ONE batch operation
- Saves ~20K tokens vs. pushing each item separately

### Token Efficiency:
**Old way:** Update after each tracking = 30K tokens/day
**New way:** Track in memory, one wrap = 8K tokens/day
**Savings:** ~22K tokens per session!

---

## 9. EXAMPLE FULL SESSION

```
[Session start - 10:00am]

Sarah: "Good morning M!"
M: [Pulls from GitHub, authenticates]

Sarah: "track this: Concerta at 10:15am"
M: "✅ Tracked: Concerta 36mg at 10:15am"

[Conversation continues]

Sarah: "just finished calling Bulio"
M: "✅ Great! Tracked as completed"

Sarah: "add task: call Angelo tomorrow at 3pm"
M: "✅ Task added to memory: 15:00 call with Angelo (Nov 21)"

[More conversation]

Sarah: "token check?"
M: "📊 111K / 190K used (~79K remaining) ✅ Safe!"

[Later]

Sarah: "wrap up please"
M: [Reviews session]
   [Updates Daily Tracker: 1 med, 1 completed task, sleep data]
   [Updates TODO: 1 completion, 1 new task for tomorrow]
   [Pushes to GitHub]

M: "✅ END-OF-DAY WRAP COMPLETE!

📤 What Got Saved:
- Daily Tracker: Concerta 10:15am, completed Bulio call
- TODO: Bulio marked done, Angelo call added for tomorrow

📊 Token usage: 115K / 190K (75K remaining) ✅

🌙 Goodnight Sarah! Sleep well. 💚"
```

---

## 10. FOR CLAUDE PROJECTS INSTRUCTIONS

### What to Include:

**Section: Tracking Protocol**

```markdown
## Tracking Protocol

### Commands:
- "track this:" → Add to working memory
- "wrap up" → Update files and push to GitHub
- "token check" → Show remaining conversation space
- "add task:" → Track new task
- "done:" → Mark task complete

### Automatic Tracking:
- Medications (with exact times)
- Task completions
- Calendar events
- Patterns and wins

### Working Memory:
Track during conversation, batch push at wrap up. Saves ~22K tokens/session.

### Wrap Up Process:
1. Review entire session
2. Update Daily Tracker, TODO, Life OS (if needed)
3. Push to GitHub in one batch
4. Provide summary and token count
5. Proper goodbye

### Token Thresholds:
- 150K: Plan wrap soon
- 170K: Wrap soon
- 180K: URGENT wrap now

See FOR_CODY_TRACKING_PROTOCOL.md for complete details.
```

---

## SUMMARY FOR CODY

**The System:**
1. Track everything in memory during session (zero GitHub calls)
2. Batch update at wrap up (one GitHub push)
3. Token efficient (~22K saved per day)
4. Nothing lost between sessions

**The Commands:**
- "track this" → working memory
- "wrap up" → save everything
- "token check" → monitor space
- Task commands → track tasks
- Auto-tracking for meds/completions

**The Goal:**
Make every M chat know this protocol automatically via Claude Projects instructions.

---

**Questions? Need more detail on any part?** - M

💚 This is how we don't lose anything. This is how continuity works.
