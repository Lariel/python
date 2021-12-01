import os;
import sys;
import pathlib;
from pathlib import Path;
from chardet.universaldetector import UniversalDetector;

detector = UniversalDetector()

try:
    infilepath = Path(sys.argv[1])
except IndexError:
    infilepath = pathlib.Path().resolve() #pasta atual

print('Pasta de trabalho: ', infilepath,' e subpastas.')

def loadfile(filename):
    print(' \nCarregando arquivo ', filename)
    
    checkencode(filename)

def checkencode(filename):

    detector.reset()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    fileenconde = detector.result['encoding']
    print('Encode detectado '+ fileenconde)

    if fileenconde == 'ISO-8859-1':
        filepath = Path(filename)
        savefile(filepath)

def savefile(filepath):
    print('Salvando arquivo ', filepath, '\n')
    filepath.write_text(filepath.read_text(encoding="ISO-8859-1"), encoding="utf8")

for pasta, subpastas, arquivos in os.walk(infilepath):
    for filename in arquivos: 
        if filename[-5:] == '.java': # Controle de tipo de arquivo
            loadfile(os.path.join(pasta, filename))