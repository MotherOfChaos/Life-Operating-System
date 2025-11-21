#!/bin/bash
# Check emails on-demand (local run)
# Usage: ./automation/check-emails-now.sh

echo "=================================="
echo "📧 CHECKING ALL EMAIL ACCOUNTS"
echo "=================================="
echo ""

# Navigate to automation directory
cd "$(dirname "$0")"

# Run email automation
python email_automation.py

echo ""
echo "=================================="
echo "✅ EMAIL CHECK COMPLETE"
echo "=================================="
echo ""
echo "Results saved to: email_triage_results.json"
echo ""
echo "To extract artist/provider info from work emails, run:"
echo "  python artist_database_extractor.py"
echo ""
