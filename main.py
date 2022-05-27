# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        words = f.read()
        texts = words.split()
    return texts


def count_words():
    text = read_file_content("./story.txt")
    word_counter = {}
    for word in text:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

    return word_counter
print(count_words())
