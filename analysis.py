# import  libraries
import pandas as pd # for working with dataframes
import numpy as np # for working with arrays and creating some visualisations and calculations
import matplotlib.pyplot as plt # for plotting 
import seaborn as sns # for some visualisations

data = pd.read_csv("/Users/katelisovenko/Yandex.Disk.localized/kate/springboard/pands_project/iris/iris.data", names=['sep_length', 'sep_width', 'pet_length','pet_width','class'])

with open("variable_summary", "w") as f:
    for column in data:
        f.write(f"Summary description for {column}:\n\n") 
        f.write(str(data[column].describe()) + "\n\n")
        f.write("************************************ \n")
    
    

with open("variable_summary", "a") as f:
    f.write("The summary contains the statistical information about each of the variables.")