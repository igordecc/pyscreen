from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas
import os
import sys
import textwrap


def writeOnImage(path, url, data, savepath):
    image = Image.open(path)
    headerImg = createHeaderImage(url, data, imgWidth=image.size[0])
    multiImage = concatImages([headerImg, image])
    multiImage.save(savepath)
    return savepath


def createHeaderImage(url, data, imgWidth):
    x = imgWidth

    # determine hight of header
    padding = 10
    font = ImageFont.load_default().font
    charwidth, charheight = font.getsize("1")
    lines = textwrap.wrap(url, width=((imgWidth - 2 * padding)//charwidth))
    width, height = font.getsize(lines[0])


    # header height = row height * (row number + 1 data row)
    maxY = (height + padding) * (len(lines) + 1) + padding
    headerImg = Image.new('RGB', (x, maxY), color=(255, 255, 255))
    draw = ImageDraw.Draw(headerImg)
    y = padding
    for line in lines:
        draw.multiline_text((padding, y), line, fill=(0, 0, 0))
        y += height + padding

    draw.text((padding, y + height), str(data), fill=(0, 0, 0))
    return headerImg


def concatImages(images):
    # concat one pic to another
    # width is const
    x = images[0].size[0]
    y = 0
    for img in images:
        y += img.size[1]
    multiImage = Image.new('RGB', (x, y))
    y_offset = 0
    for im in images:
        multiImage.paste(im, (0, y_offset))
        y_offset += im.size[1]
    return multiImage


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
    dataframe = pandas.read_excel(file)

    datalist = []
    for row in dataframe.itertuples():
        # index   url	img 	data	save	savetag
        datalist.append(list(row))
    return datalist


def addSavetagToSavepath(tag, path):
    dir = os.path.dirname(path)
    file = os.path.basename(path)
    tagfile = os.path.join(dir, str(tag) + file)
    return tagfile


def main(file):
    if os.path.isfile(file):
        print("Выполнение..")
        datalist = extractInfoFromFile(file)
        for entry in datalist:
            print(entry)
            if hasattr(entry, "__iter__"):
                # index   url	img 	data	save	savetag
                index = entry[0]
                url = entry[1]
                img = entry[2]
                data = entry[3]
                savepath = entry[4]
                tag = entry[5]
                if str(tag) != 'nan':
                    savepath = addSavetagToSavepath(tag, savepath)
                writeOnImage(img, url, data, savepath)
            else:
                input("ERROR: Entry is not an iterable. Ошибка считывания строки.")
                raise ValueError("Entry is not an iterable. Ошибка считывания строки.")
        print("Завершено успешно")
    else:
        print("Ошибка. Непрвильный путь к файлу")


if __name__ == '__main__':
    file = 'D:\\test.csv'
    file = sys.argv[1]
    main(file)






