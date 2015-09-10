from SimpleCV import ImageSet

img_set = ImageSet(".")

for img in img_set:
    oldname = img.filename
    newname = oldname[0:-3] + 'jpg'
    print 'Converting ' + oldname + ' to ' + newname
    img.save(newname)
