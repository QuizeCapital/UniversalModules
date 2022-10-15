import json
import pandas as pd   
import numpy as np


class modulesSmartFactor():
    
    def __init__(self):
        pass
    
    '''
    Open JSON file
    '''
    def openJson(self, jsonFileLink):
        with open(jsonFileLink) as file:
            return  json.load(file)
        
        
    '''
    dumping data into json Files
    '''
    def dumpJson(self, uploadLink, uploadData):
        with open(uploadLink, 'w') as file:
            file.write(json.dumps(uploadData))
            
                
    '''
    Open CSV file
    '''
    def openCsv (self, csvFileLink, delimiter = " "):
       
        return pd.read_csv(csvFileLink)
    
    '''
    This function calculates the annual growth rate using a linked return method 
    ie. returns that have been multiplied by each other to create a compound return.
    The returns are compounded for the end of the investment period ie. the  portofolio is 
    assumed to be rebalanced at this period eg. quarterly, annually etc.
    Fomula for linked returns is : 
    linked return^t = (r^t * r^t-1)
    linked return^t+1 = linked return^t * r^t+1
    total linked return = linked return^tfinal -1
    where r  is the annual return /log annual return
    
    CAGR = (total linked return)^1/t
    where t is the number of periods
    
    This function takes a dataframe/series as inputs and returns a CAGR value
    '''

    def compoundedAnnualGrowthRate(self, dataSet):
        
        cummulativeReturn = (dataSet.cumprod())
        #totalCummulativeReturn = (cummulativeReturn.iloc[-1])-1
        #totalCummulativeReturn = (cummulativeReturn.tail(1))-1
        print(cumm)
        try:
        #suppose that number2 is a float
            return ((cummulativeReturn.tail(1))**(1/len(dataSet)))-1
        except ZeroDivisionError:
            return None

        #return ((cummulativeReturn.iloc[-1])**(1/len(dataSet)))-1
        return ((cummulativeReturn.tail(1))**(1/len(dataSet)))-1

        #return cummulativeReturn
    
    '''
    This python decorator is created to add the dollar sign 
    before outputs of functionns
    '''
    # Decorator function
    def dollarDecorator(fn):
        def add_dollar(*args, **kwargs):
            return '$' + str(fn(*args,**kwargs))
        return add_dollar
    
    
    '''
    This functions calculates the dollar value return on investments 
    given a particular CAGR. It uses the standard time value of future investments formula :
    FV = I*(1+r/n)^(n*t)
    This function takes the principal, compunding frequency, total time of investments and annual
    growth of returns as inputs.
    It returns the dollar value of return on investments
    '''
    @dollarDecorator
    def valueOfXInvestedWithoutDividends(self, principal,compoundingFrequency, time, CAGR):
        
        return principal*(
            (1+
             (CAGR/compoundingFrequency))
            **(time*compoundingFrequency)
            )
    
    ''''
    This function calculates  the mean return when rolling three-year periods that the 
    strategy outperforms the Universe. That is, if an investor followed the 
    strategy for three consecutive years, what percentage of times would the 
    investor outperform the Universe?
    This functio takes a dataframe as inputs and returns another dataframe as with 
    rolling mean column as output. 
    N.B The dataframe has to contain a dat as index for it work.
    '''
    def threeYearRollingReturn(self, df):
        
        return df.rolling(3, min_periods=1).mean()
        
        
        