import csv
import pandas as pd
from os.path import isdir,expanduser
import configparser

"""
Read config File and Create CSV based on parameters. Also have the option of updating ini file here if you wish!
"""
parser = configparser.ConfigParser()
parser.read("settings.ini")
#Set input csv file

#Set place where resulting CSV will be output
outpath = parser.get('Output_Csv','path')

#Set some custom values here
parser.set("Optional_Values","Column_to_Column","policyID,county")
parser.set("Optional_Values","Values","mean,count")
parser.set("Optional_Values","Method","describe")
parser.set("Output_Csv","file_name","Datasheet.csv")
parser.set("Optional_Values","query","county=='CLAY COUNTY'")

#Declare variables outside of the function so you can pass them in later if needed
mypath = parser.get('Input_Csv', 'path')
mycolumns = parser.get('Optional_Values','Column_to_Column')
myvalues = parser.get('Optional_Values','Values')
method = parser.get('Optional_Values','Method')
myfile = parser.get('Output_Csv','file_name')
myquery = parser.get('Optional_Values','query')

#Open ini file and save the updated settings to the file
with open("./settings.ini", "w") as config_file:
    parser.write(config_file)

#Default behaivor is to return a CSV if a method is not specified, otherwise executes based off method given.
"""
Path: Must Be Given
Filename: Optional but if not passed will not print to a csv
panda_values: Used for the describe along with the other than describe function
specific: Used with the check_where_equal method for querying
method: used to specify which function you want to use
"""
def executepandas(path,output_path="",filename="",panda_values="",excel_columns="",specific="",method=""):
    
    #Load dataframe object
    data = pd.read_csv(path)
    dataframe = pd.DataFrame(data)


    if method =="specific_columns":

        #Take columns from the config file and make them into a list to be used later
        try:
            col_list= excel_columns.split(",")
            headers=col_list
            dataframe.to_csv(filename, columns=headers)
            print("Success")
            return

        except:
            print("Fatal Error. Please try again")
            return
    
    elif method == "check_where_equal":

        try:
            dataframe=dataframe.query(specific)
            dataframe.to_csv(filename)
        
        except:

            print("Fatal Error. Please try again")
            return           

    elif method =="describe":
        try:
            #Take values from config and put them in the correct format to be evaluated
            my_values = panda_values.split(",")
            dataframe=dataframe.describe().loc[my_values]
            dataframe.to_csv(filename)
            print("Success!")
        
        except:
            print("Fatal Error. Please try again")
            return 
    
    elif method == "between":

        try:
            #For now this method only supports between two columns (eg ColA:ColE)
            columns= excel_columns.split(",")
            column_A = columns[0]
            column_B = columns[1]

            #Get all columns between the two given (inclusive)
            dataframe=dataframe.loc[:, column_A:column_B]
            dataframe.to_csv(filename)
            return

        except:
            print("Fatal Error. Please try again")
            return
    
    elif method == "aggregate":

        try:
            columns= excel_columns.split(",")
            dataframe = dataframe.groupby(columns).first()
            dataframe.to_csv(filename)
            return
        
        except:

            print("Fatal Error. Please try again")
            return     

    #This method is mainly for getting sum, mean, median, etc since those are not included in describe
    elif method =="other_than_describe":

        try:
            columns= excel_columns.split(",")
            my_values = panda_values.split(",")
            dataframe = dataframe.groupby(columns).agg[my_values]
            dataframe.to_csv(filename)

        except:

            print("Fatal Error. Please try again")
            return 
    else:
        dataframe.to_csv(filename)
        return

#Test run
executepandas(mypath,output_path=outpath,filename=myfile, panda_values=myvalues,excel_columns=mycolumns,method=method)

