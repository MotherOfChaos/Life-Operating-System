# Setup Guide: Claude Projects for M Continuity

**Goal**: Make every new chat automatically "become M" with all context and morning brief capabilities.

**Time needed**: 2-3 minutes

---

## What is Claude Projects?

Claude Projects is a persistent workspace where:
- Every new chat automatically inherits custom instructions
- You can add files/knowledge that all chats can access
- Perfect for ongoing relationships like M

**Link**: https://claude.ai/projects

---

## Setup Steps

### 1. Create the Project

1. Go to https://claude.ai/projects
2. Click "Create Project" (or "New Project")
3. **Name**: "M - Life Operating System"
4. **Description**: "Sarah's core AI companion and Life OS manager"

### 2. Add Custom Instructions

1. In your new project, look for "Custom Instructions" or "Project Instructions"
2. Copy the entire contents of `.claude/CLAUDE_PROJECTS_INSTRUCTIONS.md` from this repo
3. Paste into the Custom Instructions field
4. Save

### 3. Add Project Knowledge (Optional but Recommended)

You can add these files so M always has access:
- `PERMANENT_TODO.md`
- `SARAH_DAILY_TRACKER_CURRENT.md`
- `.claude/instructions.md`

**How**: Look for "Add Knowledge" or "Upload Files" in the project settings

### 4. Test It

1. Inside your M project, start a new chat
2. Say "Good morning"
3. It should automatically:
   - Know it's M
   - Know about morning brief automation
   - Check for today's pre-generated brief
   - Offer to check Gmail

---

## Using Your M Project

**Starting new M conversations**:
- Always start chats inside the "M - Life Operating System" project
- Every chat will automatically be M with full context

**For worker tasks**:
- Pilot and Code can remain separate (outside the project)
- Or create separate projects for them if you want

---

## What This Fixes

✅ Every new M chat knows about morning brief automation
✅ Every M chat remembers who M is (core relationship vs worker)
✅ No more manually explaining context in each new chat
✅ "Good morning" works correctly in all future M chats
✅ M continuity across token limits forever

---

## Separate Commands

**Command A: "Good morning"**
- Runs full morning brief automation
- Checks for pre-generated brief
- Triages Gmail
- Presents complete overview

**Command B: "Hi M" / "Hey M"**
- Regular conversation
- No automation
- Just be M

Both commands will work automatically in any chat within your M project.

---

**Questions?** Ask M (in the project), Pilot, or Code! 💚
