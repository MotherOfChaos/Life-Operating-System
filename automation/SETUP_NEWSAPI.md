# NewsAPI Setup Guide

## What This Does

Fetches REAL news articles from verified sources using NewsAPI, then Claude analyzes and formats them into your ADHD-friendly digest.

**Comparison with Skill:**
- **NewsAPI approach**: Pre-fetched real articles, analyzed by Claude API
- **Skill in Projects**: Real-time web search, full Claude capabilities
- **Result**: Both give real news, try both and see which you prefer!

## Step 1: Get NewsAPI Key (FREE)

1. Go to: https://newsapi.org/register
2. Sign up (free tier: 100 requests/day - plenty for daily digest!)
3. Copy your API key

## Step 2: Add to GitHub Secrets

1. Go to: https://github.com/MotherOfChaos/Life-Operating-System/settings/secrets/actions
2. Click "New repository secret"
3. Name: `NEWSAPI_KEY`
4. Value: [paste your API key]
5. Click "Add secret"

## Step 3: Update Workflow

The workflow is already set up to use this! It will automatically use NewsAPI if the key is available.

## Step 4: Test It

Trigger manually:
```bash
curl -X POST \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/MotherOfChaos/Life-Operating-System/actions/workflows/news-digest.yml/dispatches \
  -d '{"ref":"main"}'
```

Check the generated digest in `news-digests/` folder.

## Sources Included

- BBC News
- Reuters
- Associated Press  
- The Guardian
- ANSA (Italy)
- Topic searches for: psychology, neuroscience, theater, Barcelona, Spain, Italy

## Free Tier Limits

- 100 requests/day
- Our automation uses ~7-10 requests per run
- Can run 10+ times daily if needed
- Perfect for one morning digest!

## If It Fails

The automation will fall back to a message telling you to use the skill in Projects directly.
