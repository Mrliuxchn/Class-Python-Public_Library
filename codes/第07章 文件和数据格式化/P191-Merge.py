from PIL import Image
im = Image.open('birdnest.jpg')
r, g, b = im.split()
newg = g.point(lambda i:i*0.9)
newb = g.point(lambda i:i<100)
om = Image.merge(im.mode,(r,newg, newb))
om.save('birdnestMerge.jpg')
