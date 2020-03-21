# TODO: add methods for
#       save log files (savelog)
#       parser macros
# 

module_dict = {'main' : '00', 'merger' : '01', 'extractor' : '02'}

def savelog(autoslides, text):
    currmodule = autoslides.currmodule 
    currmodule_num = module_dict[currmodule]
    filepath = autoslides.debugpath + '/' + currmodule_num + '_' + currmodule + '.log'
    
    try:
        f = open(filepath, 'w')
        f.write(text)
        f.close()
    except Exception as e:
        print('Error in log-file opening for ' + currmodule + ' : ' + str(e))

    return