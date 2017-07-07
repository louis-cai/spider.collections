# -*- coding: utf-8 -*-

import json


class CharacterRecognition:
    # --------------------------------------------------------------#
    def __init__(self, char):
        self.char = char

    # --------------------------------------------------------------#
    def rec_number(self):
        self.number = ['', '']
        with open('data/num_data.json', 'r') as f:
            data = json.load(f)
        for N in (0, 1):
            amount = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
            for i in range(len(data)):
                s = 0
                for x in range(len(self.char[N])):
                    for y in range(len(self.char[N][0])):
                        if data[i][1][x][y] == self.char[N][x][y]:
                            s += 1
                amount[data[i][0]] = s
            result = 0
            for name in amount:
                if amount[name] > result:
                    result = amount[name]
                    self.number[N] = name
        return self.number

    # --------------------------------------------------------------#
    def run(self):
        self.rec_number()
        if self.number[0] == '' or self.number[1] == '':
            return ''
        a = int(self.number[0])
        b = int(self.number[1])
        print a, "+", b
        return str(a + b)
