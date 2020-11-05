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

    def coilTheText(self, text, width):
        # coil list
        def coilText(text, width):
            padding = 10
            font = ImageFont.load_default().font
            char_w, char_h = font.getsize("1")
            lines = textwrap.wrap(text, width=((width - 2 * padding) // char_w))


        if isinstance(text, list):
            coiledText = []
            for tex in text:
                lines = coilText(tex, width)
                coiledText.extend(lines)
        else:
            ...


    def createHeaderImage(self, url, time, img_w):
        """create Header image based on img_w, from list of lines"""

        # determine hight of header
        padding = 10
        font = ImageFont.load_default().font
        char_w, char_h = font.getsize("1")
        lines = textwrap.wrap(url, width=((img_w - 2 * padding) // char_w))
        line_w, line_h = font.getsize(lines[0])

        # Create new image
        calcHeaderH = lambda h, p, l: (h + p)*(l + 1) + p   # header height = row height * (row number + 1 data row)
        header_H = calcHeaderH(line_h, padding, len(lines))
        headerImg = Image.new('RGB', (img_w, header_H), color=(255, 255, 255))
        draw = ImageDraw.Draw(headerImg)

        # Place text on new image
        y = padding
        for line in lines:
            draw.multiline_text((padding, y), line, fill=(0, 0, 0))
            y += line_h + padding
        draw.text((padding, y + line_h), str(time), fill=(0, 0, 0))

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

