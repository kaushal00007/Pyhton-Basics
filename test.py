####Python 3 Programming Specialization
# Question1: The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.
handle = open("travel_plans.txt")
num = 0
for line in handle:
    #line = line.rstrip();
    for c in line:
        num += 1


#Question 2: We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.
handle = open("emotion_words.txt")
num_words = 0
for line in handle:
    line = line.split()
    num_words += len(line)

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
handle = open("school_prompt.txt")
num_lines = 0
for line in handle:
    num_lines += 1

#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars
handle = open("school_prompt.txt")
beginning_chars = handle.read(30)

# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

handle = open( "school_prompt.txt")
three = []
for line in handle:
    line = line.split()
    three.append(line[2])

# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt
handle = open("emotion_words.txt")
emotions = []
for line in handle:
    line = line.split()
    emotions.append(line[0])

#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
handle = open("travel_plans.txt")
first_chars = handle.read(33)


#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word,
# then add the word to a list called p_words.
handle = open("school_prompt.txt")
p_words =[]
for line in handle:
    line = line.split()
    for word in line:
        if 'p' in word:
            p_words.append(word)