import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    '''
    Here, we create a dataframe using a python list.
    Essentially, we call the constructor of the DataFrame class to
    instantiate our object.
    '''
    simpleList = [
                   ['Katerina', 'Constantinos'],
                   ['Gae', 'Dimitra'],
                   ['Sandy','Mitsos'],
                   ['Panagiotis', 'Tim'],
                   ['George'],
                 ]

    frameObject1 = pd.DataFrame(simpleList)

    print(frameObject1)
    print(frameObject1[0][1])
    print('\n')

    '''
    Here, we create a dataframe using a python dictionary.
    '''
    simpleDict = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
                  'Age' : ['27', '24', '22', '32'],
                  'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannuj'],
                  'Qualification': ['MsC', 'MA', 'MBA', 'PhD']
                 }

    frameObject2 = pd.DataFrame(simpleDict)
    print(frameObject2)

    # We can isolate and work on specific columns of our data frame
    print(frameObject2[['Name', 'Address']])

    # We can easily check the dimensions and size of our data frame using the 'size' and 'shape' attributes.
    print("frameObject2 has " + str(frameObject2.size) + " elements")
    print("frameObject2 has shape: ")
    print(frameObject2.shape)
    print('\n')

    '''
    Here, we create a dataframe importing data from csv file.
    '''
    frameObject3 = pd.read_csv("files/nba.csv")
    print(frameObject3)

    # We can use the following commands to see the first and last rows of the frame, respectively.
    print(frameObject3.head())
    print(frameObject3.tail())

    number_of_rows = frameObject3.shape[0]
    number_of_cols = frameObject3.shape[1]

    # We can extract specific rows and columns from our data frame.
    column1 = frameObject3.iloc[:,0]
    column2 = frameObject3.loc[:,'Salary']
    rows    = frameObject3.iloc[range(440,451), range(0,number_of_cols)]

    print(column1)
    print(column2)
    print(rows)

    # Pandas dataframe objects support the 'plot' method of matplotlib.
    frameObject3.plot(x = 'Name', y = 'Salary', color = 'purple', marker = '.', linestyle = 'dotted')
    plt.show()
    print('\n')

    '''
    Another example.
    '''
    myList = [ [2, 'Catherine', 22], [1, 'Constantinos', 25], [3, 'Panos', 24] ]

    # When creating the frame, we can specify the title of each column.
    frameObject4 = pd.DataFrame(myList, columns = ['id', 'name', 'age'])
    print(frameObject4)
    print('\n')

    '''
    We can create a new dataframe using an existing dataframe which can be modified in various ways.
    '''
    frameObject5 = frameObject4.set_index('id')
    print(frameObject5)

    # We can also sort the rows of our dataframe with various ways.
    print(frameObject5.sort_index())
    print(frameObject5.sort_values(by = ['age']))
    print(frameObject5.sort_values(by = ['name']))

    # We can also export our dataframe to a csv or xlsx file.
    frameObject5.to_csv('./log/dataframe.csv')
    frameObject5.to_excel('./log/dataframe.xlsx')

if __name__ == "__main__":
    main()
