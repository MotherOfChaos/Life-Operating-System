#!/bin/bash
# 🧪 TEST MORNING BRIEF AUTOMATION NOW
# Run this anytime to test the automation without waiting for scheduled time

set -e  # Exit on error

echo "════════════════════════════════════════════════════════════"
echo "🧪 TESTING MORNING BRIEF AUTOMATION"
echo "════════════════════════════════════════════════════════════"
echo ""

# Get current time in Madrid timezone
echo "📅 Current time (Europe/Madrid):"
TZ='Europe/Madrid' date '+%A, %B %d, %Y - %H:%M %Z'
echo ""

# Check we're in the right directory
if [ ! -f "automation/news_digest_generator.py" ]; then
    echo "❌ ERROR: Please run this from Life-Operating-System root directory"
    echo "   cd ~/Life-Operating-System"
    echo "   ./automation/test-now.sh"
    exit 1
fi

# Check for API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  WARNING: ANTHROPIC_API_KEY not set"
    echo "   News digest will fail without it"
    echo "   Set it with: export ANTHROPIC_API_KEY='your-key-here'"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Step 1: Generate news digest
echo "════════════════════════════════════════════════════════════"
echo "📰 STEP 1: Generating News Digest"
echo "════════════════════════════════════════════════════════════"
echo ""

cd automation
python3 news_digest_generator.py
cd ..

echo ""
echo "✅ News digest complete!"
echo ""

# Step 2: Generate morning brief
echo "════════════════════════════════════════════════════════════"
echo "🌅 STEP 2: Generating Morning Brief"
echo "════════════════════════════════════════════════════════════"
echo ""

cd automation
python3 github_actions_morning_brief.py
cd ..

echo ""
echo "✅ Morning brief complete!"
echo ""

# Show what was created
echo "════════════════════════════════════════════════════════════"
echo "📂 FILES CREATED:"
echo "════════════════════════════════════════════════════════════"

# Find today's files
TODAY=$(TZ='Europe/Madrid' date '+%Y-%m-%d')

if [ -f "news-digests/news-digest-${TODAY}.md" ]; then
    echo "✓ news-digests/news-digest-${TODAY}.md"
else
    echo "⚠️  news-digests/news-digest-${TODAY}.md NOT FOUND"
fi

if [ -f "morning-briefs/MORNING_BRIEF_${TODAY}.md" ]; then
    echo "✓ morning-briefs/MORNING_BRIEF_${TODAY}.md"
else
    echo "⚠️  morning-briefs/MORNING_BRIEF_${TODAY}.md NOT FOUND"
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo "✅ TEST COMPLETE!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "1. Check the files above to see if they look correct"
echo "2. If they look good, commit and push:"
echo "   git add morning-briefs/ news-digests/ automation/"
echo "   git commit -m 'Fix news digest API and timezone handling'"
echo "   git push"
echo ""
