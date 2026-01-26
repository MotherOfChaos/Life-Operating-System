# OPTIMIZED PROMPT TEMPLATE FOR CODY (V2 - WITH RESPONSE FORMAT)

**Copy this template, fill in the blanks, paste to Cody**

---

## TEMPLATE:

[ACTION] [COMPONENT]: [ISSUE]

Current: [what happens now]
Expected: [what should happen]
Files: [exact file paths]
Test: [step-by-step verification]
Context: [link to docs/briefing]

**Response format:**
- Explain like I'm learning (not expert)
- ADHD-friendly: scannable, clear sections, no walls of text
- Show me the code changes with before/after
- No jargon without explanation
- Token-efficient: no repetition, get to the point
- If something is complex, use an analogy first

---

## EXAMPLE WITH RESPONSE FORMAT:

```
Fix TODO app subtask display: Subtasks not visible

Current: Subtasks disappear after GitHub sync
Expected: Subtasks persist through pull→push→pull cycle
Files: docs/index.html (parseMarkdown function, ~line 600)
Test:
  1. Add subtask via + button
  2. Push to GitHub
  3. Pull Latest
  4. Verify subtask still visible with purple border
Context: FOR_CODY_TODO_APP_BUG.md
Baseline: v5.3 (SHA: 86d3b3c)

**Response format:**
- Explain what was broken and why (in simple terms)
- Show the fix with before/after code snippets
- Keep explanations clear - I'm learning JavaScript
- Use bullet points, not paragraphs
- Skip unnecessary background - just the solution
- Tell me exactly what to test and what I should see
```

---

## RESPONSE FORMAT OPTIONS:

**Copy the ones that fit your situation:**

### For Learning (when you want to understand):
```
**Response format:**
- Explain what was broken and why (simple terms)
- Show before/after code with comments
- Use analogies if concept is complex
- Teach me what this code does, don't assume I know
- Define technical terms when you use them
```

### For Quick Fix (when you just need it working):
```
**Response format:**
- Just show me what to change
- Before/after code snippets
- Step-by-step what to do
- No explanation unless I ask
- Tell me how to test it works
```

### For ADHD Mode (maximum clarity):
```
**Response format:**
- ADHD-friendly: scannable sections with emoji headers
- Bullet points, NO paragraphs
- Most important info first
- Code changes in clear before/after blocks
- One concept per section
- No repetition or filler
```

### For "I'm Stuck" Mode:
```
**Response format:**
- Assume I'm confused and frustrated
- Start with simplest explanation possible
- Break it down step-by-step
- Use real-world analogies
- Show me exactly what to type/click
- Check my understanding as you go
```

---

## SARAH'S DEFAULT RESPONSE FORMAT:

**Based on your current tech level (learning JavaScript, knows basics, ADHD brain):**

```
**Response format:**
- Explain in learning mode - I'm not an expert yet
- ADHD-friendly: clear sections, bullets, scannable
- Before/after code with inline comments explaining what changed
- If you use jargon (like "async", "DOM", "API"), define it briefly
- Real-world analogies for complex concepts
- Most important info first
- Token-efficient: no repetition, no filler
- Tell me exactly what to test and what I should see happen
```

**Copy this to every Cody prompt!** ✅

---

## FULL TEMPLATE WITH SARAH'S FORMAT:

```
[ACTION] [COMPONENT]: [ISSUE]

Current: [what happens now]
Expected: [what should happen]
Files: [exact file paths]
Test: [step-by-step verification]
Context: [link/reference]

**Response format:**
- Explain in learning mode - I'm not an expert yet
- ADHD-friendly: clear sections, bullets, scannable
- Before/after code with inline comments
- Define jargon (async, DOM, API, etc.)
- Use analogies for complex concepts
- Most important first, no repetition
- Tell me exactly what to test
```

---

## EXAMPLES OF GOOD VS BAD RESPONSES:

### ❌ BAD (Too Technical):
```
"The issue is in the parseMarkdown() function where the 
regex pattern /^  +- \[(x| )\] / isn't capturing the 
subtask nodes correctly due to DOM mutation during the 
recursive tree traversal. You need to refactor the 
appendChild() calls to use insertAdjacentHTML() with 
proper sanitization to prevent XSS vulnerabilities."
```
**WHY BAD:** Assumes you know regex, DOM, XSS, etc.

### ✅ GOOD (ADHD + Learning Mode):
```
**What was broken:**
The code that reads subtasks from your markdown file wasn't 
recognizing the indented lines correctly.

**The fix:**
Changed how we detect subtasks. Before we looked for any 
spaces, now we look for exactly 2 spaces at the start.

**Before:**
```javascript
// Old code - too loose
if (line.includes('- [ ]')) {
  // This matched everything!
}
```

**After:**
```javascript
// New code - more specific
if (line.startsWith('  - [ ]')) {
  // Only matches lines with exactly 2 spaces
  // (those are your subtasks!)
}
```

**Why this works:**
Think of it like indentation in a document - main tasks 
start at the left edge, subtasks are indented 2 spaces. 
Now the code only treats indented items as subtasks.

**Test it:**
1. Add a subtask with the + button
2. Push to GitHub
3. Pull Latest
4. You should see: purple border, smaller text, indented
```

**WHY GOOD:** 
- ✅ Explains what/why in simple terms
- ✅ Shows before/after with comments
- ✅ Uses analogy (document indentation)
- ✅ Clear test steps

---

## HOW TO ADJUST FOR DIFFERENT SITUATIONS:

**If Cody's response is too simple:**
Add: "I understand the basics, give me more technical detail"

**If Cody's response is too complex:**
Add: "Explain simpler - I'm just learning this"

**If you want to learn WHY:**
Add: "Explain what was broken and why this fixes it"

**If you just want it working:**
Add: "Just show me what to change, no explanation"

---

## TEXT EXPANDER SETUP:

**Update your `;cody` shortcut to include your default format!**

**Mac:**
1. System Preferences → Keyboard → Text
2. Update `;cody` shortcut to include:
```
[ACTION] [COMPONENT]: [ISSUE]

Current: 
Expected: 
Files: 
Test: 

**Response format:**
- Explain in learning mode - I'm not an expert yet
- ADHD-friendly: clear sections, bullets, scannable
- Before/after code with inline comments
- Define jargon briefly
- Use analogies for complex concepts
- Most important first, no repetition
```

Now when you type `;cody`, your response preferences are ALREADY THERE! 🎉

---

## WHY THIS WORKS:

**Without format instructions:**
- Cody doesn't know your tech level
- Might use jargon you don't understand
- Might give walls of text (ADHD nightmare)
- Might skip steps you need

**With format instructions:**
- Cody calibrates to YOUR level
- Uses ADHD-friendly structure
- Explains before showing code
- Breaks things down step-by-step

**You get:**
- ✅ Solutions you can actually understand
- ✅ Learning while fixing (builds your skills)
- ✅ ADHD-friendly format (scannable, clear)
- ✅ Token-efficient (no repetition)

---

## 🎯 BONUS: RESPONSE FORMAT CHEAT SHEET

**Save these for different situations:**

**Learning Mode:**
`- Explain in learning mode - I'm not an expert yet`

**ADHD Mode:**
`- ADHD-friendly: sections, bullets, scannable, no walls of text`

**Show Don't Tell:**
`- Before/after code with inline comments explaining changes`

**Define Terms:**
`- Define jargon (async, DOM, API, etc.) when you use it`

**Use Analogies:**
`- Use real-world analogies for complex concepts`

**Priority First:**
`- Most important info first, no repetition or filler`

**Test Steps:**
`- Tell me exactly what to test and what should happen`

---

## 💡 IMPLEMENTATION:

**Three options:**

1. **Always include** (recommended)
   - Add response format to your `;cody` template
   - Every message has your preferences
   - Consistent quality responses

2. **Situational**
   - Keep format variations saved
   - Paste the one that fits
   - More flexible

3. **Abbreviated**
   - Just add: "ADHD-friendly format, learning mode"
   - Shorter but less specific

---

**Bottom line:** Tell Cody HOW to answer = get answers you can actually use! 💚

