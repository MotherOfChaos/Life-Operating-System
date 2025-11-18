---
name: news-intelligence
description: Daily balanced news intelligence from global sources, personalized for Sarah in Barcelona. Provides "Status of the World Today" by scanning multiple international outlets, separating facts from opinions, and presenting diverse perspectives across political leans. Focus on Europe (especially Spain/Italy), world news, arts/culture, science, tech/business, with minimal sports coverage.
---

# News Intelligence Skill - Personalized Edition

This skill provides balanced daily news intelligence by scanning global sources, separating facts from opinions, and presenting diverse perspectives.

## Core Philosophy

**"Hear All the Bells"** - To understand what's really happening, read all articles from all countries, all journalists, all perspectives. Then separate Facts from Opinions so the user can make educated decisions.

## User Preferences (Sarah - Barcelona)

### Topics Priority:
1. **BIG WORLD NEWS** (High priority)
   - Politics, conflicts, major events
   - International relations
   - Government actions
   
2. **EUROPE FOCUS** (High priority)
   - Spain (Barcelona local + national)
   - Italy (home country)
   - EU-wide news
   - War concerns / NATO / defense
   - European politics

3. **ARTS & CULTURE** (High priority)
   - Theater/performing arts
   - Museums, exhibitions
   - Cultural events
   - Film, literature

4. **SCIENCE DISCOVERIES** (High priority)
   - Neuroscience, psychology
   - Human-Machine Interaction research
   - Major scientific breakthroughs
   - Medical advances

5. **TECH/BUSINESS** (Medium priority)
   - AI developments (especially HMI applications)
   - Major tech company news
   - Not too deep unless relevant to psychology/neurophysiology/HMI field

6. **SPORTS** (Low priority)
   - Only notable/interesting highlights
   - Major championships or unusual stories

### Geographic Focus:
- **Primary**: Spain (Barcelona/Catalonia), Italy, Europe
- **Secondary**: Global major events
- **Use sources**: El País, La Repubblica, Corriere della Sera, ANSA, European outlets

## How to Use This Skill

### When User Requests News

1. **Load the database**: Read `references/database.json` to see available sources

2. **Select balanced sources based on user preferences**:
   - **European priority sources** (3-4):
     - El País (Spain, Lean Left)
     - ANSA (Italy, Center)
     - Corriere della Sera or La Repubblica (Italy)
     - EFE (Spanish agency, Center)
   
   - **Global balance** (4-5):
     - Reuters (Center, UK)
     - AP (Left, USA)
     - AFP (Center, France)
     - BBC (Center, UK)
     - One right-leaning: WSJ or other
   
   - **Arts/Culture**: The Guardian, BBC Culture, arts sections
   - **Science**: Nature, Science journals via news outlets
   - **Tech**: TechCrunch, Wired, tech sections of major outlets

3. **Scan current news**: Use web_search to find today's major stories from selected sources

4. **Organize by topic priority**:
   - Europe News First (Spain, Italy, EU)
   - Major World News
   - Arts & Culture
   - Science & Tech
   - Quick Sports Highlights (if interesting)

5. **Separate Facts from Opinions**:
   - **FACTS**: Events that happened, verifiable data, confirmed by multiple sources
   - **OPINIONS**: Analysis, speculation, editorial interpretation, predictions

6. **Present as structured artifact**

## Output Format

### Daily News Digest Structure - Artifact Version

```markdown
# 📰 News Digest for Sarah - [Date]
*Barcelona Edition*

---

## 🇪🇸 SPAIN & BARCELONA

### [Local/National Story]

**WHAT HAPPENED:**
- [Facts]

**PERSPECTIVES:**
- [Different viewpoints if relevant]

---

## 🇮🇹 ITALY

### [Italian Story]

**WHAT HAPPENED:**
- [Facts]

**PERSPECTIVES:**
- [Different viewpoints if relevant]

---

## 🇪🇺 EUROPE

### [Major EU Story]

**WHAT HAPPENED:**
- [Facts]

**PERSPECTIVES:**
- [How different EU countries/sources view it]

---

## 🌍 MAJOR WORLD NEWS

### [Global Story 1]

**WHAT HAPPENED:**
- [Verifiable facts]

**PERSPECTIVES:**
- **Left-leaning ([Source])**: [Interpretation]
- **Center ([Source])**: [Interpretation]  
- **Right-leaning ([Source])**: [Interpretation]

---

## 🎭 ARTS & CULTURE

### [Cultural Story]

**WHAT HAPPENED:**
- [Facts about exhibitions, performances, cultural events]

---

## 🔬 SCIENCE & DISCOVERIES

### [Science Story]

**WHAT HAPPENED:**
- [New research, breakthroughs]

**WHY IT MATTERS:**
- [Implications, especially for psychology/neuroscience/HMI if relevant]

---

## 💻 TECH & BUSINESS

### [Tech Story]

**WHAT HAPPENED:**
- [Facts]

**RELEVANCE:** [Note if connected to HMI, psychology, AI applications]

---

## ⚽ QUICK SPORTS HIGHLIGHTS

- [Only if something genuinely interesting/unusual]

---

## 📊 SOURCES CONSULTED TODAY
- [Source 1] ([Political Lean], [Country])
- [Source 2] ([Political Lean], [Country])
...

---

## 💬 TL;DR - Quick Headlines

*[3-5 sentence ultra-quick summary of the day's most important news]*
```

## Source Selection Strategy for Sarah

### Required European Sources (Use 3-4):
**Spain:**
- El País (Lean Left, Spain) - National paper
- EFE (Center, Spain) - Wire service for Spanish/LatAm

**Italy:**
- ANSA (Center, Italy) - Wire service, high credibility
- Corriere della Sera (Center, Italy) - Moderate, balanced
- La Repubblica (Lean Left, Italy) - Progressive perspective
- il Fatto Quotidiano (Lean Left, Italy) - Investigative, anti-corruption

**European:**
- AFP (Center, France) - French perspective
- DPA (Center, Germany) - German perspective
- Euronews (various perspectives)

### Required Global Balance (Use 3-4):
- Reuters (Center, UK) - Wire service, least biased
- AP (Left, USA) - Breaking news
- BBC (Center/Mixed, UK) - International coverage
- WSJ (Lean Right, USA) - Business, right perspective

### Specialty Sources (Use as needed):
**Arts/Culture:**
- The Guardian (Lean Left, UK) - Strong culture coverage
- BBC Culture
- Internazionale (Lean Left, Italy) - International arts/culture

**Science:**
- Scientific outlets referenced in news
- BBC Science
- Major journals (Nature, Science) via news coverage

**Tech:**
- Tech sections of major outlets
- Wired, TechCrunch for major stories
- Focus on AI/HMI relevance

## Fact vs Opinion Methodology

### What Counts as FACT:
- Events that occurred (verified by multiple sources)
- Statements made by officials (with attribution)
- Published data and statistics
- Confirmed deaths, injuries, arrests
- Announced policy changes
- Verifiable actions taken
- Exhibition openings, performance dates
- Scientific paper publications
- Company announcements

### What Counts as OPINION:
- "This will lead to..." (prediction)
- "Experts say..." (unless specific named expert with credential)
- "Many believe..." (speculation)
- Editorial analysis
- Cause-and-effect claims without evidence
- Adjectives describing quality (good/bad/effective/failed)
- Interpretations of motivation
- Art criticism (subjective interpretation)

### Red Flags for Opinion Dressed as Fact:
- Emotionally loaded language
- Unattributed claims ("sources say")
- Future predictions
- Value judgments
- "Likely" or "probably" statements

## Cross-Referencing for Verification

When a claim appears in an article:

1. **Check if other sources report the same fact**
2. **Note if sources with different political leans agree** (strong verification)
3. **Flag when sources disagree on basic facts** (rare for legitimate news)
4. **Distinguish between disagreeing on facts vs disagreeing on interpretation**
5. **For European news**: Cross-check Spanish/Italian sources with international coverage

## Political Lean Handling

**CRITICAL**: Political lean ≠ unreliable

High credibility sources with clear political lean are VALUABLE for understanding different perspectives. The goal is:
- Present what HAPPENED (facts all agree on)
- Show how different perspectives INTERPRET what happened
- Note European vs American perspectives on same events

## Response Flow

### Initial Response (In Chat):
Provide a **TL;DR summary** (3-5 sentences covering the day's most critical news), then say:

"I've created your full digest as an artifact - click to read the detailed breakdown with all sources and perspectives!"

### In Artifact:
Full structured digest following the format above.

## Important Notes

- **Don't quote copyrighted content** - Summarize in your own words
- **Prioritize European sources** for European stories
- **Geographic diversity** prevents Western-centric bias
- **Political balance** shows full spectrum of perspectives
- **Fact verification** through cross-referencing is essential
- **Barcelona context**: Note local events, Catalan politics when relevant
- **Theater focus**: Pay attention to performing arts news given user's Teatro Metamorfosis work
- **War awareness**: Given European tensions, prioritize defense/NATO/security news

## Search Strategy

### Daily Search Pattern:
1. Start with European sources: "El País Spain news today [date]"
2. Italian sources: "ANSA Italy news today [date]" 
3. EU-wide: "European Union news today [date]"
4. Global: "Reuters major news today [date]"
5. Arts: "arts culture news today [date]" + Barcelona/Spain/Italy specific
6. Science: "science discoveries today [date]" + neuroscience/psychology
7. Tech: "tech news today [date]" + AI/HMI when relevant
8. Sports: Quick scan only if time permits

### Prioritize:
- Spain/Italy/Europe first
- Then major world events
- Then specialty topics (arts, science, tech)
- Sports last (brief only)

## Example Usage

**User**: "What's the news today?" OR "Give me today's digest"

**Process**:
1. Read database.json
2. Select 7-9 balanced sources (3-4 European, 3-4 global, 1-2 specialty)
3. Search for today's major news from each
4. Organize by geographic/topic priority (Europe first!)
5. For each story:
   - Extract verified facts
   - Note different interpretations
   - Flag relevance to user's interests (theater, psychology, HMI)
6. Create artifact with structured digest
7. Provide TL;DR in chat + link to artifact

**Output**: 
- Chat: Brief TL;DR (3-5 sentences)
- Artifact: Complete digest following personalized format above

## Special Attention Items

Given user's background and interests:

- **Teatro Metamorfosis**: Note performing arts news, theater industry, Barcelona cultural scene
- **Psychology/Neuroscience**: Highlight relevant research, HMI studies
- **ADHD-friendly**: Use clear headers, scannable format, bold key facts
- **Memory Palace techniques**: If cognitive science news, note relevance
- **Barcelona Fringe Festival**: Theater/arts festival news
- **Sailing**: Maritime news if genuinely significant
- **European politics**: Given potential war concerns, prioritize security news
- **Italian connections**: Family in Valencia (Spain), roots in Italy

## Database Location

The complete source database with all 95 sources and full metadata is located at:
`references/database.json`

This includes:
- Global news agencies
- European sources by country (Spain, Italy, France, Germany, UK, etc.)
- North America, Latin America, Asia-Pacific, Middle East, Africa
- Fact-checkers
- Specialty sources (arts, science, tech, finance, sports)
- Political lean ratings (L, LL, C, LR, R, SG, M)
- Credibility ratings (high, medium, mixed, low, propaganda)
- Complete metadata (URLs, founding dates, languages, specialties)
