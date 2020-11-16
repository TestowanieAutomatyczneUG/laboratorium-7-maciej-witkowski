class RomanNumerals:
    def __init__(self):
        self.base = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

    def roman(self, num):
        def partOfRoman(numPart, decimalPart):
            if 1 <= numPart <= 3:
                return self.base[int('1' + str('0' * decimalPart))] * numPart
            elif numPart == 4:
                return self.base[int('1' + str('0' * decimalPart))] + self.base[int('5' + str('0' * decimalPart))]
            elif 5 <= numPart <= 8:
                return self.base[int('5' + str('0' * decimalPart))] + (
                            (numPart - 5) * self.base[int('1' + str('0' * decimalPart))])
            elif numPart == 9:
                return self.base[int('1' + str('0' * decimalPart))] + self.base[int('10' + str('0' * decimalPart))]
            else:
                return ""

        divided = [int(i) for i in str(num)]
        result = ""
        for i in range(len(divided)):
            result += partOfRoman(divided[i], (len(divided) - i) - 1)
        return result
