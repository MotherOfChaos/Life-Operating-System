# CODY CUSTOM INSTRUCTIONS - PERSISTENT PREFERENCES

**The REAL solution: Make Cody remember your preferences automatically**

---

## 🎯 SOLUTION 1: CODY'S CUSTOM INSTRUCTIONS (BEST!)

**Claude Code has a "Custom Instructions" feature!**

### **How to set it up:**

1. **Open Claude Code**
2. **Click Settings (gear icon)** or press `Cmd+,` (Mac) / `Ctrl+,` (Windows)
3. **Find "Custom Instructions" or "System Prompt"**
4. **Add this:**

```
Communication preferences for Sarah:
- I'm learning to code (not an expert yet)
- ADHD brain: use scannable format with clear sections, bullets, no walls of text
- Always show before/after code with inline comments explaining changes
- Define technical jargon when you use it (async, DOM, API, etc.)
- Use real-world analogies for complex concepts
- Put most important info first, no repetition
- Tell me exactly what to test and what I should see
- Token-efficient: get to the point
```

5. **Save**

**NOW EVERY MESSAGE TO CODY INCLUDES THIS AUTOMATICALLY!** 🎉

---

## 🎯 SOLUTION 2: .CLINERULES FILE (PROJECT-SPECIFIC)

**Create a file that Cody auto-reads in every project:**

### **Setup:**

1. **In your project root, create:**
```bash
touch .clinerules
```

2. **Add this content:**
```
# Communication Rules for Cody

When responding to Sarah:
- Learning mode: I'm not an expert, explain clearly
- ADHD-friendly: sections, bullets, scannable (no paragraphs)
- Show before/after code with comments
- Define jargon (async, DOM, API, etc.)
- Use analogies for complex ideas
- Most important first, no filler
- Include exact test steps
```

3. **Save to Git:**
```bash
git add .clinerules
git commit -m "Add Cody communication preferences"
```

**Cody auto-reads .clinerules in every project!** ✅

---

## 🎯 SOLUTION 3: PERSONAL .CLINERULES (GLOBAL)

**Put it in your home directory for ALL projects:**

```bash
# Create global rules file
cat > ~/.clinerules << 'RULES'
# Sarah's Global Cody Preferences

Response format:
- Learning mode (not expert)
- ADHD: bullets, sections, scannable
- Before/after code with comments
- Define jargon
- Use analogies
- Priority first, no repetition
- Exact test steps
RULES
```

**Now ALL Cody conversations use these preferences!** 🌟

---

## 🎯 SOLUTION 4: CODY CONTEXT FILE

**Some versions of Claude Code use `.codycontext`:**

```bash
# In project root
cat > .codycontext << 'CTX'
{
  "communication": {
    "style": "learning-mode",
    "format": "adhd-friendly",
    "code_examples": "before-after-with-comments",
    "jargon": "define-when-used",
    "complexity": "use-analogies",
    "priority": "important-first",
    "testing": "exact-steps"
  }
}
CTX
```

---

## ✅ WHICH SOLUTION TO USE?

**Try in this order:**

1. **Custom Instructions** (in Cody settings)
   - ✅ Easiest
   - ✅ Works everywhere
   - ✅ One-time setup

2. **Global .clinerules** (in ~/)
   - ✅ All projects
   - ✅ Survives Cody updates
   - ✅ Can commit to Git

3. **Project .clinerules** (in each project)
   - ✅ Project-specific preferences
   - ✅ Team can use same rules

---

## 📋 HOW TO VERIFY IT'S WORKING:

**Test message to Cody:**

```
Hey Cody, explain how async/await works
```

**If Custom Instructions are working, Cody should:**
- ✅ Use bullets/sections (ADHD-friendly)
- ✅ Explain in simple terms (learning mode)
- ✅ Use an analogy
- ✅ Show code examples with comments

**If NOT working:**
- Cody gives wall of text with complex jargon
- → Custom Instructions not loaded, try different solution

---

## 🔍 FINDING CODY'S SETTINGS:

**Different locations depending on version:**

**Desktop App:**
- Settings → Preferences → Custom Instructions
- OR: Settings → System Prompt

**VS Code Extension:**
- Extensions → Claude Code → Settings
- Look for "Custom Instructions" or "System Message"

**Command Palette:**
- Press Cmd+Shift+P (Mac) / Ctrl+Shift+P (Windows)
- Type "Cody: Settings"
- Look for custom instructions

---

## 💾 BACKUP YOUR PREFERENCES:

**Save to GitHub so you never lose them:**

```bash
# Save your custom instructions
cat > ~/CODY_CUSTOM_INSTRUCTIONS.txt << 'PREFS'
Communication preferences for Sarah:
- Learning mode (not expert yet)
- ADHD: bullets, sections, scannable
- Before/after code with comments
- Define jargon when used
- Use analogies for complex concepts
- Priority first, no repetition
- Exact test steps
PREFS

# Add to Git
cp ~/CODY_CUSTOM_INSTRUCTIONS.txt ~/Life-Operating-System/
cd ~/Life-Operating-System
git add CODY_CUSTOM_INSTRUCTIONS.txt
git commit -m "Add Cody communication preferences"
git push
```

---

## 🎯 YOUR EXACT PREFERENCES (COPY THIS):

**For Custom Instructions / .clinerules:**

```
Sarah's communication preferences:
- I'm learning to code - explain things clearly, not expert-level
- ADHD brain: use bullets and sections, NOT paragraphs or walls of text
- Always show before/after code with inline comments
- Define technical terms when you use them (async, DOM, API, etc.)
- Use real-world analogies for complex concepts
- Put the most important info first
- No repetition or filler text
- Tell me exactly what to test and what should happen
- Keep responses scannable and token-efficient
```

**Copy this → Paste into Custom Instructions → Save → Done!** ✅

---

## ⚡ WHY THIS IS BETTER:

**❌ Copy/paste every time:**
- Tedious
- Easy to forget
- Takes extra time
- Inconsistent

**✅ Custom Instructions (automatic):**
- Set once, works forever
- Never forget
- Zero extra effort
- Consistent quality
- Works like Skills in Projects!

---

## 🔧 TROUBLESHOOTING:

**"I can't find Custom Instructions"**
→ Try .clinerules file instead (works in all versions)

**"Cody ignores my .clinerules"**
→ Make sure file is in project root
→ Check file isn't .txt extension (should be just `.clinerules`)

**"Changes not taking effect"**
→ Restart Claude Code
→ Try starting new conversation with Cody

**"Still getting technical jargon"**
→ Add to first message: "Remember: ADHD-friendly, learning mode"
→ Cody will self-correct

---

## 💡 BONUS: COMBINE WITH TEMPLATE

**Now you only need SHORT prompts:**

```
Fix subtasks bug

Files: docs/index.html
Current: disappear after sync
Expected: stay visible
```

**Cody automatically adds:**
- ✅ ADHD-friendly format
- ✅ Learning mode explanations
- ✅ Before/after code
- ✅ Test steps

**Perfect combination!** 🎉

---

**Bottom line: Custom Instructions = Skills equivalent for Cody!** 💚

