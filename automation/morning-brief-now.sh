#!/bin/bash
# Manual Morning Brief Runner
# Run this anytime to generate a fresh morning brief immediately

echo "🌅 Running morning brief now..."
echo ""

# Navigate to the automation directory
cd "$(dirname "$0")" || exit 1

# Run the Python script
python3 morning_brief.py

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Morning brief completed!"
    echo "📍 Check GitHub for the latest brief"
    echo "📋 Log file: automation/logs/morning_brief.log"
else
    echo ""
    echo "⚠️  Morning brief failed!"
    echo "📋 Check log file for details: automation/logs/morning_brief.log"
    exit 1
fi
