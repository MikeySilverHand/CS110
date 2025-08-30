#Michael Hernandez
#Computer Science
#I hope to learn more about data science since I only have some experience in High school

import numpy as np
import pandas as pd
import matplotlib.pyplot

print(np.__version__)
print(pd.__version__)
print(matplotlib.__version__)
                  
#It finds the mean and standard deviation, its parameters are the array, it returns the mean and standard deviattion                  
def calculate_stats(number):
    mean = np.mean(number)
    std = np.std(number)

    return mean, std

number = np.array([1,4,5,6,3,12,24,6,21,122,52,62,73])

mean, std = calculate_stats(number)

print(f"Mean: {mean:.2f}, Standard Deviation: {std:.2f}")

#Dataset Name: International Piano competition 

#Source:https://www.kaggle.com/datasets/leesstephanie/international-piano-competitions/data  

#Description: It is a data set that shows an internation piano competitions competitors, including their age, gender, profile link, competition name, stage name, stage number, date, order stage, order day 

#Potential Questions:  
#What was the name of the winner? 
#Where can I access the winners profile link to view more information about them? 