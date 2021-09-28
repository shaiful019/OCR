from pdf2image import convert_from_path
images = convert_from_path("norlite 4-22-21 b.pdf", 500)
for i, image in enumerate(images):
    fname = 'image'+str(i)+'.jpg'
    image.save(fname, "JPEG")