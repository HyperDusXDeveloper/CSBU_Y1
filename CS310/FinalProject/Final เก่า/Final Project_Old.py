import random

def add_random_underscores(word):
    check_word = len(word)
    index = 0
    while index == 0 :
        result = []
        for i in word:
            if random.choice([True, False]) and index < int(check_word/2):
                index += 1
                result.append("_")
            else:
                result.append(i)
    return "".join(result)


with open("Final Project/data/words.txt","r") as file1 :
    words = file1.read().split()
    word = random.choice(words)
    x = add_random_underscores(word)
    print(x)