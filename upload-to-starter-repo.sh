#!/bin/bash
# Script to upload XAVIER package to ADHD-Life-OS-Starter repo

echo "🚀 Uploading ADHD Life OS Starter package to GitHub..."
echo ""

# Create temp directory
cd /tmp
rm -rf adhd-starter-upload
mkdir adhd-starter-upload
cd adhd-starter-upload

# Clone the new empty repo
echo "📥 Cloning your new repo..."
git clone https://github.com/MotherOfChaos/ADHD-Life-OS-Starter.git
cd ADHD-Life-OS-Starter

# Copy XAVIER contents
echo "📦 Copying XAVIER package files..."
cp -r /home/user/Life-Operating-System/XAVIER/* .

# Add and commit
echo "💾 Committing files..."
git add .
git commit -m "Initial commit - ADHD-friendly Life OS automation system

Complete automation package including:
- Morning brief automation (8:30 AM)
- Multi-account email triage
- AI news digest generator
- Calendar integration with smart filtering
- TODO tracking
- Mobile/web access solutions

ADHD-friendly design - saves ~35K tokens daily!
"

# Push
echo "⬆️  Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Your repo is live at:"
echo "https://github.com/MotherOfChaos/ADHD-Life-OS-Starter"
echo ""
echo "Share this link with Xavier!"
