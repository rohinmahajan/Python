#read data from a file csv
import pandas as pd
x = pd.read_csv("I:\\GitContent\\SparkApps\\ScalaApps\\Spark_Scala\\SparkApplicationsSetup\\Samplefiles\\Bank_full.csv")
#view the dataset shape
print(x.shape)
print(x.head)
#view all columns in dataset
print(x.columns)
#create a new DF with only required columns
y = x[['age','y']]
#view type of object
print(type(y))

#to read data from a excel file
#excel_file='I:\\Trainings\\MyContent\\Books\\resources\\movie.csv'
#movies = pd.read_excel(excel_file)
#print(movies.columns)


