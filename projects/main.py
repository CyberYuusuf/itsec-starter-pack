import re
from urllib.parse import urlparse

SUSPICIOUS_TLDS = {"zip", "mov"}
MAX_HYPHENS = 3

def is_ip(host: str) -> bool:
    return bool(re.fullmatch(r'(?:\d{1,3}\.){3}\d{1,3}', host))

def score_url(u: str) -> tuple[int, list[str]]:
    reasons = []
    score = 0
    try:
        p = urlparse(u if "://" in u else "http://" + u)
        host = p.hostname or ""
    except Exception:
        return 5, ["Ogiltig URL-parsning"]

    if "@" in u:
        score += 2; reasons.append("Innehåller @ i URLen")
    if is_ip(host):
        score += 2; reasons.append("IP-adress som domän")
    if host.count("-") > MAX_HYPHENS:
        score += 1; reasons.append("Många bindestreck i domän")
    if p.port and p.port not in (80, 443):
        score += 1; reasons.append(f"Ovanlig port: {p.port}")
    if any(host.endswith("." + t) or host == t for t in SUSPICIOUS_TLDS):
        score += 1; reasons.append("TLD som ofta missbrukas")
    if len(host.split(".")) > 4:
        score += 1; reasons.append("Djupt subdomän-nivå")

    return score, reasons

def label(score: int) -> str:
    if score <= 1: return "Troligen OK"
    if score == 2: return "Granska noga"
    if score <= 4: return "Misstänkt"
    return "Hög risk"

def main():
    print("== Phishing URL Rules (Educational) ==")
    print("Klistra in URL (tom rad för att avsluta):")
    while True:
        s = input("> ").strip()
        if not s:
            break
        score, reasons = score_url(s)
        print(f"Bedömning: {label(score)} (score={score})")
        if reasons:
            print("Skäl:")
            for r in reasons:
                print(" -", r)
        print()
    print("Klart. Var alltid försiktig med länkar.")

if __name__ == "__main__":
    main()
