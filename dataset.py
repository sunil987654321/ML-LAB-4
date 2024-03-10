import pandas as pd
import numpy as np

classes= pd.read_csv('C:\\Users\\harshith.m\\PycharmProjects\\ml\\venv\\Malayalam_Char_Gabor.csv')
column_data = classes.iloc[:, 1:]

def mean_and_sandarddeviation(classes,column_data):
    mean1=np.mean(classes)
    for column_name, class_data in column_data.items():
        mean=np.mean(class_data)
        print("mean of class ",column_name," in the csv file is = ", mean)
        std=np.std(class_data)
        print("standard deviation of the class ",column_name,"is = ", std)

mean_and_sandarddeviation(classes,column_data)
