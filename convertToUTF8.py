import os;
import sys;
import pathlib;
from chardet.universaldetector import UniversalDetector
from pathlib import Path

detector = UniversalDetector()

try:
    infilepath = sys.argv[1]
except IndexError:
    infilepath = pathlib.Path().resolve()

print('Pasta de trabalho: ', infilepath)

try:
    outfilepath = sys.argv[2]
except IndexError:
    outfilepath = pathlib.Path().resolve()

print('Pasta de saída: ', outfilepath)

def loadfile(filename):
    inpath = Path(infilepath+'\\'+filename)
    print('Carregando arquivo ', inpath)
    
    checkencode(inpath)

def checkencode(inpath):

    detector.reset()
    for line in open(inpath, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    fileenconde = detector.result['encoding']
    print('Encode detectado '+ fileenconde)

    if fileenconde == 'ISO-8859-1':
        outpath = Path(outfilepath+'\\'+filename)
        savefile(inpath, outpath)

def savefile(inpath, outpath):
    print('Salvando arquivo ', outpath)

    #outpath.write_text(inpath.read_text(encoding="ISO-8859-1"), encoding="utf8")

    print(' ')

for root, dirs, files in os.walk(infilepath):
    for filename in files: 
        if filename[-5:] == '.java': # Controle de tipo de arquivo
            loadfile(filename)