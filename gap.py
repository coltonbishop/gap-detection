import re
import string
import unicodedata
import os
import pickle

# Word Frequency Counter (word->frequency)
frequency = {}
known = []

# Loads stored data
pickle_in = open("freq.pickle","rb")
frequency = pickle.load(pickle_in)
pickle_in = open("known.pickle","rb")
known = pickle.load(pickle_in)

# Reads in sources and updates frequency and known
def read_in(english_sources, translated_sources):
	global frequency, known

	# Reads in new source texts and stores
	for source in english_sources:
		add_to_freq(word_list(source))
	pickle_out = open("freq.pickle","wb")
	pickle.dump(frequency, pickle_out)
	pickle_out.close()

	# Reads in new Known Words and stores
	for source in translated_sources:
		add_to_known(word_list(source))
	pickle_out = open("known.pickle","wb")
	pickle.dump(known, pickle_out)
	pickle_out.close()

# Updates global frequency dictionary and known list given a list of words
def add_to_freq(word_list):
	global frequency 
	for word in word_list:
	    count = frequency.get(word,0)
	    frequency[word] = count + 1

# Adds new words from word list to known
def add_to_known(word_list):
	for word in word_list:
		if word not in known:
			known.append(word)

# Clears the current dictionary of word frequencies
def clear_freq():
	global frequency
	frequency = {}
	pickle_out = open("freq.pickle","wb")
	pickle.dump(frequency, pickle_out)
	pickle_out.close()

# Clears the current list of known words
def clear_known():
	global known
	known = []
	pickle_out = open("known.pickle","wb")
	pickle.dump(known, pickle_out)
	pickle_out.close()

def get_known():
	global known
	return known

def get_frequency():
	global frequency
	return frequency

# Returns a list of words given a text filename
def word_list(filename):
	document_text = open(filename, 'r')
	text_string = document_text.read().lower()
	unicode_string = unicode(text_string, "utf-8")
	nfkd_form = unicodedata.normalize('NFKD', unicode_string)
	only_ascii = nfkd_form.encode('ASCII', 'ignore')
	match_pattern = re.findall(r'\b[a-z\-]{0,15}\b', only_ascii)
	return set(match_pattern)

# Prints the top x list of all words and their frequencies
def print_freq(x):
	global frequency
	for key, value in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
		print("%s: %s" % (key, value))

# Returns the top X most critical words
# Critical words are frequent words that 
def critical_words(x):
	global frequency, known
	critical_words = []
	count = 0
	for w in sorted(frequency, key=frequency.get, reverse=True):
		if count == x:
			return critical_words
		if w not in known:
			critical_words.append(w)
			count = count + 1
	return critical_words

# Returns a critical phrase to be translated
def critical_phrase():
	word = critical_words(1)[0]

	# Regular expression to find sentences that contain word
	# Should search through all text sources (randomized)
	[^.]* critical_word [^.]*\.



	print word


	# Should I store them in a list also? 1000, then randomly remove and return?
	# Refresh periodically?



