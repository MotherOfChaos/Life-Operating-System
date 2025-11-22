# Bank Statement Analysis Instructions for Code

## PROJECT CONTEXT

**User:** Sarah Poer (Mother Of Chaos)  
**Goal:** Analyze personal bank statements to extract expense data, identify patterns, and support budgeting/financial planning  
**ADHD-Friendly:** Clear structure, visual outputs, actionable insights  

---

## DATA SOURCES

### GitHub Repository
- **Location:** [User will provide repo URL]
- **Content:** Bank extracts since 2020
- **Accounts to Analyze:**
  - ✅ **Cajamar** - Personal account
  - ✅ **Caixabank** - Personal account
  - ❌ **Revolut** - EXCLUDE (not needed)
  - ❌ **Santander** - EXCLUDE (work accounts only)

### File Formats Expected
- CSV, Excel, PDF statements
- Multiple date ranges
- Spanish bank statement format (likely)

---

## PHASE 1: DATA EXTRACTION & MAPPING

### Primary Objective
Extract amounts for known recurring expenses and map them to the expense template.

### Expense Template Categories

Use the file `sarah_expenses_tracker.csv` as your template structure. Key categories:

1. **Housing & Property**
   - IBI property taxes (annual)
   - Securitas Direct alarm (monthly)
   
2. **Insurance**
   - Property insurance (Valencia, Malnom, Can Booty)
   - Vehicle insurance (motorcycle, van)
   - SANITAS health insurance (monthly)

3. **Utilities** (3 properties × 3 utilities)
   - Water (bimonthly)
   - Gas (bimonthly)
   - Electricity (bimonthly)
   - Properties: Can Booty, Malnom, Valencia (Barraca 182)

4. **Tax & Accounting**
   - Seguridad Social (monthly + recargos)
   - Asesoria/accountant fees (Oriol current, Elena previous)

5. **Medical**
   - Meu (cat) medicines (monthly)
   - Sarah's prescriptions (monthly)

6. **Subscriptions**
   - Amazon Prime
   - Netflix
   - Patreon
   - Anthropic Claude Pro

7. **Bank Fees**
   - Caixabank fees
   - Cajamar fees

8. **Payment Plans**
   - Multas Rafa: €84/month (KNOWN - verify in statements)
   - Fergie payment plan

9. **Variable Costs** (need averages)
   - Mechanic/car repairs
   - House appliances
   - Bryan expenses
   - Motorbike maintenance
   - Traffic fines

### Extraction Strategy

For each expense category:

1. **Identify transaction patterns**
   - Recurring merchant names
   - Similar amounts at regular intervals
   - Keywords in descriptions (Spanish/Catalan)

2. **Match to template**
   - Map identified transactions to expense categories
   - Calculate monthly/annual amounts
   - Note frequency patterns

3. **Flag unknowns**
   - Transactions that don't match template
   - Potential new recurring expenses
   - Irregular large amounts

### Keywords to Search (Spanish/Catalan)

**Utilities:**
- agua, water, aigües
- gas, gas natural
- luz, electricidad, endesa, iberdrola, naturgy

**Insurance:**
- seguro, assegurança
- sanitas
- mutua, mapfre, axa

**Tax:**
- seguridad social, SS
- hacienda, AEAT
- IBI, impuesto

**Subscriptions:**
- amazon, prime
- netflix
- patreon
- anthropic, claude

**Services:**
- securitas
- asesor, gestor, contable

**Fines/Legal:**
- multa, sanción
- ayuntamiento, trànsit

---

## PHASE 2: PATTERN ANALYSIS

### Time-Series Analysis

For each expense category, calculate:

1. **Frequency**
   - Monthly, bimonthly, quarterly, annual
   - Regularity (consistent or variable)

2. **Amount Trends**
   - Average amount
   - Min/max range
   - Trend over time (increasing/decreasing)
   - Seasonal patterns

3. **Anomalies**
   - Unusually high/low amounts
   - Missing expected payments
   - Duplicate charges

### Variable Expense Averaging

For irregular categories (mechanic, fines, etc.):
- Calculate monthly average over last 12 months
- Calculate monthly average over last 24 months
- Note seasonal spikes
- Identify trend direction

### Category Totals

Calculate for rolling periods:
- Last 30 days
- Last 90 days
- Last 12 months
- Year-over-year comparison

---

## PHASE 3: OUTPUT REQUIREMENTS

### Output 1: Updated Expense Template (CSV)

**File:** `sarah_expenses_tracker_FILLED.csv`

**Format:** Same structure as input template, with:
- Amount_EUR: Filled with actual amounts (monthly equivalent)
- Annual_Cost: Calculated annual total
- Notes: Add details (e.g., "Average of last 12 months: €X, Range: €Y-€Z")

**Special handling:**
- For variable expenses: Use 12-month average
- For bimonthly: Show bimonthly amount, calculate annual
- For annual: Show annual amount
- Add confidence level in Notes: "HIGH" (consistent), "MEDIUM" (some variation), "LOW" (highly variable)

### Output 2: Visual Dashboard (Markdown + Charts)

**File:** `sarah_financial_analysis.md`

Include:

1. **Executive Summary**
   - Total monthly recurring expenses
   - Total annual expenses
   - Top 5 expense categories by amount
   - Key insights (2-3 bullet points)

2. **Category Breakdown**
   - Pie chart: Expenses by category
   - Bar chart: Monthly costs by category
   - Table: Category totals with % of total

3. **Time-Series Visualizations**
   - Line chart: Total monthly expenses over time
   - Line chart: Variable expenses trend
   - Heatmap: Expenses by month and category

4. **Trend Analysis**
   - Categories increasing over time
   - Categories decreasing over time
   - Seasonal patterns identified

5. **Anomaly Report**
   - Unusual transactions
   - Missing expected payments
   - Duplicate charges
   - Large one-time expenses

### Output 3: Budget Planning File (JSON)

**File:** `sarah_budget_data.json`

Structure:
```json
{
  "analysis_date": "YYYY-MM-DD",
  "data_period": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "monthly_totals": {
    "fixed_expenses": 0,
    "variable_expenses_avg": 0,
    "total_monthly": 0
  },
  "annual_totals": {
    "total_annual": 0
  },
  "by_category": {
    "category_name": {
      "monthly_amount": 0,
      "annual_amount": 0,
      "confidence": "HIGH/MEDIUM/LOW",
      "trend": "increasing/stable/decreasing",
      "notes": ""
    }
  },
  "variable_expenses_detail": {
    "expense_name": {
      "12_month_avg": 0,
      "24_month_avg": 0,
      "min": 0,
      "max": 0,
      "trend": "",
      "seasonal_notes": ""
    }
  },
  "unmatched_recurring": [
    {
      "description": "",
      "amount": 0,
      "frequency": "",
      "suggested_category": ""
    }
  ],
  "red_flags": [
    {
      "type": "anomaly/duplicate/missing",
      "description": "",
      "amount": 0,
      "date": ""
    }
  ]
}
```

### Output 4: Action Items (Markdown)

**File:** `sarah_financial_action_items.md`

Sections:

1. **Data to Verify**
   - Expenses found in statements that seem high/unusual
   - Possible duplicates
   - Transactions needing clarification

2. **Missing Information**
   - Template items not found in statements
   - Possible cash expenses not tracked
   - Expenses that might be in excluded accounts (Revolut/Santander)

3. **Optimization Opportunities**
   - Categories with high variability (potential to reduce)
   - Duplicate subscriptions
   - Expensive recurring charges (alternatives?)
   - Bank fees that might be avoidable

4. **Budget Recommendations**
   - Suggested monthly budget per category
   - Emergency fund target (3-6 months expenses)
   - Priority areas to address

---

## SPECIAL INSTRUCTIONS

### ADHD-Friendly Outputs

- ✅ Visual > Text (charts, graphs, color coding)
- ✅ Executive summary first (TL;DR)
- ✅ Actionable items clearly listed
- ✅ Celebrate wins (e.g., "You consistently pay Multas Rafa on time!")
- ✅ No judgment language about spending
- ✅ Focus on systems and patterns, not individual transactions

### Data Quality Notes

- **Date ranges:** Use most recent complete 12-24 months
- **Currency:** All amounts in EUR
- **Incomplete data:** Note in output if data gaps exist
- **Confidence levels:** Always indicate data quality
- **Spanish formats:** Watch for decimal/thousand separators (€1.234,56 format)

### Edge Cases to Handle

1. **Can Booty housing:** Don't try to extract - it's owned by GARRDEN OF JOY S.L. (separate calculation needed)
2. **Teatro expenses:** Exclude - paid from business account
3. **Transfers between accounts:** Don't count as expenses
4. **Refunds:** Net against original expense category
5. **Large one-time purchases:** Flag separately, don't skew averages

---

## DELIVERABLES CHECKLIST

- [ ] `sarah_expenses_tracker_FILLED.csv` - Template with actual amounts
- [ ] `sarah_financial_analysis.md` - Visual dashboard & analysis
- [ ] `sarah_budget_data.json` - Structured data for budget planning
- [ ] `sarah_financial_action_items.md` - Prioritized action list
- [ ] All files in `/mnt/user-data/outputs/`

---

## QUESTIONS TO ASK SARAH IF NEEDED

1. Repo URL and access method?
2. Preferred date range for analysis?
3. Are there specific merchants/transactions to exclude?
4. Any known expense categories we're missing?
5. Budget targets or goals to compare against?

---

## SUCCESS CRITERIA

✅ All template items with amounts OR marked "Not found in statements"  
✅ Variable expenses have 12-month averages  
✅ Clear visual summary of spending patterns  
✅ Actionable optimization opportunities identified  
✅ Budget-ready data output (JSON)  
✅ ADHD-friendly presentation (visual, concise, actionable)  

---

**Remember:** This is about understanding patterns to make better decisions, not judging past choices. Focus on empowering Sarah with clear data and practical next steps.
