import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
#reading the data from file
def readFile(filename, range_s, range_e, col):
	stockData = pd.read_csv(filename+'.csv')
	stockIndicator = []
	dateData = []
	for i in range(range_s,range_e):
		stockIndicator.append([(stockData.values[i,j]) for j in range(col, col+1)])
		dateData.append([(stockData.values[i,j]) for j in range(0, 1)])
	return dateData, stockIndicator
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
#Plot Stock Prices Data with Moving Averages
def PlotStock(stockName):
	#Reading Closing prices from the Stock
	date, indicator = readFile(stockName,0,148,4)
	#print(date[0][0])
	PDateC = Data(date)
	PIndicatorC = Data(indicator)
	#Reading Moving Average of Period of 5
	date5_p, indicator5_p = readFile(stockName,4,148,7)
	PDate5_p = Data(date5_p)
	PIndicator5_p =Data(indicator5_p)
	#Reading Moving Average of Period of 10
	date10_p, indicator10_p = readFile(stockName, 9, 148, 8)
	PDate10_p = Data(date10_p)
	PIndicator10_p =Data(indicator10_p)
	#Reading Moving Average of Period of 20
	date20_p, indicator20_p = readFile(stockName, 19, 148, 9)
	PDate20_p = Data(date20_p)
	PIndicator20_p =Data(indicator20_p)
	#Reading Moving Average of Period of 50
	date50_p, indicator50_p = readFile(stockName, 49, 148, 10)
	PDate50_p = Data(date50_p)
	PIndicator50_p =Data(indicator50_p)
	#Plot all the Moving Average Data, 5 days, 10 days, 20 days, and 50 days period
	fig, ax = plt.subplots(figsize=(40,5))
	ax.plot(PDateC,PIndicatorC, label = "Closing Price")
	ax.plot(PDate5_p,PIndicator5_p, label = "5_p")
	ax.plot(PDate10_p,PIndicator10_p, label = "10_p")
	ax.plot(PDate20_p,PIndicator20_p, label = "20_p")
	ax.plot(PDate50_p,PIndicator50_p, label = "50_p")
	ax.set_ylabel('Stock Prices')
	ax.set_xlabel('Date')
	ax.set_title(stockName+' Stock Prices')
	fig.autofmt_xdate()
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
	plt.setp(ax.get_xticklabels(), rotation=90, fontsize=7.5)
	plt.legend(loc='upper left')
	plt.subplots_adjust(left=0.04, right=0.992, top=0.90, bottom=0.20)
	plt.show()
#Plotting the data for RSI according to each stock
def PlotRSI(stockName):
	#reading in the file
	date, RSIindicator = readFile(stockName,10,148,13)
	dateR = Data(date)
	indR = Data(RSIindicator)
	#Plotting the RSI Indicator
	fig, ax = plt.subplots(figsize=(40,5))
	ax.plot(dateR,indR)
	ax.set_xlabel('Date')
	ax.set_title(stockName+' RSI Indicators')
	#Indicator for overbought and oversold
	ax.axhline(y=30, color='r', linestyle='dashed')
	ax.axhline(y=70, color='r', linestyle='dashed')
	fig.autofmt_xdate()
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
	plt.setp(ax.get_xticklabels(), rotation=90, fontsize=7.5)
	plt.subplots_adjust(left=0.04, right=0.992, top=0.90, bottom=0.20)
	plt.show()
#MACD Signal Plot
def MACDPlot(stockName):
	#Reading in the data from Excel for plotting 
	dateS, SignalI = readFile(stockName,0,148,17)
	dateMACD, MACD = readFile(stockName,0,148,16)
	date = Data(dateS)
	signal = Data(SignalI)
	macd_signal = Data(MACD)

	fig, ax = plt.subplots(figsize=(40,5))
	ax.plot(date,signal, label ='Signal Line')
	ax.plot(date,macd_signal, label= 'MACD')
	#ax.hist(date, bins = macd_hist)
	ax.set_xlabel('Date')
	ax.set_title(stockName+' MACD Indicators')
	#Indicator for overbought and oversold
	ax.axhline(y=0, color='r', linestyle='dashed')
	fig.autofmt_xdate()
	plt.legend(loc='upper left')
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
	plt.setp(ax.get_xticklabels(), rotation=90, fontsize=7.5)
	plt.subplots_adjust(left=0.04, right=0.992, top=0.90, bottom=0.20)
	plt.show()
#------------------------------------OLAP operation (Drill-Up)------------------------------------
def PlotDrillUpStockPrice(stockName):
	date, stockP = readFile(stockName,150,157,4)
	date = Data(date)
	SP = Data(stockP)

	date5_p, indicator5_p = readFile(stockName,150,157,7)
	PDate5_p = Data(date5_p)
	PIndicator5_p =Data(indicator5_p)
	#Reading Moving Average of Period of 10
	date10_p, indicator10_p = readFile(stockName, 150, 157, 8)
	PDate10_p = Data(date10_p)
	PIndicator10_p =Data(indicator10_p)
	#Reading Moving Average of Period of 20
	date20_p, indicator20_p = readFile(stockName, 150, 157, 9)
	PDate20_p = Data(date20_p)
	PIndicator20_p =Data(indicator20_p)
	#Reading Moving Average of Period of 50
	date50_p, indicator50_p = readFile(stockName, 152, 157, 10)
	PDate50_p = Data(date50_p)
	PIndicator50_p =Data(indicator50_p)
	#Plot all the Moving Average Data, 5 days, 10 days, 20 days, and 50 days period
	fig, ax = plt.subplots(figsize=(40,5))
	ax.plot(date,SP, label = "Closing Price" ,color = 'black')
	ax.plot(PDate5_p,PIndicator5_p, label = "5_p", color ='springgreen')
	ax.plot(PDate10_p,PIndicator10_p, label = "10_p", color = 'pink')
	ax.plot(PDate20_p,PIndicator20_p, label = "20_p", color='aqua')
	ax.plot(PDate50_p,PIndicator50_p, label = "50_p", color = 'orange')
	ax.set_ylabel('Stock Prices')
	ax.set_xlabel('Date')
	ax.set_title(stockName+' Monthly Stock Closing Prices')
	#fig.autofmt_xdate()
	#ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
	#plt.setp(ax.get_xticklabels(), rotation=30, fontsize=7.5)
	plt.legend(loc='upper left')
	#plt.subplots_adjust(left=0.04, right=0.992, top=0.90, bottom=0.20)
	plt.show()
#Drill Up RSI (Summarize DataSet)
def PlotDrillUpRSI(stockName):
	date, RSIindicator = readFile(stockName,150,157,13)
	dateR = Data(date)
	indR = Data(RSIindicator)
	#Plotting the RSI Indicator
	fig, ax = plt.subplots(figsize=(40,5))
	ax.plot(dateR,indR)
	ax.set_xlabel('Date')
	ax.set_title(stockName+' Monthly RSI Indicators')
	#Indicator for overbought and oversold
	ax.axhline(y=30, color='r', linestyle='dashed')
	ax.axhline(y=70, color='r', linestyle='dashed')
	fig.autofmt_xdate()
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
	plt.setp(ax.get_xticklabels(), rotation=90, fontsize=7.5)
	plt.subplots_adjust(left=0.04, right=0.992, top=0.90, bottom=0.20)
	plt.show()
#Monthly MACD Analysis
def PlotDrillUpMACD(stockName):
	#Reading in the data from Excel for plotting 
	dateS, SignalI = readFile(stockName,150,157,17)
	dateMACD, MACD = readFile(stockName,150,157,16)
	date = Data(dateS)
	signal = Data(SignalI)
	macd_signal = Data(MACD)

	fig, ax = plt.subplots(figsize=(40,5))
	ax.plot(date,signal, label ='Signal Line')
	ax.plot(date,macd_signal, label= 'MACD')
	#ax.hist(date, bins = macd_hist)
	ax.set_xlabel('Date')
	ax.set_title(stockName+' Monthly MACD Indicators')
	#Indicator for overbought and oversold
	ax.axhline(y=0, color='r', linestyle='dashed')
	fig.autofmt_xdate()
	plt.legend(loc='upper left')
	ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
	plt.setp(ax.get_xticklabels(), rotation=90, fontsize=7.5)
	plt.subplots_adjust(left=0.04, right=0.992, top=0.90, bottom=0.20)
	plt.show()

#Plotting for all the Stock Prices for Each Semiconductor/Chip Company
"""
PlotStock('TSM')
PlotStock('INTC')
PlotStock('AMD')
#Plotting the RSI Indicators for each stock
PlotRSI('TSM')
PlotRSI('INTC')
PlotRSI('AMD')
#Plotting the MACD Indicators for each stock
MACDPlot('TSM')
MACDPlot('INTC')
MACDPlot('AMD')

#------------------------DAta Aggregation: OLAP Operation-> Drill UP Plot------------------------

PlotDrillUpStockPrice('TSM')
PlotDrillUpStockPrice('AMD')
PlotDrillUpStockPrice('INTC')
#Monthly RSI Indicators
PlotDrillUpRSI('TSM')
PlotDrillUpRSI('AMD')
PlotDrillUpRSI('INTC')
#Monthly MACD Indicators
PlotDrillUpMACD('TSM')
PlotDrillUpMACD('AMD')
PlotDrillUpMACD('INTC')
"""