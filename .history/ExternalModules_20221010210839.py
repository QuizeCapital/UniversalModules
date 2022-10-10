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
    This functions calculates the dollar value return on investments 
    given a particular CAGR. It uses the standard time value of future investments formula 
    
    FV = I*(1+R
    '''
    def valueOfXInvestedWithoutDividends(self, principal, CAGR):
        
        