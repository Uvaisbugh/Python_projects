# This is the end of the image_resizer.py file
from PIL import Image

def resize_image(file,sizel, size2) :
    image = Image.open(file)

    print(f"Current size : {image.size}" )

    resized_image = image.resize(( sizel, size2))
    
    resized_image.save(file[0:-5] + str(size1) + '.jpeg')

file_name = input('Enter file name: ')
size1 = int(input( ' Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(file_name,size1, size2)
print('Image resized successfully')
