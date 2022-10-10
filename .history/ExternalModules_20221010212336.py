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
        totalCummulativeReturn = (cummulativeReturn.iloc[-1])-1

        return ((cummulativeReturn.iloc[-1])**(1/len(dataSet)))-1
    
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
    given a particular CAGR. It uses the standard time value of future investments formula 
    
    FV = I*(1+r^n/t)^(n*t)
    
    
    '''
    @dollarDecorator
    def valueOfXInvestedWithoutDividends(self, principal,compoundingFrequency, time, CAGR):
        
        return principal*(
            (1+
             (CAGR/compoundingFrequency))
            **(time*compoundingFrequency)
            )
        
        
        
        