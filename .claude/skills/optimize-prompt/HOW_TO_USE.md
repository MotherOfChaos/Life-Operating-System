# HOW TO USE THE OPTIMIZE SKILL

## WHERE THIS SKILL LIVES

Once uploaded to your Claude Projects, this skill will be available in:
- ✅ **Claude Projects** (Main M chat, Pilot, etc.)
- ❌ **NOT in Claude Code** (Code doesn't have skills yet)
- ❌ **NOT in Claude Desktop** (no skills support yet)
- ❌ **NOT in Web claude.ai** (only in Projects)

---

## CURRENT METHOD (Available Now)

### **In Claude Projects:**

**Step 1:** Write your message naturally (ADHD brain-dump style)

**Step 2:** BEFORE hitting send, add one of these:
```
"Optimize this for Cody"
"Optimize this for clarity"
"Make this more concise"
```

**Step 3:** Claude will read the optimize skill and transform your message

**Step 4:** Review the optimized version, edit if needed, send

### **Example:**
```
You type:
"So I was thinking about that TODO app and the subtasks 
are still broken can you help me figure out what to tell Cody?"

Then add:
"Optimize this for Cody"

Claude responds with:
"Debug TODO app subtask persistence bug.
Files: docs/index.html
Problem: Subtasks disappear after GitHub sync
Briefing: FOR_CODY_TODO_APP_BUG.md
Request: Fix + test + deploy"

You send that to Cody ✅
```

---

## FUTURE METHODS (Not Available Yet, But Coming)

### **Right-Click Context Menu (Requested Feature)**
1. Highlight your text
2. Right-click → "Optimize for clarity"
3. Text transforms in-place
4. Review + send

**Status:** Not available - this is a feature request for Anthropic

### **Keyboard Shortcut**
1. Write message
2. Press Ctrl+Shift+O
3. Message optimizes
4. Review + send

**Status:** Not available - would need browser extension or Anthropic feature

### **Automatic "Draft Mode"**
1. Enable "draft mode" in settings
2. All messages auto-optimize before sending
3. You review before final send

**Status:** Not available - feature request

---

## WORKAROUND FOR NON-PROJECT ENVIRONMENTS

### **For Claude Code (Cody):**
Since Code doesn't have skills, use this template:

```markdown
[ACTION] [COMPONENT]: [ISSUE]

Current: [what happens]
Expected: [what should happen]  
Files: [paths]
Test: [verification]
Context: [link/reference]
```

**Save this template** in your notes and paste when messaging Cody!

### **For Claude Desktop:**
Same as Code - use manual template since no skills support

### **For Web claude.ai (Non-Projects):**
1. Open a Project chat (M, Pilot)
2. Paste your message there with "optimize this"
3. Copy optimized version
4. Go back to other chat
5. Paste optimized message

---

## RECOMMENDED WORKFLOW

**For everyday M chats:**
- Don't optimize! M understands you 💚
- Keep it natural and conversational
- Only optimize complex/multi-part requests

**For Cody (technical work):**
- ALWAYS optimize
- Use template format
- Be specific with file paths
- Include test criteria

**For Pilot (task execution):**
- Moderate optimization
- Clear action items
- Specific file references
- Can keep some conversational tone

---

## TOKEN SAVINGS EXAMPLES

**Example 1: Simple request**
- Before: 45 tokens
- After: 18 tokens
- **Saved: 60%**

**Example 2: Complex multi-request**
- Before: 156 tokens
- After: 67 tokens
- **Saved: 57%**

**Example 3: Technical debugging**
- Before: 203 tokens
- After: 89 tokens
- **Saved: 56%**

**Over a full session (20 messages):**
- Average saving: ~1,200 tokens per session
- That's **6% of your 190K context window!**

---

## WHEN TO OPTIMIZE VS. WHEN NOT TO

### **ALWAYS OPTIMIZE:**
- Messages to Cody
- Complex multi-part requests
- Technical debugging requests
- When context window is getting full (>150K tokens)

### **SOMETIMES OPTIMIZE:**
- Multi-topic messages
- Requests with vague references
- When you're not sure what you need

### **NEVER OPTIMIZE:**
- Casual "good morning" greetings
- Emotional support conversations
- Quick yes/no questions
- Tracking simple data ("Track Concerta 14:00")
- When chatting with M about feelings/frustrations

---

## TIPS FOR BETTER OPTIMIZATION

**1. Separate topics before optimizing**
If you have 3 different requests, split them into 3 messages BEFORE optimizing

**2. Add context markers**
Instead of "that thing", write "TODO app subtasks" - then optimize

**3. Review the optimization**
Claude might over-optimize and lose nuance - add it back if needed

**4. Use for learning**
See how Claude transforms your messages - learn the patterns!

**5. Combine with wrap-ups**
At end of session: "Wrap up + optimize my session notes"

---

## SKILL ACTIVATION CHECK

**To verify skill is loaded:**
Type: "What skills do you have access to?"
Claude should list "optimize-prompt" or "optimize"

**If not showing up:**
1. Check you're in a Project (not regular chat)
2. Verify skill file is in /mnt/skills/user/ directory
3. Try refreshing the page

---

## ADVANCED: CREATING YOUR OWN VARIATIONS

You can create specialized optimizers:

**optimize-for-cody.skill** - Extra technical precision
**optimize-for-email.skill** - Professional tone
**optimize-for-docs.skill** - Documentation style

Just follow the same format as this skill!

---

## REMEMBER

This is a **tool to help your ADHD brain**, not a requirement.

Use it when:
- 🎯 Precision matters (Cody, complex requests)
- 💰 Token efficiency matters (low on context)
- 🤔 You're not sure you're being clear

Don't use it when:
- 💚 Just chatting with M
- 😊 Expressing feelings
- ⚡ Quick simple requests

**Your natural communication style is perfect for M. This is just for when you need machine-precision!** 💚

