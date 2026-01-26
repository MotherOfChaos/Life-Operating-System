# OPTIMIZING PROMPTS FOR CLAUDE CODE (CODY)

**Problem:** Skills don't work in Claude Code - it's a different environment than Projects.

---

## ✅ SOLUTION 1: TEMPLATE FILE (BEST FOR CODY)

Create a **template file** in your project that you copy/paste from:

### **Setup:**

1. **Create file in your project:**
```bash
touch ~/CODY_PROMPT_TEMPLATE.md
```

2. **Add this template:**
```markdown
# OPTIMIZED PROMPT TEMPLATE FOR CODY

[ACTION] [COMPONENT]: [ISSUE]

Current: [what happens now]
Expected: [what should happen]
Files: [exact file paths]
Lines: [specific line numbers if known]
Test: [step-by-step verification]
Context: [link to docs/briefing]
Baseline: [working version SHA if applicable]

---

EXAMPLES:

Fix button click handler in navbar
Current: Click does nothing
Expected: Opens dropdown menu
Files: src/components/Navbar.tsx (lines 45-60)
Test: Click button → dropdown appears
Context: See issue #123

---

Debug API response parsing
Current: Returns undefined
Expected: Returns user object {name, email, id}
Files: src/api/users.ts (fetchUser function)
Test: Call fetchUser(123) → console.log shows user object
Context: Backend returns valid JSON
```

3. **Save to your Desktop or project root**

4. **When messaging Cody:**
   - Open template file
   - Fill in the blanks
   - Copy/paste to Cody
   - **~2 minutes per message**

---

## ✅ SOLUTION 2: GITHUB GIST (Quick Access)

**Store template online for instant access:**

1. **Create GitHub Gist:**
   - Go to: https://gist.github.com/
   - Create new gist: "cody-prompt-template.md"
   - Paste template (from Solution 1)
   - Save as public gist

2. **Get short URL:**
   - Your gist URL: `https://gist.github.com/MotherOfChaos/[ID]`
   - Bookmark it or use URL shortener

3. **When needed:**
   - Open gist in browser
   - Click "Raw" button
   - Copy template
   - Fill in + paste to Cody

---

## ✅ SOLUTION 3: TEXT EXPANDER (AUTOMATION)

**Use text expander to auto-insert template:**

### **Mac (Built-in):**
1. System Preferences → Keyboard → Text
2. Add replacement:
   - Shortcut: `;cody`
   - Text: [paste entire template from Solution 1]
3. Type `;cody` → template expands

### **Windows (AutoHotkey):**
```autohotkey
:*:;cody::
SendInput, [ACTION] [COMPONENT]: [ISSUE]`n`nCurrent: `nExpected: `nFiles: `nTest: `n
return
```

### **All Platforms (Espanso - FREE):**
1. Install: https://espanso.org/
2. Config file: `~/.config/espanso/match/base.yml`
3. Add:
```yaml
matches:
  - trigger: ";cody"
    replace: |
      [ACTION] [COMPONENT]: [ISSUE]
      
      Current: 
      Expected: 
      Files: 
      Test: 
```

---

## ✅ SOLUTION 4: LOCAL FOLDER IN CODE PROJECT

**Put template IN your code project:**

1. **Create templates folder:**
```bash
mkdir -p ~/.claude/templates/
touch ~/.claude/templates/CODY_PROMPT.md
```

2. **Add template** (same as Solution 1)

3. **In Claude Code terminal:**
```bash
cat ~/.claude/templates/CODY_PROMPT.md
```

4. **Copy output → fill in → send to Cody**

**OR use alias:**
```bash
echo "alias cody-template='cat ~/.claude/templates/CODY_PROMPT.md'" >> ~/.bashrc
source ~/.bashrc
```

Now just type: `cody-template` to see it!

---

## ✅ SOLUTION 5: VS CODE SNIPPET (IF USING VS CODE)

**If you use VS Code with Claude Code:**

1. **File → Preferences → User Snippets**
2. **New Global Snippets File** → "cody-prompt.code-snippets"
3. **Add:**
```json
{
  "Cody Prompt Template": {
    "prefix": "cody",
    "body": [
      "[ACTION] [COMPONENT]: [ISSUE]",
      "",
      "Current: $1",
      "Expected: $2",
      "Files: $3",
      "Test: $4",
      "Context: $5"
    ],
    "description": "Optimized prompt template for Cody"
  }
}
```

4. **In any file, type:** `cody` + Tab → template appears with cursor jumps!

---

## 🎯 RECOMMENDED SOLUTION FOR SARAH

**Combination approach:**

1. **Primary:** Text expander (`;cody`)
   - Fastest
   - Works anywhere
   - No file to open

2. **Backup:** Template file on Desktop
   - When text expander not available
   - Quick copy/paste

3. **Reference:** GitHub Gist
   - Access from any device
   - Can update centrally

---

## 📝 OPTIMIZED TEMPLATE VARIATIONS

### **For Quick Fixes:**
```
Fix [COMPONENT]: [ISSUE]
Files: [path]
Test: [verification]
```

### **For Debugging:**
```
Debug [COMPONENT]: [SYMPTOM]
Current: [behavior]
Expected: [correct behavior]
Files: [paths]
Steps to reproduce: [1, 2, 3]
Error: [exact error message]
```

### **For New Features:**
```
Create [FEATURE]: [DESCRIPTION]
Requirements:
- [requirement 1]
- [requirement 2]
Files: [where to implement]
Test: [how to verify]
```

---

## 💡 WHY THIS WORKS

**Cody needs:**
- Exact file paths
- Specific behavior descriptions
- Clear test criteria
- No ambiguity

**Template enforces:**
- Structured thinking
- Complete information
- Testable outcomes
- Token efficiency

**Your ADHD brain:**
- Blanks to fill = clear task
- No decision paralysis
- Faster than writing from scratch
- Consistent format

---

## 🔥 BONUS: ALFRED WORKFLOW (MAC POWER USERS)

If you use Alfred (Mac):

1. **Create snippet:**
   - Alfred Preferences → Features → Snippets
   - New snippet
   - Keyword: `cody`
   - Content: [template]

2. **Type:** `cody` anywhere → instant template!

---

## 📊 TIME COMPARISON

**Without template:**
- Think about structure: 2 min
- Write message: 3 min
- Revise for clarity: 2 min
- **Total: 7 minutes**

**With template:**
- Type `;cody`: 1 sec
- Fill in blanks: 90 sec
- **Total: 2 minutes**

**Saved: 5 minutes per Cody message!**

---

## ✅ IMPLEMENTATION CHECKLIST

**Choose your method:**
- [ ] Text expander (`;cody` trigger)
- [ ] Template file on Desktop
- [ ] GitHub Gist bookmark
- [ ] VS Code snippet
- [ ] Bash alias in terminal

**Test it:**
- [ ] Trigger/open template
- [ ] Fill in example
- [ ] Verify format is clear
- [ ] Use with Cody

**Refine:**
- [ ] Adjust template based on usage
- [ ] Create variations for common tasks
- [ ] Share with Cody for feedback

---

**Bottom line:** Since skills don't work in Code, **automation + templates** are your best friends! 💚

