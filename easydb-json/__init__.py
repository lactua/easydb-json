from threading import Thread as _Thread
from json import load as _load, dump as _dump
from os.path import dirname as _dirname, exists as _exists, isfile as _isfile, abspath as _abspath
from time import sleep as _sleep

def _writeDB():
    global db, path
    while True:
        with open(path, 'w') as file:
            _dump(db, file, indent=4)
        _sleep(0.5)

def init(path):
    global db
    path = _abspath(path)
    globals()['path'] = path
    
    if not _exists(_dirname(path)):
        raise FileNotFoundError(f"{_dirname(path)} don't exists")
    
    if _exists(path):
    
        if not _isfile(path):
            raise FileNotFoundError(f"{path} is not a file")
        
        with open(path, 'r') as file:
            db = _load(file)
        
    else:
        open(path,'w').close()
        db = {}
        
    _Thread(target=_writeDB).start()
    
    return db