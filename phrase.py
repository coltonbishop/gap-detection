from gap import *

print "What"

# English Text for Which Transled Data Exists
translated_sources = ["data/text1.txt", "data/text2.txt", "data/text3.txt", "data/text4.txt"]

# Large corpus of english Text for Which Transled Data Does Not Yet Exist
sources = ["data/book1.txt", "data/book2.txt", "data/book3.txt", "data/book4.txt", 'data/book5.txt']

clear_known()
add_to_known(word_list('data/book1.txt'))
add_to_known(word_list('data/book2.txt'))
add_to_known(word_list('data/book3.txt'))
add_to_known(word_list('data/book4.txt'))
add_to_known(word_list('data/book5.txt'))
read_in(sources)

#print_freq()

#print_freq()

print critical(100)