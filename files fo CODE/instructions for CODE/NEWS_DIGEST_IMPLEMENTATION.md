# Claude Code: News Digest System Implementation

## YOUR TASK
Create the news intelligence system that generates daily news digests using the news-intelligence skill and Global Media Database.

## FILES YOU HAVE
1. **news-intelligence-SKILL.md** - The skill definition with all rules
2. **Global_Media_Database_v3.json** - The complete database (150+ sources)
3. **news-digest-2025-11-16.md** - Example output from today

## WHAT TO BUILD

### Output 1: Daily News Digest (Markdown File)

**Format:** `news-digest-YYYY-MM-DD.md`

**Structure** (from news-intelligence-SKILL.md lines 98-202):
```markdown
# 📰 News Digest for Sarah - [Date]
*Barcelona Edition*

---

## 🇪🇸 SPAIN & BARCELONA
### [Story Title]
**WHAT HAPPENED:**
- [Facts only]

**PERSPECTIVES:**
- [Different viewpoints if relevant]

---

## 🇮🇹 ITALY
### [Story Title]
**WHAT HAPPENED:**
- [Facts]

---

## 🇪🇺 EUROPE
### [Story Title]
**WHAT HAPPENED:**
- [Facts]

**PERSPECTIVES:**
- [How different sources view it]

---

## 🌍 MAJOR WORLD NEWS
### [Story Title]
**WHAT HAPPENED:**
- [Facts]

**PERSPECTIVES:**
- **Left-leaning ([Source])**: [Interpretation]
- **Center ([Source])**: [Interpretation]
- **Right-leaning ([Source])**: [Interpretation]

---

## 🎭 ARTS & CULTURE
### [Story Title]
**WHAT HAPPENED:**
- [Facts about exhibitions, performances, events]

---

## 🔬 SCIENCE & DISCOVERIES
### [Story Title]
**WHAT HAPPENED:**
- [New research, breakthroughs]

**WHY IT MATTERS:**
- [Implications for psychology/neuroscience/HMI if relevant]

---

## 💻 TECH & BUSINESS
### [Story Title]
**WHAT HAPPENED:**
- [Facts]

**RELEVANCE:** [Note if connected to HMI, psychology, AI]

---

## 📊 SOURCES CONSULTED TODAY
- [Source] ([Political Lean], [Country])
- [Source] ([Political Lean], [Country])

---

## 💬 TL;DR - Quick Headlines
*[3-5 sentence ultra-quick summary]*
```

### Output 2: Command to Generate News

Create a simple command that the user can run daily.

**Command format:**
```bash
python generate_news.py [--date YYYY-MM-DD]
```

If no date provided, use today's date.

---

## IMPLEMENTATION APPROACH

### Option A: Web Scraping Script (Recommended)

Create `generate_news.py` that:

1. **Reads the database** to select sources:
   - 3-4 European priority (El País, ANSA, Corriere, etc.)
   - 3-4 Global balance (Reuters, AP, BBC, etc.)
   - Specialty as needed (arts, science, tech)

2. **Searches for today's news** from selected sources:
   - Use requests + BeautifulSoup to scrape headlines
   - Or use RSS feeds if available
   - Or call a news API (NewsAPI, MediaStack, etc. - requires API key)

3. **Organizes by topic priority**:
   - Spain → Italy → Europe → World → Arts → Science → Tech

4. **Separates facts from opinions**:
   - Flag: predictions, "experts say", value judgments
   - Keep: events that occurred, statements made, published data

5. **Creates the markdown file** following the structure above

6. **Saves to**: `news-digest-YYYY-MM-DD.md`

### Option B: LLM-Assisted Script (Simpler but requires API)

Create `generate_news_llm.py` that:

1. Reads the skill instructions
2. Reads the database
3. Makes API calls to Claude API with instructions:
   ```
   Today is [date]. Using the news-intelligence skill and database,
   search the web for today's major news and create the daily digest
   following the exact format in the skill.
   
   Priority: Spain → Italy → Europe → World → Arts → Science → Tech
   Balance: Use sources with different political leans
   Separate: Facts vs Opinions clearly
   ```
4. Saves the output

---

## CORE RULES FROM SKILL (CRITICAL!)

### Source Selection (from lines 206-242):
**European Priority (Use 3-4):**
- El País (Lean Left, Spain)
- ANSA (Center, Italy)
- Corriere della Sera (Center, Italy) OR La Repubblica (Lean Left, Italy)
- EFE (Center, Spain)

**Global Balance (Use 3-4):**
- Reuters (Center, UK)
- AP (Left, USA)
- BBC (Center, UK)
- WSJ (Lean Right, USA) - for business/right perspective

**Specialty (as needed):**
- Arts: Guardian, BBC Culture
- Science: Nature, Science journals via news
- Tech: TechCrunch, Wired

### Fact vs Opinion (lines 244-272):
**FACTS:**
- Events that occurred (verified by multiple sources)
- Statements made by officials (with attribution)
- Published data and statistics
- Confirmed deaths, injuries, arrests
- Exhibition openings, performance dates
- Scientific paper publications

**OPINIONS:**
- "This will lead to..." (prediction)
- "Experts say..." (unless specific named expert)
- "Many believe..." (speculation)
- Editorial analysis
- Cause-and-effect claims without evidence
- Value judgments (good/bad/effective/failed)

### Search Strategy (lines 314-330):
1. Start European: "El País Spain news today [date]"
2. Italian: "ANSA Italy news today [date]"
3. EU-wide: "European Union news today [date]"
4. Global: "Reuters major news today [date]"
5. Arts: "arts culture news today [date]" + Barcelona/Spain/Italy
6. Science: "science discoveries today [date]" + neuroscience/psychology
7. Tech: "tech news today [date]" + AI/HMI
8. Sports: Brief only if interesting

### User Preferences (lines 14-53):
**Topic Priority:**
1. BIG WORLD NEWS (High)
2. EUROPE FOCUS - Spain, Italy, EU (High)
3. ARTS & CULTURE - Theater, museums, cultural events (High)
4. SCIENCE - Neuroscience, psychology, HMI (High)
5. TECH/BUSINESS - AI developments, HMI applications (Medium)
6. SPORTS - Only notable highlights (Low)

**Geographic Focus:**
- Primary: Spain (Barcelona/Catalonia), Italy, Europe
- Secondary: Global major events

**Special Attention:**
- Teatro Metamorfosis theater news
- Psychology/Neuroscience/HMI research
- ADHD-friendly format (clear headers, scannable, bold facts)
- European politics (war concerns, NATO, defense)

---

## DELIVERABLES

1. **generate_news.py** - Main script to generate daily digest
2. **README.md** - Instructions on how to use it
3. **requirements.txt** - Python dependencies
4. **config.json** (optional) - User preferences, API keys if needed

---

## EXAMPLE USAGE

```bash
# Generate today's news
python generate_news.py

# Generate for specific date
python generate_news.py --date 2025-11-16

# Output saved to: news-digest-2025-11-16.md
```

---

## VALIDATION CHECKLIST

Your implementation should:
- ✅ Read the Global Media Database
- ✅ Select balanced sources (European priority + global balance)
- ✅ Organize by geographic/topic priority (Spain → Italy → Europe → World → Arts → Science → Tech)
- ✅ Separate facts from opinions clearly
- ✅ Include "WHAT HAPPENED" and "PERSPECTIVES" sections
- ✅ List sources consulted with political lean
- ✅ Provide TL;DR at top or bottom
- ✅ Use ADHD-friendly format (clear headers, scannable, bold key facts)
- ✅ Note relevance to user's interests (theater, HMI, neuroscience)
- ✅ Save as markdown file with date

---

## NOTES

**About Web Scraping:**
- Some sites block scrapers (use headers, User-Agent)
- RSS feeds are easier (check database for RSS URLs)
- NewsAPI or similar services are simplest but may require paid API key

**About Copyright:**
- Never reproduce articles verbatim
- Summarize in your own words
- Maximum one short quote (<15 words) per article
- Follow skill guidelines (lines 303-312)

**About Fact-Checking:**
- Cross-reference claims across sources with different political leans
- If sources disagree on basic facts, note it (rare for legitimate news)
- European sources for European news, international for global

---

## START HERE

1. Decide: Web scraping or LLM-assisted approach?
2. Create the main script
3. Test with today's date
4. Validate output matches the format from news-digest-2025-11-16.md
5. Add error handling and logging
6. Create README with usage instructions

Good luck! 🚀
