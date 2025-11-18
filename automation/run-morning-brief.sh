#!/bin/bash
# Simple morning brief - run this when you wake up!

cd "$(dirname "$0")" || exit 1

echo "🌅 Good morning! Running your brief..."
echo ""

python3 simple_morning_brief.py

echo ""
echo "✅ Done! Claude will now check your email and present everything."
