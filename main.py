from os import listdir, getcwd
from subprocess import call
from checkIfScss import checkIfScss


for file in listdir ():
    if checkIfScss (file):

