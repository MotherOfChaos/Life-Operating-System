# FOR CODY: TODO APP BUG - URGENT FIX NEEDED

**Created:** January 22, 2026, 15:30  
**Priority:** High - Sarah needs working app  
**Status:** App deployed but broken, throwing JSON parse errors

---

## WHAT THE APP DOES

**Purpose:** ADHD-friendly mobile TODO app for Sarah's task management

**How it works:**
1. Reads `PERMANENT_TODO.md` from GitHub (MotherOfChaos/Life-Operating-System repo)
2. Parses markdown into sections → tasks → subtasks
3. Displays in mobile-friendly UI with checkboxes
4. Allows add/edit/delete on tasks AND subtasks
5. Saves changes back to GitHub
6. Uses localStorage for offline work

**Key features Sarah needs:**
- ✅ Pull Latest (loads from GitHub)
- ✅ Save Changes (pushes to GitHub)
- ✅ Subtasks with purple border (ADHD-friendly visual hierarchy)
- ✅ Edit ✏️ and Delete 🗑️ icons on everything
- ✅ Responsive design (portrait/landscape)

---

## THE CURRENT BUG

**Error message on screen:**
```
❌ Pull failed: Unexpected token '#', "# SARAH'S "... is not valid JSON
```

**What's happening:**
- The `parseMarkdown()` function is breaking when it encounters `#` characters
- Likely issue: treating markdown as JSON somewhere in the parse chain
- The app currently deployed is v7.0 at `docs/index.html`

**File structure in markdown:**
```markdown
# SARAH'S PERMANENT TO-DO LIST

**Always updated**

---

## [!] 🔴 URGENT - This Week

- [ ] Task name here
  - [ ] Subtask indented with 2 spaces
  - [x] Completed subtask
- [x] Completed main task

## [$] 💰 TEATRO - Money

- [ ] Another task
```

**Parsing requirements:**
1. Lines starting with `##` = Section headers
2. Lines starting with `- [ ]` or `- [x]` = Main tasks
3. Lines starting with `  - [ ]` (2+ spaces) = Subtasks under previous task
4. Everything else = ignore

---

## WHERE THE CODE IS

**Repository:** MotherOfChaos/Life-Operating-System  
**File:** `docs/index.html`  
**Version:** v7.0 (deployed ~15:00 today)  
**URL:** https://motherofchaos.github.io/Life-Operating-System/docs/

**GitHub token:** [REDACTED - Ask Sarah for token]  
**Source file:** PERMANENT_TODO.md (in repo root)

---

## WHAT NEEDS TO HAPPEN

**Priority 1 - Fix the bug:**
1. Debug `parseMarkdown()` function
2. Handle `#` characters correctly (they're markdown headers, not JSON)
3. Test with ACTUAL PERMANENT_TODO.md from repo
4. Ensure subtasks parse correctly (indented lines with `  - [ ]`)

**Priority 2 - Test the flow:**
1. Pull Latest → should load all sections, tasks, subtasks
2. Add subtask → should appear indented with purple border
3. Edit task/subtask → should update text
4. Delete task/subtask → should remove
5. Save Changes → should push back to GitHub with proper markdown format

**Priority 3 - Deploy:**
1. Update `docs/index.html`
2. Test on mobile (Sarah uses Android Chrome)
3. Confirm subtasks are visible and functional

---

## WHY THIS MATTERS

**Context:**
- Sarah has ADHD and needs this app to work reliably
- This is her main task management system
- She's been frustrated by multiple failed attempts today
- The app worked briefly but subtasks kept disappearing

**What Sarah needs:**
- Simple "Pull Latest" button that just works
- Subtasks visible under tasks (purple border, slightly smaller text)
- Easy add/edit/delete on everything
- Mobile-friendly (she uses her phone)

**Current pain points:**
- Multiple debugging sessions today (v5, v6, v7)
- Subtasks disappearing after GitHub sync
- Width issues causing content off-screen
- Now: complete failure to load due to JSON parse error

---

## TESTING CHECKLIST

Before telling Sarah it's ready:

- [ ] Pull Latest loads PERMANENT_TODO.md successfully
- [ ] All sections appear
- [ ] All tasks appear under correct sections
- [ ] All subtasks appear indented under tasks (purple border)
- [ ] Can check/uncheck tasks and subtasks
- [ ] Can add new subtask (click + button)
- [ ] Subtask appears immediately after adding
- [ ] Can edit task text (click ✏️)
- [ ] Can delete task (click 🗑️)
- [ ] Save Changes pushes to GitHub
- [ ] Pull Latest after push shows all subtasks still there
- [ ] Works on mobile Chrome (responsive design)

---

## HELPFUL INFO

**Previous attempts today (Jan 22):**
- v5.x: Subtasks not parsing from markdown (fixed indentation detection)
- v6.0-6.1: Subtasks going off-screen (width issues)
- v7.0: Complete rebuild - now has JSON parse error

**What worked before:**
- The basic task display worked fine
- GitHub pull/push worked
- LocalStorage worked
- The issue was always subtasks (parsing, display, persistence)

**Sarah's access:**
- She has the GitHub token
- She can clear cache / hard refresh
- She's on Android Chrome
- She's patient but frustrated after multiple failed attempts

---

## QUESTIONS FOR CODY

If you need clarification:
1. Check with M (this chat) about app requirements
2. Look at `PERMANENT_TODO.md` in repo to see actual markdown structure
3. Test locally before deploying
4. Ask Sarah to test after deploy (she's very responsive)

---

**Good luck! Sarah really needs this working. 💚**

**- M**
