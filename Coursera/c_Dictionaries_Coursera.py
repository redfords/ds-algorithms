"""
Return the most frequent word in a file and the number of occurrences.
"""

def most_frequent_word():
    name = input('Enter the file name: ')
    handle = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    bigcount = None
    bigword = None
    for word, count in counts.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

    print(bigword, bigcount)


"""
Write a program to read through a mail log, and return how many messages have
come from each email address.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'ray@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'david.horwitz@uct.ac.za': 4, 'stephen.marquard@uct.ac.za': 2}

Add code to the above program to figure out who has the most messages in the file.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5
"""

def no_of_emails():
    name = input('Enter the file name: ')
    handle = open(name)

    counts = dict()
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            counts[words[1]] = counts.get(words[1], 0) + 1

    print(counts)
    print(max(counts, key = counts.get), max(counts.values()))
    handle.close()


"""
Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and only
count the letters a-z. Your program should not count spaces, digits, punctuation,
or anything other than the letters a-z.
"""

def letter_frequency():
    name = input("Enter the file: ")
    handle = open(name)

    counts = dict()
    text = handle.read().lower()
    for letter in text:
        if letter >= 'a' <= 'z':
            counts[letter] = counts.get(letter, 0) + 1
    
    sorted_counts = sorted( [ (v,k) for k,v in counts.items() ], reverse=True)
    for k,v in sorted_counts:
        print(k,v)

    handle.close()

letter_frequency()

"""
Text Analysis 
You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can
perform analysis on a given piece of text.
​
Constructor - takes argument 'text', makes it lower case and removes all punctuation, assume only the
following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?).
freqAll - returns a dictionary of all unique words along with the number of their occurences.
freqOf - returns the frequency of the word passed in argument.
"""

class analysedText(object):
    def __init__(self, text):
        self.text = text

        for ch in ['.', ',', '!', '?']:
            text = text.replace(ch, '')
        self.fmtText = text.lower()

    def freqAll(self):
        words = self.fmtText.split()
        counts = dict()
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        return counts

        # wordList = self.fmtText.split()
        # freqMap = {}
        # for word in set(wordList):
        #     freqMap[word] = wordList.count(word)
    
    def freqOf(self, word):
        freqDict = self.freqAll()       
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

sample = """
Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor.
diam et labore? et diam magna. et diam amet.
"""

t1 = analysedText(sample)
# print(t1.fmtText)
# print(t1.freqAll())
# print(t1.freqOf('lorem'))

# Copy file contents to another file
# with open("example1.txt","r") as readFile:
#     with open("example2.txt","w") as writeFile:
#         for line in readFile:
#             writeFile.write(line)

"""
Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""

def convert(keys, values):
    nums = dict(zip(keys, values))
    return nums

"""
Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
"""

def merge(dict1, dict2):
    # dict3 = {**dict1, **dict2}
    dict1.update(dict2)
    return dict1

"""
Access the value of key ‘history’ from the below dict
sample = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
Expected output:
80
"""
def returnMarksHistory(sample):
    return sample['class']['student']['marks']['history']

"""
Initialize dictionary with default values
Given:
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
"""

def initDictionary(employees, defaults):
    return dict.fromkeys(employees, defaults)

"""
Create a new dictionary by extracting the following keys from a below dictionary
Given dictionary:
sample = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
Keys to extract
keys = ["name", "salary"]
Expected output:
{'name': 'Kelly', 'salary': 8000}
"""
def createDict(sample, keys):
    return {k: sample[k] for k in keys}

"""
Delete set of keys from a dictionary
Given:
sample = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keysToRemove = ["name", "salary"]
Expected output:
{'city': 'New york', 'age': 25}
"""

def removeKeys(sample, keysToRemove):
    return  {k: sample[k] for k in sample.keys() - keysToRemove}

"""
Rename key city to location in the following dictionary
sample = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
"""
def rename(sample):
    sample['location'] = sample.pop('city')
    return sample

"""
 Get the key of a minimum value from the following dictionary
sample = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
Expected output:
Math
"""

def getMin(sample):
    return min(sample, key = sample.get)