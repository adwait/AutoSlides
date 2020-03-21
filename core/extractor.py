import re

class Block:
    content = None
    address = None


class Extractor:

    ftext = None
    rawdict = {}

    def __init__(self):
        pass

    def loadfrommain(self, asl):
        self.ftext = asl.rawtext

    def getblocks(self):
        rawblocks = re.split(r'<--(\d(?:\.\d)*)-->', self.ftext)
        addressreg = re.compile(r'\d(?:\.\d)*')

        key = ''

        for b in rawblocks:
            if key:
                if key == b:
                    key = ''
                else:
                    self.rawdict[key] = b.strip()
            else:
                if re.match(addressreg, b):
                    key = b

        return self.rawdict

