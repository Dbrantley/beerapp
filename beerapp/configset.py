import csv
import pandas as pd
from os.path import isdir,expanduser
import configparser

"""
Create a config file
"""
def createconfig():

        #Specified the file I want to process here but can be changed in the main if needed!
        config = configparser.ConfigParser()
        config.add_section("Input_Csv")
        config.set("Input_Csv", "path","C:\\Users\\Damien\\Downloads\\FL_insurance_sample\\FL_insurance_sample.csv")

        #Makes it so the output path is inside of the user's mydocuments folder by default
        config.add_section("Output_Csv")
        config.set("Output_Csv", "path",expanduser("~/Documents"))
        config.set("Output_Csv", "file_name","Data.csv")

        config.add_section("Optional_Values")

        #Ini Default settings
        config.set("Optional_Values", "Column_and_Column_Values","")
        config.set("Optional_Values", "Column_to_Column_Values","")
        config.set("Optional_Values", "Columns","")
        config.set("Optional_Values","Values","")

        #Methods are specified in the main. Possibly not needed but wanted to make sure every function executed correctly!
        config.add_section("Method")
        config.set("Method", "Method","")


        with open("./settings.ini", "w") as config_file:
                config.write(config_file)

#Initialize config settings
createconfig()