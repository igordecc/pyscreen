# test proj
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import PIL
import webbrowser
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys


def writeOnImage():
    path = "D:\\test.png"
    image = Image.open(path)


    url = "https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil"
    data = "30.10.2020"

    draw = ImageDraw.Draw(image)
    draw.text((0,0), url + " " + data, (255,0,0))
    draw.text()
    savepath = "imgs\\temp.png"
    image.save(savepath)
    webbrowser.open(savepath)


def _writeOnImage(imgpath, savepath, *args):
    image = Image.open(imgpath)
    draw = ImageDraw.Draw(image)
    print(image._check_size())
    # Image.new("RGB", )
    font = ImageFont.truetype(font="ABeeZee-Regular.otf", size=23)
    y = 0
    for arg in args:
        draw.text((0,y), arg, (0,0,0), font=font)
        y += 30

    image.save(savepath)
    webbrowser.open(savepath)


def writeOneImageFromConcole():
    cmdargs = sys.argv
    print(cmdargs)
    programname = cmdargs[0]
    imagepath = cmdargs[1]
    savepath = cmdargs[2]
    _writeOnImage(imagepath, savepath, *cmdargs[3:])


if __name__ == '__main__':
    writeOneImageFromConcole()
    print("ok")

