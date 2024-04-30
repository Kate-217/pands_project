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
    
# creating histograms:


plt.figure(figsize=(18, 12))  

for i, feature in enumerate(data):
    if feature != 'class':# excluding the last column
        # 2 row, 2 col, i+1 means that each iterration it creates new subplot in 
        # the 2x2 grid
        plt.subplot(2, 2, i+1)  
        sns.histplot(data=data, x=data[feature], hue='class', multiple='dodge')
        plt.title(f"Comparative distribution of {feature} across the classes")
        plt.xlabel(f'{feature}, mm')
        plt.ylabel('Frequency')

plt.tight_layout()  # Adjust layout to make sure everything fits without overlapping
plt.savefig('histograms.png')
plt.close()  
          
                
                
    
    
def plot_hist_hue(data, column, hue):
    
    for feature in data[column]:
        plt.figure(figsize=(6,6))
        plot = sns.histplot(data=data, x= data[column], hue = hue , multiple = 'dodge')
        plt.title(f'Comparative distribution of {column}')
        plt.xlabel(f'{column},mm')
        plt.ylabel('Frequency')
        with open('hists.png','+ab') as f:
        #Ensure you have matplotlib installed.
        #Here plt is your matplotlib.pyplot import
            plt.savefig('hists.png')
            plt.close()
plot_hist_hue(data, column= "sep_length", hue = 'class') 
#plot_hist_hue(data, column= "sep_width", hue = 'class')           