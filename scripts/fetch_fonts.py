"""Unduh font Google Fonts dan simpan lokal agar aplikasi 100% offline."""
import os, re, urllib.request

CSS_URL = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600"
           "&family=Figtree:wght@400;500;600&display=swap")
OUT = os.path.join(os.path.dirname(__file__), "..", "app", "src", "main", "assets", "fonts")
UA = "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 Chrome/120.0 Mobile Safari/537.36"

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA})).read()

os.makedirs(OUT, exist_ok=True)
css = get(CSS_URL).decode()
urls = list(dict.fromkeys(re.findall(r"url\((https://[^)]+)\)", css)))
for i, u in enumerate(urls):
    name = f"font{i}.woff2"
    open(os.path.join(OUT, name), "wb").write(get(u))
    css = css.replace(u, name)
open(os.path.join(OUT, "fonts.css"), "w", encoding="utf-8").write(css)
print(f"OK: {len(urls)} file font disimpan di {os.path.abspath(OUT)}")
