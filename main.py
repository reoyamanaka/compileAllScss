from os import listdir, getcwd, system
from subprocess import call
from utils import checkIfScss, getNameWithoutScssExtension


for file in listdir ():
    if checkIfScss (file):
        nameWithoutScssExtension = getNameWithoutScssExtension (file)
        outputName = file.replace (".scss", ".css")

        system (f"sass {file} {file.replace ('.scss', '.css')}") 

