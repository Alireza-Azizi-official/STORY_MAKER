# to open the file in read mode. 
with open("story.txt", "r") as f :
    story = f.read()
# print(story)

# have a set to eliminate the repetitive words and set different targets to find the specific words.
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

# to find the words we want to replace.
for i,char in enumerate(story):
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
# print(words)

# to have a dictionary with the words we find and replace them with the entered words.
answers = {}
for word in words:
    answer = input("Enter a word for " + word + ":")
    answers[word] = answer

# to put the new words in the story.
for word in words: 
    story = story.replace(word,answers[word])
print(story)