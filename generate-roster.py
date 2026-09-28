import os, json
folder = "ai-artist-images-roster"
files = sorted(os.listdir(folder))
roster = []
# known mapping
map_names = {
 "alep1_ai-king-pharaoh.jpeg": ("Aleph","King Pharaoh","Judah","The Unsealing"),
 "aleph-2.0-ai-papay.jpg": ("Aleph","Aleph 2.0 Papay","Judah","The Scribe"),
 "aleph1_si-king-pharaoh.jpeg": ("Aleph","Si King Pharaoh","Judah","Sphinx"),
 "bet-artist-ai_desert_rose.jpg": ("Bet","Desert Rose","Reuben","AI Artist"),
 "daleth_ai-lonestar.jpg": ("Daleth","Lonestar","Gad","AI Artist"),
 "gimel_ai-dj_dehrtay-dog.jpeg": ("Gimel","DJ Dehrtay Dog","Dan","AI Artist"),
 "heh_ai-pruh.jpg": ("Heh","Pruh","Asher","AI Artist"),
 "vav_ai-dahctor.jpg": ("Vav","Dahctor","Issachar","AI Artist"),
 "zayin_dj-tatiana_sirleaf.jpeg": ("Zayin","DJ Tatiana Sirleaf","Zebulun","Ayin Crew"),
 ",ayin_dj-tatiana_sirleaf.png": ("Ayin","DJ Tatiana Sirleaf","Zebulun","Ayin Crew"),
 "chet_ai_truth-ben-yhvh.jpeg": ("Chet","Truth Ben YHVH","Naphtali","The Truth"),
 "1stlamed_ai_twin-imhotep.jpg": ("Lamed","Twin Imhotep","Levi","Twin 1"),
 "2ndlamed_ai-twin-daat.jpg": ("Lamed","Twin Daat","Levi","Twin 2"),
 "yod_ai-nefertiti.jpg": ("Yod","Nefertiti","Benjamin","Queen"),
 "ayin-ai_ivory.jpg": ("Ayin","Ivory","Ephraim","AI Artist"),
 "nun_ai-hallel_node.jpg": ("Nun","Hallel Node","Manasseh","AI Artist"),
 "tet_ai-soundclash.jpg": ("Tet","Soundclash","Simeon","AI Artist"),
 "shin_fullcrew-unsealing_tour.webp": ("Shin","Fullcrew Unsealing Tour","Reuben","Unsealing"),
 "sin_ai-artists-group.photo.png": ("Sin","AI Artists Group","Simeon","Group Seal"),
 "poster_88s-ai_artists.jpg": ("Poster","88s AI Artists","All Tribes","Poster"),
 "ai-metatron.jpeg": ("Metatron","Metatron","Crown","Toth Console"),
 "ai-metatron_box.jpeg": ("Metatron","Metatron Box","Crown","Toth Console"),
 "metatron_toth-ai-console.jpg": ("Metatron","Toth Console","Crown","Console"),
}
for f in files:
 if f.lower().endswith(('.jpg','.jpeg','.png','.webp','.gif')):
   if f in map_names:
     letter,name,tribe,role = map_names[f]
   elif "Screenshot" in f:
     # these are your Asian + remaining 88s renders
     letter="Pe"
     name=f"Asian Character — {f.replace('Screenshot_','').replace('.jpg','')}"
     tribe="Issachar"
     role="88s Asian Seal — Breathing"
   else:
     letter="Pe"
     name=f.replace('_',' ').replace('.jpg','').replace('.jpeg','')
     tribe="88s"
     role="AI Artist"
   roster.append({"letter":letter,"name":name,"tribe":tribe,"image":f"ai-artist-images-roster/{f}","role":role})

with open("roster.json","w") as out:
 json.dump({"roster": roster}, out, indent=2)
print(f"Generated roster.json with {len(roster)} entries")
