from PIL import Image
im = Image.open('birdnest.jpg')
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save('birdnestBGR.jpg')
