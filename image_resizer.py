from PIL import Image

def image_resizer(size1, size2):
    image = Image.open('test.jpg')
    print('size of the image : ', image.size)
    resized_image = image.resize((size1, size2))
    resized_image.save('rahdi.jpg')

image_resizer(500, 520)