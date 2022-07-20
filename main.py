from os import listdir, getcwd, system, walk
from subprocess import call
from utils import checkIfScss, getNameWithoutScssExtension


for root, dirs, files in walk (getcwd ()):
    for fileName in files: 
        # print (f"fileName: {fileName}")
        if checkIfScss (fileName):
            print (f"Compiling SCSS file with name: {fileName}")
            nameWithoutScssExtension = getNameWithoutScssExtension (fileName)
            outputName = fileName.replace (".scss", ".css")

            system (f"sass {root}/{fileName} {root}/{fileName.replace ('.scss', '.css')}") 
