from pdf2image import convert_from_path
images = convert_from_path("data/CQ 4-1-21.pdf", 500)
for i, image in enumerate(images):
    fname = 'bank_statement'+str(i)+'.jpg'
    image.save(fname, "JPEG")