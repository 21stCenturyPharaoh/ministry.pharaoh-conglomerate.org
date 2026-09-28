import json, os, shutil, re, pathlib
# rename comma file
bad = pathlib.Path("ai-artist-images-roster/,ayin_dj-tatiana_sirleaf.png")
if bad.exists():
    bad.rename("ai-artist-images-roster/ayin_dj-tatiana_sirleaf.png")
# kill duplicate roster/
if os.path.isdir("roster"):
    shutil.rmtree("roster")
# clean roster.json
with open("roster.json") as f:
    d=json.load(f)
roster=d.get("roster") or d.get("artists") or []
clean=[]
for it in roster:
    img=it.get("image","").replace("ai-artist-images-roster/,","").replace("ai-artist-images-roster/","").replace(",","").strip("/")
    it["image"]=img
    if "id" not in it:
        it["id"]=re.sub(r'[^a-z0-9]+','-',it.get("name","").lower()).strip('-')
    clean.append(it)
with open("roster.json","w") as f:
    json.dump({"roster":clean,"artists":clean},f,indent=2)
# patch index.html
html=pathlib.Path("index.html").read_text()
html=html.replace('renderRoster(data.artists || []);','renderRoster(data.roster || data.artists || []);')
html=html.replace("var imgSrc = r.image.startsWith('ai-artist')? r.image : IMAGE_BASE + r.image;","")
html=html.replace("a.image.startsWith('ai-artist')? a.image : IMAGE_BASE + a.image","a.image.indexOf('/')>-1 ? a.image : IMAGE_BASE + a.image")
if 'id="book-cover"' not in html:
    book="""
  <section id="book-cover">
    <h2>📖 The Unsealing — Book Cover</h2>
    <div class="card" style="text-align:center">
      <img src="./ai-artist-images-roster/poster_88s-ai_artists.jpg" alt="The Unsealing" style="width:100%;max-width:380px;border-radius:12px;border:1px solid var(--gold);margin:0 auto 12px;display:block">
      <p style="color:var(--ink);font-size:14px">The Unsealing — Legacy of Mama Hajah Norfeh & Col. Sirleaf</p>
      <div class="btnrow"><a class="btn solid" href="https://www.amazon.com/dp/B0B3H8886Z">Buy on Amazon</a></div>
    </div>
  </section>
"""
    html=html.replace("<section>\n    <h2>🎵 Micdom AI Records",book+"\n  <section>\n    <h2>🎵 Micdom AI Records")
pathlib.Path("index.html").write_text(html)
print(f"Fixed {len(clean)} artists + injected book cover")
