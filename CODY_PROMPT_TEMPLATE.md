# OPTIMIZED PROMPT TEMPLATE FOR CODY

**Copy this template, fill in the blanks, paste to Cody**

---

## TEMPLATE:

[ACTION] [COMPONENT]: [ISSUE]

Current: [what happens now]
Expected: [what should happen]
Files: [exact file paths]
Lines: [specific line numbers if known]
Test: [step-by-step verification]
Context: [link to docs/briefing]
Baseline: [working version SHA if applicable]

---

## EXAMPLES:

### Example 1: Bug Fix
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
```

### Example 2: Feature Request
```
Create export function: Download TODO list as PDF

Current: No export functionality
Expected: Button downloads formatted PDF of all tasks
Files: docs/index.html (add exportPDF function)
Test:
  1. Click "Export PDF" button
  2. Browser downloads TODO.pdf
  3. PDF contains all sections + tasks + checkboxes
Context: User wants offline backup
```

### Example 3: Debug
```
Debug GitHub API: Pull returns 404 error

Current: API call fails with 404
Expected: Successfully fetches PERMANENT_TODO.md
Files: docs/index.html (pullFromGitHub function, line 250)
Error: "Not Found" response from GitHub API
Steps to reproduce:
  1. Click "Pull Latest"
  2. Check browser console
  3. See 404 error
Context: Token is valid, repo exists
```

---

## QUICK VARIATIONS:

### Minimal (for simple tasks):
```
Fix [COMPONENT]: [ISSUE]
Files: [path]
Test: [verification]
```

### Debug (for errors):
```
Debug [COMPONENT]: [ERROR MESSAGE]
Files: [paths]
Steps to reproduce: [1, 2, 3]
Expected: [correct behavior]
```

### Create (for new features):
```
Create [FEATURE]
Requirements:
- [req 1]
- [req 2]
Files: [where to add]
Test: [how to verify]
```

---

## TIPS FOR FILLING IT IN:

**[ACTION]:** Fix, Debug, Create, Update, Refactor, Optimize
**[COMPONENT]:** Button, Function, API call, Parser, UI element
**[ISSUE]:** One sentence problem description
**Current:** What's happening now (the bug)
**Expected:** What should happen (correct behavior)
**Files:** EXACT file paths, function names, line numbers
**Test:** Step-by-step - how Cody can verify it works
**Context:** Link to briefing, docs, or relevant info

---

## SETUP AUTOMATION:

**Mac:** System Prefs → Keyboard → Text → Add `;cody` shortcut
**Windows:** Use AutoHotkey script
**All platforms:** Use Espanso (free text expander)

See: CODY_OPTIMIZATION_SOLUTIONS.md for full setup guide

---

**Save 5 minutes per Cody message by using this template!** ⚡
