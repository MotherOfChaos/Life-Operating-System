# Personal Finances Analysis Project

**Created:** 2025-11-08  
**Status:** Ready for Code Analysis  
**Owner:** Sarah Poer (Mother Of Chaos)

---

## 📋 Project Overview

This project contains a comprehensive personal expense tracking system designed for bank statement analysis, budgeting, and financial projections. The system is ADHD-friendly with clear structure, visual outputs, and actionable insights.

### Goals
1. Extract expense data from bank statements (2020-present)
2. Calculate monthly averages for variable costs
3. Identify spending patterns and trends
4. Support budgeting and financial projections
5. Find optimization opportunities

---

## 🏠 Properties Tracked

### Personal Properties (3)
1. **Can Booty** (Santa Coloma/Badalona) - Primary residence
   - Owned by GARRDEN OF JOY S.L. (Sarah is Admin)
   - Special calculation needed for housing costs
2. **Malnom** - Barcelona centre flat (owned by Sarah)
3. **Barraca 182** - Valencia (Sarah owns, father lives there)

### Business Property (EXCLUDED)
- **Teatro Metamorfosis** (Tapioles 12, Barcelona)
  - Business expenses only (LAS TIAS DEL SEC, S.L.)
  - NOT included in personal analysis

---

## 💳 Bank Accounts

### Analyze
- ✅ **Cajamar** - Personal account
- ✅ **Caixabank** - Personal account

### Exclude  
- ❌ **Revolut** - Not needed
- ❌ **Santander** - Work accounts only

---

## 📊 Expense Categories (37 items total)

| Category | Count | Details |
|----------|-------|---------|
| Utilities | 9 | 3 properties × 3 utilities (water, gas, electricity) - Bimonthly |
| Subscriptions | 4 | Amazon Prime, Netflix, Patreon, Anthropic Claude - Monthly |
| Insurance | 6 | 3 property + 2 vehicle + 1 health (SANITAS) |
| Property Tax | 2 | IBI for Valencia & Malnom - Annual |
| Social Security | 2 | TGSS regular + recargos |
| Accountant | 2 | Oriol (current) + Elena (previous) |
| Bank Fees | 2 | Cajamar + Caixabank |
| Payment Plans | 2 | Multas Rafa (€84/mo × 36 months) + Fergie |
| Pharmacy | 2 | Meu (cat) medicines + Sarah's prescriptions |
| Variable Costs | 5 | Mechanic, appliances, Bryan, motorbike, fines |
| Security | 1 | Securitas Direct alarm |

---

## 📁 File Structure

### PRIMARY FILES FOR CODE

1. **sarah_expenses_structured_table.csv**
   - Main input file with all 37 expense items
   - Includes search keywords, payment frequency, property locations
   - Structured for automated extraction

2. **CODE_INSTRUCTIONS_bank_analysis.md**
   - Comprehensive analysis instructions
   - Output format specifications
   - ADHD-friendly requirements

3. **sarah_finances_chat_context.json**
   - Complete project context
   - Property details, bank account info
   - Known amounts and pending decisions

### SUPPORTING FILES

4. **expense_table_visual.md**
   - Human-readable table with explanations
   - Column definitions
   - Instructions for Code

5. **sarah_expense_inputs_raw.md**
   - Chronological list of all inputs
   - Raw conversation data
   - Reference for context

### REFERENCE FILES

6. **expense_template_current.md**
   - Original template (superseded by structured table)

7. **sarah_expenses_tracker.csv**
   - Original simple CSV (superseded by structured table)

---

## 🎯 Known Values

### Confirmed Amounts
- **Multas Rafa:** €84/month for 36 months
  - Monthly: €84
  - Annual: €1,008
  - Total remaining: €3,024

---

## 🔍 Code Analysis Requirements

### Phase 1: Data Extraction
- Map bank transactions to expense template
- Use search keywords for pattern matching
- Handle Spanish/Catalan/English descriptions

### Phase 2: Pattern Analysis
- Calculate monthly averages for variable expenses
- Identify trends (increasing/decreasing/stable)
- Note seasonal patterns
- Flag anomalies

### Phase 3: Outputs

Code should generate:

1. **sarah_expenses_tracker_FILLED.csv**
   - Template with actual amounts
   - Confidence levels noted

2. **sarah_financial_analysis.md**
   - Executive summary
   - Visual charts/graphs
   - Category breakdowns
   - Trend analysis

3. **sarah_budget_data.json**
   - Structured data for budgeting
   - Monthly/annual totals
   - By category details
   - Red flags and unmatched transactions

4. **sarah_financial_action_items.md**
   - Data to verify
   - Missing information
   - Optimization opportunities
   - Budget recommendations

---

## 🧠 ADHD-Friendly Approach

### Output Requirements
- ✅ Executive summary first (TL;DR)
- ✅ Visual > Text (charts, graphs, color coding)
- ✅ Actionable items clearly listed
- ✅ Celebrate wins (consistent payments, etc.)
- ✅ NO shame about past decisions
- ✅ Focus on systems and patterns

### Data Quality
- Always indicate confidence levels
- Note data gaps
- Spanish format awareness (€1.234,56)
- Handle incomplete data gracefully

---

## ⚠️ Edge Cases

1. **Can Booty housing:** Don't calculate - separate system needed
2. **Teatro expenses:** Exclude - business account
3. **Transfers between accounts:** Don't count as expenses
4. **Refunds:** Net against original expense category
5. **Large one-time purchases:** Flag separately, don't skew averages

---

## 🚀 Next Steps

1. Code accesses GitHub repo with bank statements
2. Code runs analysis per instructions
3. Code generates all 4 output files
4. Review and validate extracted data
5. Create final budget plan

---

## 📞 Contact

**Sarah Poer**  
- Founder & Artistic Director, Teatro Metamorfosis
- Company: LAS TIAS DEL SEC, S.L.
- Location: Barcelona, Spain

---

## 📝 Notes

- Data source: GitHub repo with bank extracts since 2020
- Last updated: 2025-11-08
- Version: v1.0
- Chat ID: finances_channel_v1

---

**Status: Ready for Code Analysis** ✅
