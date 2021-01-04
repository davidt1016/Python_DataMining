
#Importing all the required Python libraries for tokenizing
import pandas as pd
import re
import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import spacy
import numpy as np
import random
from PIL import Image 
import matplotlib.image as mpimg


#--------------------------Removing URL Punctuation-------------------------- 
def remove_url_punctuation(X):

	url_pattern = re.compile(r'https?://\S+|www\.\S+')
	replace_url = url_pattern.sub(r'',str(X))
	punct_pattern = re.compile(r'[^\w\s]')
	no_punct = punct_pattern.sub(r'', replace_url).lower()

	return no_punct

#--------------------------Splitting tweets into word--------------------------
def split_words(X):

	split_word_list = X.split(" ")

	return split_word_list

#--------------------------Removing stop words--------------------------
def remove_stopwords(X):

	global stop_words
	words = []
	for word in X:
		if word not in stop_words and len(word) > 2 and word != 'nan':
			words.append(word)

	return words

#--------------------------Removing other language using langdetect--------------------------
def detect_language(X):

	from langdetect import detect, DetectorFactory
	#To avoid Inconsistent len(Unique_Word_List)
	DetectorFactory.seed = 0
	try:
		lang = detect(X)
		return(lang)
	except:
		return ("other")

#--------------------------Loading Tweet Text File--------------------------
columns = ['id', 'text']
df = pd.read_csv('/Users/davidteng/Desktop/D1.txt', names = columns, sep="\t", lineterminator = '\n', error_bad_lines = False )
df.head()
#--------------------------Removing Punctuation, special characters in tweets--------------------------
df['tidy_tweet'] = df['text'].apply(remove_url_punctuation)
#print(df['text'].head())
#print("-----------------------------")
#print(df['tidy_tweet'].head)

#--------------------------Retaining only tweets in English--------------------------
df['en'] = df['tidy_tweet'].apply(detect_language)
#print(df['tidy_tweet'].head(10))
#print("-----------------------------")
df=df[df['en'] == 'en']
#print(df['tidy_tweet'].head(10))

#--------------------------Tokenizing Tweets--------------------------
df['word_list'] = df['tidy_tweet'].apply(split_words)
df['word_list'].head(5)

#--------------------------Remove stop words using NLTK, such as I, the , a, and, etc.--------------------------
global stop_words
stop_words = set(stopwords.words('english'))
df['nlp_tweet'] = df['word_list'].apply(remove_stopwords)
#print(df['word_list'].head(5))
#print("-----------------------------")
#print(df['nlp_tweet'].head(5))

#--------------------------Creating a list of unique words--------------------------
all_words_unique_list = (df['nlp_tweet'].explode()).unique()
#Output the length of unique words
print(len(all_words_unique_list))

word_list = list(df['nlp_tweet'].explode())
#print("WORD LIST HERE")
#print(word_list)
#Constructs a list of unique words along with its occurence frequencies in the tweets
word_count_dict = collections.Counter(word_list)

#--------------------------Computing normalized frequency count-------------------------- 
normalized_count = {}
for k, v in word_count_dict.items():
	normalized_count[k] = v/len(df['nlp_tweet'])

#Frequency Distribution of each unique word
nltk_count = nltk.FreqDist(word_list)
#print(word_count_dict.most_common(100))
#print("--------------------------------------------------------")


#-------------------------Manual Filtering out data for Data Set 1--------------------------
#nltk_count.pop('100000')
del nltk_count['100']
del nltk_count['could']
del nltk_count['hes']
del nltk_count['dont']
del nltk_count['doesnt']
del nltk_count['also']
del nltk_count['isnt']
del nltk_count['youre']
del nltk_count['thats']
del nltk_count['covid19']
del nltk_count['must']
del nltk_count['ive']
del nltk_count['ill']
del nltk_count['aint']
del nltk_count['times']
del nltk_count['eid']
del nltk_count['cant']
del nltk_count['years']
nltk_count['year'] =17
nltk_count['time'] = 21
nltk_count['covid'] = 10
#Manually Filtering out some unnecessary data for COVID19 dataset
"""
del nltk_count['2020']
del nltk_count['2nd']
del nltk_count['altmadrianpuse']
del nltk_count['covid19']
del nltk_count['may']
del nltk_count['per']
del nltk_count['tests']
del nltk_count['amid']
del nltk_count['mypotnab']
del nltk_count['naouma_']
nltk_count['covid'] = 388
nltk_count['test'] = 22"""

#Normalized frequency count output
print(nltk_count.most_common(100))

#Creating Mask for the Word Cloud such that it matches the desired shape
triangle_mask = np.array(Image.open("/Users/davidteng/Desktop/tri.png"))


#Generating WordCloud with some customizations on how the word should be displayed
#-------------------------------Setting the color scheme for data set 1 and data set 2---------------------------
#For DataSet 1 colour scheme
#Reference to https://stackoverflow.com/questions/47143461/python-wordcloud-color-by-term-frequency for colour changes according to its frequency
def WordColoring(freqWord):
	def coloring(word, font_size, position, orientation, random_state=None, **kwargs):
		return "hsl({}, {}%, {}%)".format(172, 100 * freqWord[word]/5, int(100.0 * freqWord[word] / 300.0))
	return coloring

#For DataSet 2 colour scheme
"""
def WordColoring(freqWord):
	def coloring(word, font_size, position, orientation, random_state=None, **kwargs):
		return "hsl({}, {}%, {}%)".format(200, 100 * freqWord[word]/5, int(100.0 * freqWord[word] / 255.0))
	return coloring 
"""

#Allowing only 100 words to be displayed on the wordCloud
#For Data set 1 WordCloud
wordcloud = WordCloud(width = 900, height = 900, max_words = 100, background_color = 'white', mask = triangle_mask).generate_from_frequencies(nltk_count)
#For data set D2 WordCloud
#wordcloud = WordCloud(width = 1200, height = 650, max_words = 100, background_color = 'white').generate_from_frequencies(nltk_count)
wordcloud.recolor(color_func=WordColoring(nltk_count))
#Writing it into file
#wordcloud.to_file("/Users/davidteng/Desktop/WordCloud_Data1.png")
#wordcloud.to_file("/Users/davidteng/Desktop/WordCloud_COVID.png")
wordcloud.to_file("/Users/davidteng/Desktop/Combined.png")

#Output the WordCloud Figure
plt.figure(figsize=(10,8))
plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis('off')
plt.show()

















