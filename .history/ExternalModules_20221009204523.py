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
    
    CAGR = (total linked return)^ 
    '''
    def compoundedAnnualGrowthRate (self):
        
        
        
    # Return the quintile of market cap and y-axis
    # titles of plots ie. limits of quintiles gotten 
    # by last market  cap value in quintile
    # '''
    # def splitMarketDataAndMarketCapLimits(self, marketDataFile):
        
    #     originalMarketDataFile = self.openCsv(marketDataFile)
    #     groupedMarketCapTickers = originalMarketDataFile.sort_values(['MarketCap'], ascending=[False,])
    #     splitFiveWaysByMarketValue= np.array_split(groupedMarketCapTickers, 5)
        
    #     listLimitMarketCaps = ['>'+str("{:,}".format(dataframe['MarketCap'].iloc[-1])) for dataframe in splitFiveWaysByMarketValue]
        
    #     quintileTickersAndLimits ={listLimitMarketCaps[num] : splitFiveWaysByMarketValue[num] for num in range(len(splitFiveWaysByMarketValue))}
        
    #     return quintileTickersAndLimits
    
    
    # '''
    
    # '''
    # def janeDoe(self, dfVertical, verticalSize, dfHorizontal, horizontalSize):
        
    # splitVertical = np.array_split(dfVertical, verticalSize)
        # splitHorizontal = np.array_split(dfHorizontal, horizontalSize)
        
        
          

    

#splitPrint = objectTwo.splitMarketDataAndMarketCapLimits('/Users/adamszequi/SmartFactor/Smart-Factor-Research-Files-5/Master Dataset File/marketCapDataCleaned.csv')
#pathReturns = '/Users/adamszequi/SmartFactor/Smart-Factor-Research-Files-5/RevenuePerShare/returnsData.json'

#print(splitPrint)

