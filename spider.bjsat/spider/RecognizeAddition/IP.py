# -*- coding: utf-8 -*-

from CR import *
from PIL import Image


class ImageProcessing:
    # --------------------------------------------------------------#
    def __init__(self, name='', im=None):
        self.name = name
        self.im = im

    # --------------------------------------------------------------#
    # 根据RGB来去除噪声
    def get_kind_by_rgb(self):
        self.kind = []
        VAL = 125000
        if len(self.name) != 0:
            im = Image.open(self.name)
        elif self.im != None:
            im = self.im
        else:
            return self.kind
        if im.mode != 'RGB':
            im = im.convert('RGB')
        for x in range(im.size[1]):
            self.kind.append([])
            for y in range(im.size[0]):
                tmp = im.getpixel((y, x))
                u = tmp[0] * tmp[1] * tmp[2]
                if u < VAL:
                    self.kind[x].append(1)
                else:
                    self.kind[x].append(0)
        return self.kind

    # --------------------------------------------------------------#
    # 根据位置截取字符，截取数字信息
    def get_char_by_size(self):
        self.char = []
        SIZE = (((7, 6), (15, 16)), ((33, 6), (41, 16)))
        for i in range(len(SIZE)):
            self.char.append([])
            for x in range(SIZE[i][0][1], SIZE[i][1][1]):
                self.char[i].append([])
                for y in range(SIZE[i][0][0], SIZE[i][1][0]):
                    self.char[i][x - SIZE[i][0][1]].append(self.kind[x][y])
        return self.char

    # --------------------------------------------------------------#
    def run(self):
        self.output = ''
        if len(self.get_kind_by_rgb()) == 0:
            return self.output
        self.get_char_by_size()
        self.output = CharacterRecognition(self.char).run()
        return self.output

# if __name__ == '__main__':
#     noResultTime = 0
#     for i in range(1, 301):
#         test = ImageProcessing('data/Fig/Fig_%03d.png' % i)
#         result = test.run()
#         if len(result) == 0:
#             noResultTime += 1
#         print u'【', i, u'】', result
#     print 'noResultTime =', noResultTime
#     # noResultTime = 0
