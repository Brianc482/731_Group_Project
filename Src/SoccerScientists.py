import pandas as pd

#Reading in the datasets
first = pd.read_csv("https://raw.githubusercontent.com/Brianc482/731_Group_Project/main/Data/2015-2016.csv")
second = pd.read_csv("https://raw.githubusercontent.com/Brianc482/731_Group_Project/main/Data/2016-2017.csv")
third = pd.read_csv("https://raw.githubusercontent.com/Brianc482/731_Group_Project/main/Data/2017-2018.csv")
fourth = pd.read_csv("https://raw.githubusercontent.com/Brianc482/731_Group_Project/main/Data/2018-2019.csv")

#Dropping a constant column that only appears in two of the
#data sets
third.drop(["Div"],axis=1,inplace=True)
fourth.drop(["Div"],axis=1,inplace=True)

#Creating a frame to hold the data sets and concatenating
#into a single larger set
frame = [first, second, third, fourth]
df = pd.concat(frame)

#Cleaning up the datetime format so that all appear the same
df['Date'] = pd.to_datetime(df.Date)
df['Date'] = df['Date'].dt.strftime('%m-%d-%Y')
df.sort_values('Date')

#Displaying the transformed data set and some information
print(df)

print("\nLet's see if there are any N/A values to drop.")
dropped_df = df.dropna()
print("The value should read \'True\' if there are no N/A values: ", df.equals(dropped_df))


print("\nThe list of keys are as follows:\n")
print(df.keys())

print("\nA statistical description of our data:\n")
print(df.describe())




