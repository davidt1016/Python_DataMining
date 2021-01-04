'''
Top indicators :

1. VWAP
	- Volume * Close 
	- Sum of 13 days close price / sum of total volume  or  sum of total 20 days / sum of total volume

2. RSI-

'''
import matplotlib.pyplot as plt
import numpy as np
#import yahoo
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas_datareader as web
from datetime import date
import pandas as pd


#date_list, price, volume= yahoo.get_history('AC.TO')
ticker = input("ticker: ")
start = '2020-01-01'
today = date.today()
df = web.DataReader(ticker, data_source='yahoo', start=start, end=today)

def Moving_Avg(price, n):
	rolling_mean = price.rolling(window=n).mean()
	print(rolling_mean)
	return rolling_mean

def WVAP(price, volume):
	price = np.array(price,dtype=float)
	volume = np.array(volume,dtype=float)
	price_x_volume = price*volume
	wvap_list_1 = []
	wvap_list_2 = []
	i = len(price_x_volume) 
	while i > 0:
		sum_volume_1 = np.sum(volume[i-20:i])
		sum_price_volume_1 = np.sum(price_x_volume[i-20:i])
		wvap_1 = sum_price_volume_1/sum_volume_1
		wvap_list_1.append(wvap_1)


		sum_volume_2 = np.sum(volume[i-60:i])
		sum_price_volume_2 = np.sum(price_x_volume[i-60:i])
		wvap_2 = sum_price_volume_2/sum_volume_2
		wvap_list_2.append(wvap_2)
		i-=1
	df['WVAP_1'] = wvap_list_1[::-1]
	df['WVAP_2'] = wvap_list_2[::-1]

	return wvap_list_1, wvap_list_2


def RSI(price, n=10):
    delta = price.diff()
    #-----------
    dUp, dDown = delta.copy(), delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0
    RolUp = dUp.rolling(n).mean()
    RolDown = dDown.rolling(n).mean().abs()
    rsi= 100-100/(1+RolUp/RolDown)
    df['RSI'] = rsi
    return rsi


def MACD(price):
	exp1 = price.ewm(span=12, adjust=False).mean()
	exp2 = price.ewm(span=26, adjust=False).mean()
	macd = exp1-exp2
	signal = macd.ewm(span=9, adjust=False).mean()
	df['12'] = exp1
	df['26'] = exp2
	df['MACD'] = macd
	df['Signal'] = signal
	#df['Histogram'] = macd - signal
	return macd, signal

def slope_calculation(price, wvap_list_1, wvap_list_2):
	price = np.array(price,dtype=float)
	#print(price)
	price_difference = []
	wvap_list_1_difference = []
	wvap_list_2_difference = []
	i = len(price)-1
	while i > 0:
		#print(price[i])
		difference=price[i]-price[i-1]
		wvap_1_difference=wvap_list_1[i]-wvap_list_1[i-1]
		wvap_2_difference=wvap_list_2[i]-wvap_list_2[i-1]
		price_difference.append(difference)
		wvap_list_1_difference.append(wvap_1_difference)
		wvap_list_2_difference.append(wvap_2_difference)
		
		
		i-=1
	return price_difference, wvap_list_1_difference, wvap_list_2_difference


def add_to_df(data, name):
	df[name] = data
'''
def plot():
	gs = gridspec.GridSpec(4, 1)
	plt.figure()
	ax = plt.subplot(gs[0:2, 0]) # row 0, col 0
	
	plt.ylabel('Price', fontsize=18)
	plt.plot(df['Close'])
	plt.plot(df['12'])
	plt.plot(df['26'])
	plt.plot(df['WVAP_1'])
	plt.plot(df['WVAP_2'])
	plt.legend(['Price','12','26','WVAP_20','WVAP_60'], loc='upper left')

	ax = plt.subplot(gs[2, 0]) # row 0, col 1
	plt.plot(df['RSI'])
	plt.axhline(y=70, color='r', linestyle='-')
	plt.axhline(y=30, color='r', linestyle='-')
	plt.legend(['RSI'], loc='upper left')

	ax = plt.subplot(gs[3, 0]) # row 1, span all columns
	plt.plot(df['MACD'])
	plt.plot(df['Signal'])
	#plt.plot(df['Histogram'])
	plt.legend(['MACD','Signal'], loc='upper left')
	#plt.plot(df['RSI'])
	
	plt.show()

'''


day_5 = Moving_Avg(df['Close'], 5)
day_10 = Moving_Avg(df['Close'], 10)
day_20 = Moving_Avg(df['Close'], 20)
day_50 = Moving_Avg(df['Close'], 50)
#print(20_day
add_to_df(day_5, '5_p')
add_to_df(day_10, '10_p')
add_to_df(day_20, '20_p')
add_to_df(day_50, '50_p')

diff = df['20_p'] < df['50_p']
print(diff)
diff_forward = diff.shift(1)
crossing = np.where(abs(diff - diff_forward) == True)[0]
#print(crossing)
print(df.iloc[crossing])

wvap_list_1, wvap_list_2 = WVAP(df['Close'], df['Volume'])
rsi = RSI(df['Close'])
macd, signal_line = MACD(df['Close'])

#plot()


####df.reset_index(level=0, inplace=True)
df = df.round(3)
df.to_csv(ticker+'.csv')




#--------------------------------------------------------------
i = 0 
price = df['Close']


'''
temp = 0
indication = []
while i < len(price):
	try:
		difference=price[i+1]-price[i]
		if difference > temp and 
			print(str(price[i+1])+" ,"+ str(price[i]))
			print("buy")
		else:
			print(str(price[i+1])+" ,"+ str(price[i]))
			print("down")
		temp = difference
	except IndexError:
		break
	i+=1
'''


