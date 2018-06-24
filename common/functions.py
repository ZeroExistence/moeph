import PIL
from PIL import Image as pilimage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.six import BytesIO


# Create your models here.

def resize(image, width, height):
    img = pilimage.open(image)
    exif = None
    if 'exif' in img.info:
        exif = img.info['exif']
    img = img.crop(correct_aspect(img, width, height))
    img = img.resize((width,height), PIL.Image.ANTIALIAS)
    img = img.convert("RGB")
    output = BytesIO()

    if exif:
        img.save(output, format='JPEG', exif=exif, quality=90)
    else:
        img.save(output, format='JPEG', quality=90)

    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField', "%s" % image.name, 'image/jpeg', output.getbuffer().nbytes, None)


# Function to get 1.5 ratio for image
def correct_aspect(img, width, height):
    oheight = float(img.size[1])
    owidth = float(img.size[0])
    ratio = oheight/owidth
    aspect = float(height)/float(width)
    if ratio > aspect:
        height = owidth*float(aspect)
        width = owidth
        offset = (oheight-height)/2
        uset = 0+offset
        dset = oheight-offset
        lset = 0
        rset = width
    elif ratio < aspect:
        height = oheight
        width = oheight/float(aspect)
        offset = (owidth-width)/2
        lset = 0+offset
        rset = owidth-offset
        uset = 0
        dset = height
    else:
        lset = 0
        rset = owidth
        uset = 0
        dset = oheight
    return (round(lset,2), round(uset,2), round(rset,2), round(dset,2))
