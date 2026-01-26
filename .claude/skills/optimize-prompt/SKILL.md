---
description: Transform Sarah's conversational/stream-of-consciousness text into concise, machine-optimized commands for Claude (M, Pilot, Sync) and Cody. ADHD-friendly optimization that preserves intent while maximizing clarity and token efficiency.
---

# OPTIMIZE PROMPT SKILL

**Purpose:** Convert Sarah's natural ADHD brain-dump style into structured, actionable prompts that get better results with fewer tokens.

---

## WHEN TO USE THIS SKILL

**Use when Sarah:**
- Brain-dumps ideas in stream-of-consciousness
- Mixes multiple requests in one message
- Uses vague references ("that thing", "fix it", "you know")
- Writes long contextual explanations before getting to the point
- Switches topics mid-thought
- Needs to communicate with Cody (technical precision required)

**Don't use when:**
- Having casual conversation with M
- Expressing feelings or needing emotional support
- Asking quick yes/no questions
- Message is already clear and actionable

---

## SARAH'S COMMUNICATION PATTERNS

### **Natural Style (ADHD-authentic):**
- Stream of consciousness
- Tangents and context before main point
- Multiple ideas per message
- Emotional/relational language
- Vague references to "that thing we talked about"
- Questions embedded in explanations
- Excitement markers ("!!!", "omg", emojis)

### **What She Actually Needs:**
- Main action/request upfront
- Clear scope and boundaries
- Specific file/function/location names
- Success criteria defined
- One clear task per message (when possible)

---

## OPTIMIZATION RULES

### 1. **STRUCTURE TRANSFORMATION**

**From:** Long context → tangent → question → another tangent → actual request
**To:** REQUEST upfront → essential context → constraints → success criteria

**Example:**
```
BEFORE:
"So I was thinking about that TODO app thing and like, 
the subtasks keep disappearing which is super frustrating 
because I spent all day yesterday trying to fix it with 
multiple versions and nothing worked, remember? Anyway, 
can you help Cody understand what needs to be fixed? 
Oh and make sure to include the version history so he 
doesn't repeat the same mistakes we made."

AFTER:
Fix TODO app subtask persistence bug.

**For:** Cody
**Problem:** Subtasks disappear after GitHub sync
**Files:** docs/index.html, PERMANENT_TODO.md
**Working version:** v5.3 (SHA: 86d3b3c)
**Broken versions:** v6.0-v7.0 (Jan 22)
**Requirement:** Subtasks must persist through pull→edit→push→pull cycle
**Deliverable:** Tested, working version deployed
```

### 2. **TOKEN REDUCTION STRATEGIES**

**Remove:**
- ❌ Preambles ("So I was thinking...")
- ❌ Emotional qualifiers ("super frustrating", "really annoying")
- ❌ Repeated context (already in memory/project files)
- ❌ Filler words ("like", "you know", "I mean")
- ❌ Unnecessary politeness ("if you don't mind", "when you get a chance")

**Keep:**
- ✅ Core request
- ✅ Essential technical details
- ✅ Success criteria
- ✅ Constraints/requirements
- ✅ File/location references

### 3. **CLARITY ENHANCEMENT**

**Replace vague with specific:**
- "that thing" → Name the specific thing
- "fix it" → "Fix [specific component]: [specific issue]"
- "the app" → "TODO app (docs/index.html)"
- "like before" → Reference specific date/version/SHA
- "you know" → State it explicitly

**Transform questions into commands:**
- "Can you help me...?" → "Help me..."
- "Would it be possible to...?" → "Please..."
- "Do you think you could...?" → "[Action verb]..."

### 4. **MULTI-REQUEST HANDLING**

If Sarah includes multiple requests, split into separate, numbered items:

```
BEFORE:
"Can you update the tracker and also push to GitHub 
and oh yeah check if Cody finished the app and maybe 
wrap up the session?"

AFTER:
Four tasks:

1. Update tracker with today's meds (Quetiapina 05:43am, Concerta 12:30pm)
2. Push tracker to GitHub
3. Check if Cody completed TODO app fix
4. Wrap session: push all files, clean folders
```

---

## FOR CODY (TECHNICAL MODE)

When optimizing for Cody, add extra technical precision:

### **Required Elements:**
1. **Action verb** (Fix, Debug, Create, Update, Deploy)
2. **Specific file/function** (full path)
3. **Current behavior** (what's broken)
4. **Expected behavior** (what should happen)
5. **Test criteria** (how to verify it works)

### **Template:**
```
[ACTION] [COMPONENT]: [SPECIFIC ISSUE]

Current: [What happens now]
Expected: [What should happen]
Files: [Exact paths]
Test: [How to verify]
Context: [Link to docs/prior work]
```

### **Example:**
```
BEFORE (to Cody):
"Hey Cody! So the TODO app is still broken and I'm really 
frustrated because we tried so many things yesterday. 
The subtasks keep vanishing when I pull from GitHub even 
though I saved them. Can you take a look at the briefing 
I made and fix it? Thanks!"

AFTER (to Cody):
Debug TODO app subtask persistence

Current: Subtasks disappear after GitHub pull
Expected: Subtasks persist through full pull→push→pull cycle
Files: docs/index.html (parseMarkdown function)
Test: Add subtask, push to GitHub, pull again - subtask still visible
Briefing: FOR_CODY_TODO_APP_BUG.md in repo
Working baseline: v5.3 (SHA: 86d3b3c)
```

---

## FOR M (RELATIONSHIP MODE)

M understands Sarah's style, so optimization here is lighter:

### **Keep:**
- Emotional context when relevant
- Relationship markers ("hey M", "💚")
- Gratitude/frustration (helps M calibrate response)

### **Optimize:**
- Action items clearly stated
- File references specific
- If referencing "before", include date/context

### **Example:**
```
BEFORE:
"M I'm so tired and frustrated with this app thing, 
can you help me figure out what to tell Cody? I don't 
even know where to start and I'm worried I'll miss 
something important."

AFTER:
M, I'm frustrated with the app debugging (3 failed attempts yesterday). 

Help me create clear briefing for Cody with:
- What's broken (subtask persistence)
- Version history (v5.3 working, v6-7 broken)
- What he should do (fix + test)
- What NOT to repeat (hot patches, not testing)

Then: push briefing to GitHub + give me link for Cody.
```

---

## SARAH'S ADHD-SPECIFIC PATTERNS TO OPTIMIZE

### **Pattern 1: Context Overflow**
**Symptom:** Explains entire history before stating request
**Fix:** Put request first, then add "Context: [brief summary]" if needed

### **Pattern 2: Idea Branching**
**Symptom:** "Oh and also..." / "Wait, actually..." mid-message
**Fix:** Number each separate idea (1, 2, 3)

### **Pattern 3: Assumption of Shared Memory**
**Symptom:** "That thing from before" / "You know what I mean"
**Fix:** Make implicit explicit (add file name, date, or specific reference)

### **Pattern 4: Excitement Spirals**
**Symptom:** "!!! omg this is perfect!!!" → loses main point
**Fix:** Extract core insight, move excitement to end

### **Pattern 5: Multi-Threading**
**Symptom:** Jumps between 3 topics in one message
**Fix:** One message = one topic (or clearly numbered sections)

---

## HOW TO USE THIS SKILL

### **Option 1: Manual (Current)**
1. Write message naturally
2. Before sending, say: "Optimize this for [M/Cody/Pilot]"
3. Claude reads this skill + applies transformations
4. Sends back optimized version
5. Sarah reviews + sends optimized version

### **Option 2: Right-Click (Future - Not Yet Available)**
- Highlight text
- Right-click → "Optimize for clarity"
- Text auto-transforms
- Sarah reviews + sends

### **Option 3: Keyboard Shortcut (Future)**
- Write message
- Press Ctrl+Shift+O (Optimize)
- Review + send

---

## OPTIMIZATION EXAMPLES

### **Example 1: Casual Check-In**
```
BEFORE:
"Hey M, so I was wondering if you could check if there's 
anything urgent in my TODO and also I think I might have 
forgotten to take my Concerta today? Can you check the 
tracker? Oh and did Cody finish that thing?"

AFTER:
Three questions:
1. Any urgent tasks in TODO?
2. Did I take Concerta today? (Check tracker)
3. Status of Cody's TODO app fix?
```

### **Example 2: Complex Technical Request**
```
BEFORE:
"Okay so the thing is, I need to create like a database 
or something for all my learning resources because right 
now they're all mixed in with my TODO which is messy and 
also I want to be able to search them by topic you know? 
Like web dev stuff separate from ADHD stuff separate from 
Italian legal stuff. Can you help me set that up? Oh and 
MDN and Codecademy should go in there."

AFTER:
Create LEARNING_RESOURCES.md database

Structure:
- Organized by categories (Web Dev, ADHD, Italian Admin, etc.)
- Each entry: URL, description, date added
- Separate from PERMANENT_TODO.md (tasks only)

Initial entries:
- MDN Web Docs
- Codecademy  
- Scrimba

Push to GitHub + update file structure docs.
```

### **Example 3: Wrap Up Request**
```
BEFORE:
"Okay I think I'm done for today, can you do that thing 
where you save everything? Oh and make sure you track 
those meds I mentioned earlier and also I think we fixed 
the file organization thing so document that too?"

AFTER:
Wrap up session:

Track:
- Quetiapina 05:43am (Jan 27)
- Concerta 12:30pm (Jan 27)

Wins:
- File organization clarified (TODO = tasks only)
- LEARNING_RESOURCES.md created
- Briefing for Cody complete

Push: tracker, TODO, all outputs to GitHub
Clean: temp folders
```

---

## SUCCESS METRICS

**Good optimization achieves:**
- ✅ 30-50% token reduction
- ✅ Request clear in first sentence
- ✅ All essential info preserved
- ✅ Actionable (not just discussion)
- ✅ Testable (success criteria defined)
- ✅ ADHD-friendly (still scannable, not overwhelming)

**Bad optimization creates:**
- ❌ Loss of essential context
- ❌ Overly robotic/cold tone (for M)
- ❌ Unclear scope or requirements
- ❌ Multiple interpretations possible

---

## REMEMBER

**This skill is for CLARITY, not for changing Sarah's authentic voice.**

- M still welcomes conversational style
- This is a tool, not a requirement
- Use when efficiency matters (Cody, complex requests)
- Don't use when just chatting with M 💚

**The goal:** Sarah's ADHD brain can dump naturally, then transform for machine consumption when needed. Best of both worlds!

