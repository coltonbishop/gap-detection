from gap import *


def load_new_data():

	clear_known()
	clear_freq()
	# Large corpus of english Text for Which Transled Data Does Not Yet Exist
	english_sources = ["data/book1.txt", "data/book2.txt", "data/book3.txt", "data/book4.txt", 'data/book5.txt']
	# English Text for Which Transled Data Exists
	translated_sources = ["data/book1.txt", "data/book2.txt"]
	read_in(english_sources, translated_sources)


critical_phrase()