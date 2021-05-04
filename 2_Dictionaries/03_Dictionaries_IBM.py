# You will need this dictionary for the next two questions:

# soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}

# In the dictionary soundtrack_dic what are the keys?

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic.keys()
dict_keys(['The Bodyguard', 'Saturday Night Fever'])

#  In the dictionary soundtrack_dic what are the values?

soundtrack_dic.values()
dict_values(['1992', '1977'])

# You will need this dictionary for the following questions:

# The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales
# in millions 50, 50 and 65 respectively.

# Create a dictionary album_sales_dict where the keys are the album name and the sales in millions
# are the values.

album_sales_dict = {"Back in Black":50, "The Bodyguard":50, "Thriller":65}

# Use the dictionary to find the total sales of Thriller

album_sales_dict["Thriller"]

# Find the names of the albums from the dictionary using the method keys()

album_sales_dict.keys()
dict_keys(['Back in Black', 'The Bodyguard', 'Thriller'])

# Find the values of the recording sales from the dictionary using the method values

album_sales_dict.values()
dict_values([50, 50, 65])

""" Text Analysis 
You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can
perform analysis on a given piece of text.
​
Constructor - takes argument 'text', makes it lower case and removes all punctuation, assume only the
following punctuation is used: period (.), exclamation mark (!), comma (,) and question mark (?).

freqAll - returns a dictionary of all unique words along with the number of their occurences.

freqOf - returns the frequency of the word passed in argument. """

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

sample = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
t1 = analysedText(sample)
print(t1.fmtText)
print(t1.freqAll())
print(t1.freqOf('lorem'))

# Copy file contents to another file
with open("example1.txt","r") as readFile:
    with open("example2.txt","w") as writeFile:
        for line in readFile:
            writeFile.write(line)

"""
Your local university's Raptors fan club maintains a register of its active members on a .txt document.
Every month they update the file by removing the members who are not active. You have been tasked with
automating this with your python skills.
Given the file currentMem, remove each member with a 'no' in their inactive coloumn. Keep track of each
of the removed members and append them to the exMem file. Make sure the format of the original files is
preserved (hint: do this by reading/writing whole lines and ensuring the header remains).
"""

from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

genFiles(memReg,exReg)

def cleanFiles(currentMem,exMem):
    '''
    currentMem: File containing list of current members
    exMem: File containing list of old members
    
    Removes all rows from currentMem containing 'no' and appends them to exMem
    '''
    
    
    pass 

# Code to help you see the files
# Leave as is
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
