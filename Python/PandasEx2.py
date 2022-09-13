import pandas as pd

class main:
    def __init__(self,filename):
        self.df=pd.read_csv(filename)
    def briefInfo(self):
        print('Total records {}',len(self.df))
        print('Columns are',self.df.columns)
    def UniqueVals(self,Col):
        print('Unique values are ',self.df[Col].unique())


var1=main('E:\Downloads\RepPivot.csv')
var1.briefInfo()
var1.UniqueVals('GeographicLocationID')