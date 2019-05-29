import codecs
from bs4 import BeautifulSoup
from html import unescape
import os
import pandas as pd
files = os.listdir('blogs/')

keywords = ['travel', 'flight']
li = []
def load_xml(file):
	file = 'blogs/' + file
	with codecs.open(file, 'r', encoding='utf-8',
                 errors='replace') as f:
		xml_string = f.read()

	soup = BeautifulSoup(unescape(xml_string), 'lxml')
	l = soup.text.strip().split('\n')
	final = ''
	for line in l:
		if len(line) != 0:
			if line[0].isnumeric():
				continue
		final += line

	final = final.replace('urlLink', '')
	for k in keywords:
		if k in final.lower():
			print('t')
			li.append(1)
			print(final)
			break
	return final

def create_dataframe():
	read_dict = {}
	read_dict['blogs'] = list()
	count = 0
	print(len(files))
	for file in files:
		blog = load_xml(file)
		read_dict['blogs'].append(blog)
		count += 1

	return pd.DataFrame.from_dict(read_dict)


