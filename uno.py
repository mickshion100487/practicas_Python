from PIL import Image
img = Image.open("hulk2.jpg")
#img.show()

#print(img.mode)
#img=img.convert("L")
#img.save("maximus2.jpg")
#img = img.rotate(-90)
#img.show()
#print(img.size)
#print(img.width)
#print(img.height)
img=img.resize((300,300))
box = (100,100,250,250)
img=img.crop(box)
img.show()
