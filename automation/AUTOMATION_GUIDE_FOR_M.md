# Automation Guide for M

## Quick Reference

### News Digest
**Trigger**: `curl -X POST -H "Authorization: token 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" https://api.github.com/repos/MotherOfChaos/Life-Operating-System/actions/workflows/news-digest.yml/dispatches -d '{"ref":"main"}'`

**Output**: `news-digests/YYYY-MM-DD_news_digest.md`

**When**: Auto at 08:30 AM CET daily + on-demand

### Email Check  
**Trigger**: `curl -X POST -H "Authorization: token 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" https://api.github.com/repos/MotherOfChaos/Life-Operating-System/actions/workflows/email-check.yml/dispatches -d '{"ref":"main"}'`

**Output**: `email-digest/YYYY-MM-DD-HH-MM.json`

**When**: On-demand only

### Calendar
**Trigger**: `curl -X POST -H "Authorization: token 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" https://api.github.com/repos/MotherOfChaos/Life-Operating-System/actions/workflows/calendar-action.yml/dispatches -d '{"ref":"main","inputs":{"action":"list"}}'`

**When**: On-demand only

## Implementation Status

✅ News Digest - READY (needs API key verification)
🟡 Email Check - PARTIAL (workflow ready, needs Gmail API setup)
🟡 Calendar - PARTIAL (workflow ready, needs Calendar API setup)

## Next Steps

1. Verify ANTHROPIC_API_KEY in GitHub secrets
2. Add Gmail API credentials
3. Add Calendar API credentials
4. Test each automation

Last updated: January 7, 2026
