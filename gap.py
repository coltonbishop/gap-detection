import re
import string
import unicodedata
import os

# Word Frequency Counter (word->frequency)
frequency = {}
known = []


# Reads in sources and updates frequency and known
def read_in(sources):
	global known, frequency
	# Reads in Known Words
	update_known()
	# Reads in source texts
	for source in sources:
		update_freq(word_list(source))

# Update known from text file
def update_known():

	global known
	# Reads in Known Words
	document_text = open('data/known.txt', 'r')
	text_string = document_text.read().lower()
	unicode_string = unicode(text_string, "utf-8")
	nfkd_form = unicodedata.normalize('NFKD', unicode_string)
	only_ascii = nfkd_form.encode('ASCII', 'ignore')
	match_pattern = re.findall(r'\b[a-z\-]{0,15}\b', only_ascii)
	known = list(dict.fromkeys(match_pattern)) 

# Updates global frequency dictionary and known list given a list of words
def update_freq(word_list):
	global frequency 
	for word in word_list:
	    count = frequency.get(word,0)
	    frequency[word] = count + 1


# Adds new words from word list to known
def add_to_known(word_list):
	new_words = []
	text_file = open("data/known.txt", "r")
	lines = text_file.readlines()
	for word in word_list:
		if word not in lines:
			new_words.append(word)

	with open("data/known.txt", 'w') as f:
	    for word in new_words:
	        f.write("%s\n" % word)
	update_known()

def clear_known():
	os.remove("data/known.txt")
	open('data/known.txt', 'a').close()


def get_known():
	return known

def get_frequency():
	return frequency


# Returns a list of words given a text filename
def word_list(filename):
	document_text = open(filename, 'r')
	text_string = document_text.read().lower()
	unicode_string = unicode(text_string, "utf-8")
	nfkd_form = unicodedata.normalize('NFKD', unicode_string)
	only_ascii = nfkd_form.encode('ASCII', 'ignore')
	match_pattern = re.findall(r'\b[a-z\-]{0,15}\b', only_ascii)
	return match_pattern

# Prints list of all words and their frequencies
def print_freq():
	frequency_list = frequency.keys()
	for words in frequency_list:
		print words, frequency[words]

# Returns the top X most critical words
# Critical words are frequent words that 
def critical(x):

	critical_words = []
	count = 0
	for w in sorted(frequency, key=frequency.get, reverse=True):
		if count == x:
			return critical_words
		if w not in known:
			critical_words.append(w)
			count = count + 1
	return critical_words


 		





