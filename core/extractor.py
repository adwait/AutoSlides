import re

class Block:
    content = None
    localpath = None
    address = None

    def __init__(self, con, lpath, add):
        self.content, self.localpath, self.address = con, lpath, add


class Extractor:

    ftext = None
    rawdict = {}

    def __init__(self):
        pass

    def loadfrommain(self, asl):
        self.ftext = asl.rawtext

    def getblocks(self):
        rawblocks = re.split(r'(<--(?:\S)*-->)', self.ftext)
        addressreg = re.compile(r'<--(\d(?:\.\d)*)-->')
        pathreg = re.compile(r'<--path\:((?:\S)*)-->')

        key = ''
        lpath = ''

        print(rawblocks)

        for b in rawblocks:
            if re.match(pathreg, b):
                lpath = re.match(pathreg, b).group(1)
            elif key:
                if key == b:
                    key = ''
                else:
                    self.rawdict[re.match(addressreg, key).group(1)] = (b.strip(), lpath)
            else:
                if re.match(addressreg, b):
                    key = b

        return self.rawdict