# IT Security Starter Pack

En samling **enkla, säkra och pedagogiska** mini-projekt du kan lägga upp på GitHub som student inom IT-säkerhet.
All kod är **defensiv/utbildande** (ej intrångstester).

## Innehåll
- `projects/password_strength_checker/` – Enkel lösenordsanalys (längd, teckenklasser, entropi-estimat)
- `projects/phishing_url_rules/` – Basregler för att flagga misstänkta URL:er
- `projects/file_integrity_checker/` – Hashar filer (SHA-256) och jämför med manifest
- `projects/log_parser_firewall/` – Parser för förenklade brandväggsloggar + statistik

## Kom igång (lokalt)
```bash
# (valfritt) skapa virtuell miljö
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python -m pytest -q
```

## Publicera på GitHub
1. Skapa ett nytt repo på GitHub (tomt).
2. Kör följande i den här katalogen:
```bash
git init
git add .
git commit -m "Init: IT security starter pack"
git branch -M main
git remote add origin <din-repo-url>
git push -u origin main
```
3. Aktivera CI (GitHub Actions) – workflow ingår i `.github/workflows/python.yml`.

## Licens
MIT – fritt att använda och bygga vidare.
