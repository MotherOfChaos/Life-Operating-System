# Instructions for Claude Code: Rebuild Global Media Database

## YOUR TASK
Rebuild the comprehensive Global Media Database with 150+ sources from documented research sessions. The current database has only 77 sources but research sessions 3-5 documented 150-180+ sources that need to be integrated.

## FILES YOU HAVE
1. **Global_Media_Database.json** (current 77-source version) - Use as base structure
2. **RESEARCH_DOCUMENTATION.md** - All documented sources from research sessions
3. **database-structure-template.json** - Clean template to follow

## WHAT TO BUILD

### Target: 150+ sources across these categories:

**Global News Agencies** (10): AP, Reuters, AFP, ANSA, DPA, EFE, Xinhua, TASS, PTI, Kyodo

**Europe** (30+):
- **Italy** (7): Corriere della Sera, La Repubblica, Il Fatto Quotidiano, Internazionale, ANSA, Il Sole 24 Ore, La Stampa
- **Spain** (7): El País, El Mundo, elDiario.es, CTXT, ABC, La Vanguardia, El Confidencial
- **France** (6): Le Monde, Le Figaro, Libération, Mediapart, L'Obs, Le Parisien
- **Germany** (6): Der Spiegel, Die Zeit, FAZ, Süddeutsche Zeitung, taz, CORRECTIV
- **UK** (6): BBC, Guardian, Telegraph, Times, Financial Times, Independent

**North America** (8):
- USA: NYT, Washington Post, WSJ, NPR, ProPublica, The Atlantic
- Canada: CBC, Globe and Mail

**Latin America** (16): ALiados fact-checking network + major outlets from Mexico, Brazil, Argentina, Colombia, Chile, Venezuela, Peru

**Asia-Pacific** (12):
- Japan: Asahi Shimbun, Kyodo News, NHK
- India: The Hindu, Indian Express, PTI
- Australia: ABC, The Age, Sydney Morning Herald
- Indonesia, Philippines, Singapore outlets

**Middle East** (6): Haaretz, Times of Israel, Al Jazeera, Middle East Eye, +2 more

**Africa** (4): Daily Maverick (South Africa), Premium Times (Nigeria), +2 more

**Specialty Sources** (40+):

**Arts & Culture** (18):
- Visual Arts: Artforum, Frieze, Apollo, ArtNews, Hyperallergic
- Music: Pitchfork, Rolling Stone, NME
- Film: Variety, Hollywood Reporter, Cahiers du Cinéma
- Theater: American Theatre, The Stage
- Literature: Paris Review, London Review of Books
- Architecture: Dezeen, ArchDaily

**Science/Health** (8): Nature, Science, Lancet, NEJM, JAMA, Scientific American, Science News, New Scientist

**Technology** (5): Ars Technica, TechCrunch, Wired, The Verge, MIT Technology Review

**Finance/Business** (4): Bloomberg, The Economist, Financial Times, Barron's

**Sports** (3): ESPN, The Athletic, BBC Sport

**Investigative Networks** (3): ICIJ, OCCRP, GIJN

**Independent Journalists/Substacks** (10): 
- Heather Cox Richardson (history/politics)
- Matt Taibbi (investigative)
- Bari Weiss (culture/politics)
- Glenn Greenwald (civil liberties)
- Seymour Hersh (investigative)
- 404 Media (tech collective)
- Defector (sports/culture)
- +3 more quality independents

## JSON STRUCTURE TO FOLLOW

```json
{
  "database_info": {
    "name": "Global Media Database",
    "version": "3.0",
    "created": "2025-11-08",
    "updated": "2025-11-16",
    "purpose": "Comprehensive global news sources for Claude news-intelligence skill",
    "total_sources": "150+",
    "creator": "Mother Of Chaos",
    "status": "Complete - Ready for Claude Skill"
  },
  
  "political_lean_legend": {
    "L": "Left",
    "LL": "Lean Left / Left-Center",
    "C": "Center / Least Biased",
    "LR": "Lean Right / Right-Center",
    "R": "Right",
    "SG": "State-Guided / Government Controlled",
    "M": "Mixed (varies by section/program)",
    "N/A": "Not applicable (specialty/arts content)"
  },
  
  "credibility_ratings": {
    "high": "Rigorous fact-checking, transparent corrections, strong editorial standards",
    "medium": "Generally reliable but occasional lapses",
    "mixed": "Quality varies significantly",
    "low": "Frequent inaccuracies",
    "propaganda": "State-controlled narrative"
  },
  
  "legitimacy_criteria": {
    "tier_1": "Automatic inclusion - Established outlets 50+ years, major awards, paper of record status, IFCN certification",
    "tier_2": "Credentialed individuals - Professional journalism background, verified credentials",
    "tier_3": "Emerging quality - Transparent practices, documented fact-checking"
  },
  
  "usage_notes": {
    "for_claude_skill": "Cross-reference articles from different political leans and regions. Prioritize high credibility. Use geographic diversity.",
    "fact_checking_method": "1) Identify claims 2) Search across political spectrum 3) Check consistency 4) Flag opinion vs fact 5) Note disagreements",
    "bias_handling": "Political lean ≠ unreliable. High credibility sources with clear lean are valuable for perspectives."
  },
  
  "global_news_agencies": [
    {
      "name": "Associated Press (AP)",
      "url": "https://apnews.com",
      "founded": 1846,
      "type": "wire_service",
      "political_lean": "L",
      "credibility": "high",
      "countries": "global",
      "languages": ["English", "Spanish"],
      "specialty": "Breaking news, politics",
      "notes": "Moved from Lean Left to Left in Nov 2024. Co-operative, non-profit.",
      "tier": 1
    }
    // ... continue with all sources
  ],
  
  "italy": [
    // Italian sources
  ],
  
  "spain": [
    // Spanish sources
  ]
  
  // ... etc for all categories
}
```

## EACH SOURCE NEEDS:
- `name` (string)
- `url` (string)
- `founded` (year, optional)
- `type` (wire_service, newspaper, broadcaster, magazine, online_native, investigative_network, independent_journalist, etc.)
- `political_lean` (L, LL, C, LR, R, SG, M, N/A)
- `credibility` (high, medium, mixed, low, propaganda)
- `countries` (string - "global" or specific countries)
- `languages` (array)
- `specialty` (string - main focus areas)
- `notes` (string - important context)
- `tier` (1, 2, or 3)

## VALIDATION RULES
1. All JSON must be valid (no trailing commas, proper escaping)
2. Every source must have all required fields
3. Political lean must use only defined values
4. Credibility must use only defined values
5. URLs must include https://
6. Total sources should be 150-180

## OUTPUT
Save as: `Global_Media_Database_v3.json`

Validate it works by loading as JSON and counting sources by category.

## APPROACH
1. Start with the current 77-source database as base
2. Systematically add sources category by category
3. Use the research documentation for source details
4. Validate JSON after each major addition
5. Final validation: count total sources, ensure 150+

## PRIORITY ORDER
1. Complete Europe sources (highest priority for user in Barcelona)
2. Add arts/culture sources (user's interest area)
3. Add remaining global regions
4. Add specialty sources (science, tech, etc.)
5. Add independent journalists

Go build it! 🚀
