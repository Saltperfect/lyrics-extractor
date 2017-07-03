import requests
from bs4 import BeautifulSoup
import operator

def word_finder(url):
	word_list = []
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code,'lxml')
	for post_text in soup.find_all('p',{'class':'verse'}):
		content = post_text.get_text()
		words = content.lower().split()
		for each_word in words:
			prin(each_word)
			word_list.append(each_word)
	clean_list(word_list)

def clean_list(word_list):
	clean_word_list = []
	for word in word_list:
		if word[-1] is "," or "\"" or "(" or ")" or "?":
			word = word.replace(',' , '')
			word = word.replace("\"","")
			word = word.replace(")","")
			word = word.replace("(","")
			word = word.replace("?","")
		elif word[0] is "\"":
			word = word.replace("\"","")
			word = word.replace(")","")
			word = word.replace("(","")
		print (word)
		clean_word_list.append(word)
	create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
	word_count = {}
	for word in clean_word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	for key, value in sorted(word_count.items() , key = operator.itemgetter(1)):
		print (key,value)
	text_maker(word_count)



def text_maker(word_count,url):
	fw = open(str(url[27:-5]) + ".txt" , 'w')
	for k,v in word_count.items():
		fw.write(k,'',v,'\n')
	fw.close()


url = 'http://www.metrolyrics.com/stressed-out-lyrics-twenty-one-pilots.html'