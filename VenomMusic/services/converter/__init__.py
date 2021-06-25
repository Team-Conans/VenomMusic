from os import listdir, mkdir

if "raw_files" not in listdir():

    mkdir("raw_files")

from VenomMusic.services.converter.converter import convert
