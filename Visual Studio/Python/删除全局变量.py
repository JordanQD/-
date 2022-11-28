def mydelallglobals():
    d = globals()
    for name in d:
        try:
            if name.startswith('_') or name in ['In','Out','get_ipython','exit','quit','json']:
                continue
            #print('name:',name)
            exec('del ' + name)
        except:
            pass
mydelallglobals()
d = globals()
print('d:',d)