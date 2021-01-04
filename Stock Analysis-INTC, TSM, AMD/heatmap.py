import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
#reading the data from file
def readFile(filename, range_s, range_e, col):
	stockData = pd.read_csv(filename+'.csv')
	stockIndicator = []
	for i in range(range_s,range_e):
		stockIndicator.append([(stockData.values[i,j]) for j in range(col, col+1)])
	return stockIndicator
#Changing list within a list data read from the excel into a list
def Data(data):
	resData = []
	index  = 0
	res = 0
	while index < len(data):
		res = data[index][0]
		resData.append(res)
		index = index + 1
	return resData
#Obtaining Data for heat map
def gatherData(filename):
	#Gathering data/indicators from each excel file
	close = Data(readFile(filename, 0, 148, 4))
	volume = Data(readFile(filename, 0, 148, 5))
	RSI = Data(readFile(filename, 10, 148, 13))
	signal = Data(readFile(filename,0,148,17))
	MACD = Data(readFile(filename,0,148,16))
	return close, volume, RSI, signal, MACD

#Gathering data for each stock
TSM_Cl, TSM_V, TSM_RSI, TSM_Sig, TSM_MACD = gatherData('TSM')
AMD_Cl, AMD_V, AMD_RSI, AMD_Sig, AMD_MACD = gatherData('AMD')
INTC_Cl, INTC_V, INTC_RSI, INTC_Sig, INTC_MACD = gatherData('INTC')
#Converting the data into data frame for generating heat map later
df = pd.DataFrame(list(zip(TSM_Cl, TSM_V, TSM_RSI, TSM_Sig, TSM_MACD,
	AMD_Cl, AMD_V, AMD_RSI, AMD_Sig, AMD_MACD, INTC_Cl, INTC_V, INTC_RSI,
	INTC_Sig, INTC_MACD)), columns = ['TSM Closing Prices', 'TSM Volumes', 'TSM RSI', 'TSM Signals', 'TSM MACD',
									   'AMD Closing Prices', 'AMD Volumes', 'AMD RSI', 'AMD Signals', 'AMD MACD',
									   'INTC Closing Prices', 'INTC Volumes', 'INTC RSI', 'INTC Signals', 'INTC MACD'])																		
#Generating Heat map
fig, ax = plt.subplots(figsize=(20,8))
sns.heatmap(df.corr(), annot = True , ax=ax, cmap="YlGnBu")
plt.subplots_adjust(left=0.15, right=1.0, top=0.90, bottom=0.20)
plt.show()