import pathlib
p=pathlib.Path("index.html").read_text()
# make loader robust: if roster image already starts with ai-artist-images-roster, use as is
old=" card.innerHTML ="
new=" var imgSrc = r.image.startsWith('ai-artist')? r.image : IMAGE_BASE + r.image;\n card.innerHTML ="
if old in p and "imgSrc" not in p:
    p=p.replace(old,new)
    # also replace IMAGE_BASE + r.image inside template
    p=p.replace("IMAGE_BASE + r.image","imgSrc")
    pathlib.Path("index.html").write_text(p)
    print("Loader patched to use imgSrc")
else:
    print("Loader already patched or pattern not found")
