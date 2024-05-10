# import  libraries
import pandas as pd # for working with dataframes
import numpy as np # for working with arrays and creating some visualisations and calculations
import matplotlib.pyplot as plt # for plotting 
import seaborn as sns # for some visualisations

data = pd.read_csv("/Users/katelisovenko/Yandex.Disk.localized/kate/springboard/pands_project/iris/iris.data", names=['sep_length', 'sep_width', 'pet_length','pet_width','class'])

with open("variable_summary.txt", "w") as f:
    for column in data:
        f.write(f"Summary description for {column}:\n\n") 
        f.write(str(data[column].describe()) + "\n\n")
        f.write("************************************ \n")
       
    
    

with open("variable_summary.txt", "a") as f:
    f.write("The summary contains the statistical information about each of the variables.")
    f.write("\n")
f.close()
    
# creating histograms:

 
def plot_hist_hue(data, column, hue):  
    sns.histplot(data=data, x= data[column], hue = hue , multiple = 'dodge')
    plt.title(f'Comparative distribution of {column}')
    plt.xlabel(f'{column},mm')
    plt.ylabel('Frequency')

fig, axs = plt.subplots(4, 1, figsize=(20, 20))  
plt.subplot(4,1,1)
plot_hist_hue(data=data, column = 'sep_length', hue = 'class')

plt.subplot(4,1,2)
plot_hist_hue(data=data, column = 'sep_width', hue = 'class')

plt.subplot(4,1,3)
plot_hist_hue(data=data, column = 'pet_length', hue = 'class')

plt.subplot(4,1,4)
plot_hist_hue(data=data, column = 'pet_width', hue = 'class')


plt.tight_layout()
plt.savefig('histograms.png')
plt.close()

# adding scatterplots:

with open ('sactterplot.png', 'wb') as f:
    
    sns.pairplot(data, hue='class',diag_kind="hist", corner=True, height=1.8)
    plt.suptitle('Correlation between the variables and distribution histograms')
    plt.savefig(f)
f.close()    