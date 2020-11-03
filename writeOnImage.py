from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import webbrowser


def writeOnImage(path, url, data, savepath):
    image = Image.open(path)
    headerImg = createHeaderImage(url, data, imgWidth=image.size[0])
    multiImage = createNewImageFromMultiple(image.size[0], (image.size[1] + headerImg.size[1]), [headerImg, image] )

    multiImage.save(savepath)
    return savepath



def createNewImageFromMultiple(width, height, images):
    multiImage = Image.new('RGB', (width, height))
    y_offset = 0
    for im in images:
        multiImage.paste(im, (0, y_offset))
        y_offset += im.size[1]

    return multiImage


def createHeaderImage(url, data, imgWidth):
    y = 60
    x = imgWidth

    headerImg = Image.new('RGB', (x, y))
    draw = ImageDraw.Draw(headerImg)
    draw.multiline_text((5, 5), url)
    draw.text((5, 35), data)

    return headerImg


# imgs, url, data
# or img url data
def extractInfoFromFile(file):
    


if __name__ == '__main__':
    path = "D:\\test.png"
    url = "https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil"
    data = "30.10.2020"
    savepath = 'test.png'
    writeOnImage(path, url, data, savepath)
    webbrowser.open(savepath)