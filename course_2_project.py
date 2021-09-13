#We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv
# which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet.
# We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and
# negative_words.txt.

#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
# You will create a csv file, which contains columns for the Number of Retweets, Number of Replies,
# Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry
# words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or
# Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

#To start, define a function called strip_punctuation which takes one parameter, a string which represents a word,
# and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method
# for strings.)
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    updated_word = ""
    for c in word:
        if c not in punctuation_chars:
            updated_word += c
    return updated_word

#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter,
# a string which represents one or more sentences, and calculates how many words in the string are considered positive words.
# Use the list, positive_words to determine what words will count as positive. The function should return a positive integer -
# how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased,
# so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


def strip_punctuation(word):
    updated_word = ""
    for c in word:
        if c not in punctuation_chars:
            updated_word += c
    return updated_word


def get_pos(sentence):
    lower_sentence = sentence.lower()
    lower_sentence = strip_punctuation(lower_sentence)
    splitted_words = lower_sentence.split()
    pos_count = 0
    for words in splitted_words:
        if words in positive_words:
            pos_count += 1
    return pos_count
#Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter,
# a string which represents one or more sentences, and calculates how many words in the string are considered
# negative words. Use the list, negative_words to determine what words will count as negative. The function
# should return a positive integer - how many occurrences there are of negative words in the text. Note that all
# of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to
# lower case as well.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def strip_punctuation(word):
    updated_word = ""
    for c in word:
        if c not in punctuation_chars:
            updated_word += c
    return updated_word

def get_neg(sentence):
    lower_neg_words = strip_punctuation(sentence).lower().split()
    neg_count = 0
    for words in lower_neg_words:
        if words in negative_words:
           neg_count += 1
    return neg_count

#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake
# generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that
# tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
# Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to
# create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive
# Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet),
# and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in
# that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google
# Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment,
# if you’re accessing this textbook from Coursera.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    updated_word = ""
    for c in word:
        if c not in punctuation_chars:
            updated_word += c
    return updated_word
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(sentence):
    lower_sentence = sentence.lower()
    lower_sentence = strip_punctuation(lower_sentence)
    splitted_words = lower_sentence.split()
    pos_count = 0
    for words in splitted_words:
        if words in positive_words:
            pos_count += 1
    return pos_count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(sentence):
    lower_neg_words = strip_punctuation(sentence).lower().split()
    neg_count = 0
    for words in lower_neg_words:
        if words in negative_words:
           neg_count += 1
    return neg_count

#The following code opens the twitter file
inputFileHandle=open("project_twitter_data.csv","r")
data = inputFileHandle.readlines()

#The following code writes in the csv file named resulting_data
outfile=open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")

for i in data[1:]:
    res_row=""
    splt=i.strip().split(",")           #Leading and trailing whitespaces are removed with strip
    res_row=("{},{},{},{},{}".format(splt[1], splt[2], get_pos(splt[0]), get_neg(splt[0]), (get_pos(splt[0])-get_neg(splt[0]))))
    outfile.write(res_row)
    outfile.write("\n")

outfile.close()


