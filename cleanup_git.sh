#!/bin/bash

echo "=== RENSAR GIT REPO ==="

# Skapa/uppdatera .gitignore
cat > .gitignore << 'GITIGNORE'
__pycache__/
*.pyc
*.db
.DS_Store
.vscode/
.env
mynewapp.db
GITIGNORE

echo "1. .gitignore skapad/uppdaterad"

# Ta bort trackade men oönskade filer
git rm --cached .DS_Store 2>/dev/null || true
git rm --cached mynewapp.db 2>/dev/null || true
git rm --cached -r __pycache__/ 2>/dev/null || true

echo "2. Oönskade filer borttagna från tracking"

# Lägg till .gitignore
git add .gitignore

# Commit
git commit -m "Rensar repo och lägger till .gitignore"

echo "3. Commit skapad"

# Push
git push

echo "✅ Repo rensat och pushat till GitHub!"
