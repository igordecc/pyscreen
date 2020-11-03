from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import webbrowser
import pandas
import os
import sys

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


def testImageWriter():
    path = "D:\\test.png"
    url = "https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil"
    data = "30.10.2020"
    savepath = 'test.png'
    writeOnImage(path, url, data, savepath)
    # webbrowser.open(savepath)

# ======================
# PROTOTYPE
# imgs, url, data
# or img url data
def extractInfoFromFile(file):
    dataframe = pandas.read_csv(file)

    datalist = []
    for row in dataframe.itertuples():
        # index   url	img 	data	save	savetag
        # [0, 'https://www.avito.ru/saratov/kvartiry/1-k_kvartira_34_m_89_et._1989595079', 'D:\\pyscreen\\imgs\\webpage00669.png', '03.11.2020', 'D:\\pyscreen\\imgs\\webpage00669.png', 'withhead']
        datalist.append(list(row))
    return datalist


def addSavetagToSavepath(tag, path):
    dir = os.path.dirname(path)
    file = os.path.basename(path)
    tagfile = os.path.join(dir, tag + file)
    return tagfile


def main(file):
    if os.path.isfile(file):
        print("Выполнение..")
        datalist = extractInfoFromFile(file)
        for entry in datalist:
            print(str(entry))
            # index   url	img 	data	save	savetag
            index = entry[0]
            url = entry[1]
            img = entry[2]
            data = entry[3]
            savepath = addSavetagToSavepath(entry[5], entry[4])
            writeOnImage(img, url, data, savepath)
        print("Завершено успешно")
    else:
        print("Ошибка. Непрвильный путь к файлу")


if __name__ == '__main__':

    file = 'D:\\test.csv'
    file = sys.argv[1]
    main(file)






