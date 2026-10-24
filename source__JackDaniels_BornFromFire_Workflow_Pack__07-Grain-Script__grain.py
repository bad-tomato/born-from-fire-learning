import os
from PIL import Image, ImageChops, ImageFilter, ImageDraw

D = "/tmp/grain"
# (name, extra blur to tame AI over-sharpness)
PLATES = [
    ("01_distiller", 0.9),
    ("02_char", 0.45),
    ("03_drip", 0.45),
    ("04_icedrop", 0.5),
    ("05_bottle", 0.5),
]

def filmify(path, blur, sigma=26, amt=0.55):
    im = Image.open(path).convert("RGB")
    if blur > 0:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    w, h = im.size
    noise = Image.effect_noise((w, h), sigma).convert("L")
    nrgb = Image.merge("RGB", (noise, noise, noise))
    grained = ImageChops.soft_light(im, nrgb)
    return Image.blend(im, grained, amt)

outs = []
for name, blur in PLATES:
    src = os.path.join(D, f"src_{name}.png")
    out = os.path.join(D, f"grained_{name}.png")
    im = filmify(src, blur)
    im.save(out)
    outs.append((name, out, im.size))
    print(name, im.size, "->", out)

# vertical contact sheet to eyeball the grain/look
thumbs = []
for name, _ in PLATES:
    t = Image.open(os.path.join(D, f"grained_{name}.png")).convert("RGB")
    t.thumbnail((680, 383))
    thumbs.append((name, t))
pad = 14
cw = max(t.size[0] for _, t in thumbs) + 2 * pad
chh = sum(t.size[1] for _, t in thumbs) + pad * (len(thumbs) + 1)
sheet = Image.new("RGB", (cw, chh), (18, 15, 11))
y = pad
for name, t in thumbs:
    x = (cw - t.size[0]) // 2
    sheet.paste(t, (x, y))
    y += t.size[1] + pad
sheet.save(os.path.join(D, "preview.png"))
print("PREVIEW", sheet.size)
