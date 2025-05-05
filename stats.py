def countbook(words):
    words = words.split()
    count = len(words)
    return count

def countletters(words):
    lettercount={}
    words = words.lower()
    for letter in words:
        if letter in lettercount:
            lettercount[letter] += 1
        else:
            lettercount[letter] = 1
    return lettercount

def sort_on(words):
    return words["num"]

def sortedletters(lettercount):
    newDict=[]
    for char, number in lettercount.items():
        newDict.append({"char":char,"num": number})
    newDict.sort(reverse=True, key=sort_on)
    return newDict

