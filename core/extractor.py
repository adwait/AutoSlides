import re

class Block:
    content = None
    localpath = None
    address = None

    def __init__(self, con, lpath, add):
        self.content, self.localpath, self.address = con, lpath, add

    def prettyprint(self):
        print("\tAddress:{0}\n\tLocalpath:{1}\n\tContent:{2}".format(self.address, self.localpath, self.content))


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

        for b in rawblocks:
            if re.match(pathreg, b):
                lpath = re.match(pathreg, b).group(1)
            elif key:
                if key == b:
                    key = ''
                else:
                    cleankey = re.match(addressreg, key).group(1)
                    self.rawdict[cleankey] = Block(b.strip(), lpath, cleankey)
            else:
                if re.match(addressreg, b):
                    key = b

        return self.rawdict

    def prettyprint(self):
        for key, value in self.rawdict.items():
            print(key + ":")
            value.prettyprint()