from PIL import Image
im = Image.open('baidu_logo.gif')      # 读入一个GIF文件
try:
    im.save('picframe{:03d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('picframe{:03d}.png'.format(im.tell()))
except:
    print("处理结束")
