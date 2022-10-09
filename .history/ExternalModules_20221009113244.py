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
    This func
    '''
    def johnDoe
    # '''
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

