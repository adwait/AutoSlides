#!/usr/bin/env python

'''
AutoSlides 0.1

A tool to convert annotated LaTeX documents into presentation slides 
'''

VERSION_NUMBER = 0.1

import importlib
import time
import sys
import os
import shutil
import getopt
# import exceptions

import core.merger
import core.utils
# import core.content_extractor


help_string = 'please consult source code'

class autoslides:

    cmdline = None
    options = None
    args = None
    debug = False

    hyperparams = []

    inputfile = None
    configuration = None

    debugpath = 'log'

    # module_dir = 'modules.'
    # modulelist = ['merge']
    # modules = []
    currmodule = None

def setconfig(config):
    # TODO: decide on configuration options and format and implement this method
    print('custom config is currently disabled, sorry\n')
    sys.exit(1)

def main():

    autoslides.cmdline = sys.argv
    autoslides.timestamp = time.time()

    # os.makedirs(os.path.dirname(autoslides.debugpath), exist_ok=True)

    print('')
    print(' AutoSlides ')
    print('------------')
    print('')

    # for module_name in modulelist:
    #     try:
    #         mod = importlib.import_module(module_dir + module_name)
    #         autoslides.modules.append(getattr(mod, module_name)())
    #     except ImportError as e:
    #         print("import error for module {0}\nplease check the installation".format(module_name)
    #         sys.exit(1)
    #     except AttributeError as e:
    #         print("attribute error for module {0}\nplease check the installation".format(module_name))
    #     except Exception as e:
    #         print("initialization failed for module {0}\nplease check the installation".format(module_name))

    try:
        args = "hi:c:vd"
        autoslides.options, autoslides.args = getopt.getopt(autoslides.cmdline[1:], args)
    except getopt.GetoptError:
        print('AutoSlides: incorrect usage\n')

    for o, a in autoslides.options:
        if o in "-v":
            print(VERSION_NUMBER)
        elif o in "-h":
            print(help_string + '\n')
        elif o in "-i":
            autoslides.inputfile = a
        elif o in "-c": 
            autoslides.setconfig(a)
        elif  o in "d":
            autoslides.debug = True

    # Merge LaTeX source into a single file
    autoslides.currmodule = 'merger'
    Merger = core.merger.Merger()
    # print(autoslides.inputfile)
    Merger.loadfromstring(autoslides.inputfile, autoslides)
    output = Merger.getoutput()

    print(output)

    if autoslides.debug:
        core.utils.savelog('{0}/merger__input.log'.format(autoslides.debugpath),input)
        core.utils.savelog('{0}/merger__output.log'.format(autoslides.debugpath),output)
        


if __name__ == "__main__":
    main()        


