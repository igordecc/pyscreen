from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas
import os
import sys
import textwrap


class HeaderedImage:
    def __init__(self, path, url, data, savepath):
        self.path = path
        self.url = url
        self.data = data
        self.savepath = savepath
        font = ImageFont.load_default().font
        self.fontd = {"padding": 10,
                 "font": font,
                 "font_size": None,
                 "char_w": (font.getsize("1"))[0],
                 "char_h": (font.getsize("1"))[1]
                 }

    def coilTheText(self, text, width: int, fontd):
        """

        :param text: string, or list of strings
        :param width: pixel width of text line
        :param fontd: special dictionary, predefined in __init__ of the class
        :return: coiled text
        """
        padding = fontd["padding"]
        font = fontd["font"]
        char_w = fontd["char_w"]
        # coil list

        def coilText(text):
            # not hardcoded
            find_number_of_chars = lambda w, p, c: (w - 2 * p) // c
            number_of_chars = round(find_number_of_chars(width, padding, char_w))
            if number_of_chars < 1:
                number_of_chars = 1
            # text wrap consume width in characters
            # that means prog mast calculate width in number of characters beforehand
            coiledText = textwrap.wrap(text, width=(number_of_chars))
            return coiledText

        if isinstance(text, list):
            coiledText = []
            for tex in text:
                lines = coilText(tex)
                coiledText.extend(lines)
            return coiledText
        else:
            return coilText(text)

    def testCoilTheText(self):
        smallest_case = self.coilTheText("OneONeOneoneOneOne", 20, self.fontd)
        print(smallest_case)
        largest_case = self.coilTheText("OneONeOneoneOneOne", 2000, self.fontd)
        print(largest_case)
        fractional_case = self.coilTheText("OneONeOneoneOneOne", 73.5, self.fontd)
        print(fractional_case)
        negative_case = self.coilTheText("OneONeOneoneOneOne", -73.5, self.fontd)
        print(negative_case)


    def createHeaderImage(self, url, time, img_w):
        """create Header image based on img_w, from list of lines"""

        # determine hight of header
        padding = self.fontd["padding"]
        char_h = self.fontd["char_h"]



        # Create new image
        text = [url, time]
        lines = self.coilTheText(text, img_w, self.fontd)

        calcHeaderH = lambda h, p, l: (h + p)*l + p   # header height = row height * row number
        header_H = calcHeaderH(char_h, padding, len(lines))


        def linesOnImage(header_w, header_h):
            headerImg = Image.new('RGB', (header_w, header_H), color=(255, 255, 255))
            draw = ImageDraw.Draw(headerImg)

            # Place text on new image
            y = padding
            for line in lines:
                draw.multiline_text((padding, y), line, fill=(0, 0, 0))
                y += char_h + padding

            return headerImg

        return headerImg

    def concatImagesVertically(self, images):
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


    def main(self, path, url, data, savepath):
        image = Image.open(path)
        headerImg = self.createHeaderImage(url, data, img_w=image.size[0])
        multiImage = self.concatImagesVertically([headerImg, image])
        multiImage.save(savepath)
        return savepath

    def test(self):
        self.testCoilTheText()


if __name__ == '__main__':
    path = "D:\\test.png"
    url = "https://stackoverflow.com/questions/16373425/add-text-on-image-using-pil"
    data = "30.10.2020"
    savepath = 'test.png'
    himg = HeaderedImage(path, url, data, savepath)
    himg.test()
