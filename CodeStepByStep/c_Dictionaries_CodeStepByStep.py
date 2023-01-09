"""
Write a function named area_codes that prints information about the most commonly occurring area
code in a file of telephone numbers.

The input file contains a collection of telephone numbers, one per line, in the following format.
Each phone number begins with a three-digit area code.

650-723-2273
206-685-2181
800-356-9377
800-347-3288
650-725-7411
520-297-6312
206-543-1695
800-266-2278
206-543-2969

Your function should open and read the contents of this input file and figure out which area code
occurs most frequently in the data. If multiple area codes are tied for being the most frequent,
print the numerically smallest of the ones that tied.

After determining which is the most common area code, your function should prout all of the phone
numbers from that area code, in sorted numerical order, one per line.

For example, if the input above at right comes from a file named phonenumbers.txt, then the call
of area_codes("phonenumbers.txt") should print the following console output:

206-543-1695
206-543-2969
206-685-2181
"""

def area_codes(file_name):
    handle = open(file_name)
    lines = list()
    count = dict()

    for line in handle:
        lines.append(line)
        count[line[: 3]] = count.get(line[: 3], 0) + 1

    max_key = max(count, key = count.get)

    for line in lines:
        if line[: 3] == max_key:
            print(line)

# area_codes('codes.txt')

"""
Write a function named biggest_family that reads an input file of people's names and prints
information about which family has the most people in it.

Each line of the file contains a first name, a single space, and a last name.

Jon Snow
Ned Stark
Gregor Clegane
Cersei Lannister
Tyrion Lannister
Sandor Clegane
Jaime Lannister
Catelyn Stark
Theon Greyjoy
Arya Stark
Cersei Smith
Ned Jones

Your function should open and read the contents of this file and figure out which last name(s)
occur most frequently in the data, and print the members of the family in ABC order in exactly the
format shown below.

If multiple families are tied for the most members, preach of the tied families in the same format.

For example, if the input above is in families.txt, then the call of biggest_family("families.txt")
should print:

Lannister family: Cersei Jaime Tyrion
Stark family: Arya Catelyn Ned
"""

def biggest_family(file_name):
    handle = open(file_name)
    lines = list()
    count = dict()

    for line in handle:
        name = line.split()
        lines.append(name)
        count[name[1]] = count.get(name[1], 0) + 1

    max_value = max(count.values())
    max_keys = list(key for key, value in count.items() if value == max_value)

    for key in max_keys:
        print(f"{key} family:")
        for line in lines:
            if line[1] == key:
                print(line[0])

# biggest_family('family.txt')

"""
Write a complete console program that asks the user for a list of names (one per line) until the
user enters a blank line (i.e., just presses Enter when asked for a name). At that point, the
program should print out how many times each name in the list was entered. A sample run of this
program is shown below.

Enter name: Alice
Enter name: Bob
Enter name: Alice
Enter name: Chelsea
Enter name: Bob
Enter name: Alice
Enter name:
Entry [Alice] has count 3
Entry [Bob] has count 2
Entry [Chelsea] has count 1
"""

def count_names():
    names = []
    new_name = '...'
    count = dict()

    while new_name != '':
        new_name = input("Enter name: ")
        if new_name != '':
            names.append(new_name)
    
    for name in names:
        count[name] = count.get(name, 0) + 1

    for key, value in count.items():
        print(f"Entry [{key}] has count {value}")

"""
Write a function named deans_list that accepts as a parameter a dictionary of student names mapped
to GPAs (A decimal number between 0.0 and 4.0 inclusive) and returns a set of all students who have
GPAs of 3.5 or above. For example, if a dictionary grades contains the following:

{"Hermione": 4, "Harry": 3.4, "Ron": 3.4, "Ginny": 3.8, "Draco": 3.7}
Then the call of deans_list(grades) should return the following set:

{"Hermione", "Ginny", "Draco"}
If the passed in dictionary is empty, your function should return an empty set.
"""

def deans_list(student_gpa):
    gpa_list = set()
    for student, gpa in student_gpa.items():
        if gpa >= 3.5:
            gpa_list.add(student)
    return gpa_list

student_gpa = {"Hermione": 4, "Harry": 3.4, "Ron": 3.4, "Ginny": 3.8, "Draco": 3.7}

"""
Write a function named friend_list that accepts a file name as a parameter and reads friend
relationships from a file and stores them into a compound collection that is returned. You should
create a dictionary where each key is a person's name from the file, and the value associated with
that key is a setof all friends of that person. Friendships are bi-directional: if Marty is friends
with Danielle, Danielle is friends with Marty.

The file contains one friend relationship per line, consisting of two names. The names are separated
by a single space.

Marty Cynthia
Danielle Marty

Then the call of friend_list("buddies.txt") should return a dictionary with the following contents:

{'Cynthia': ['Marty'], 'Danielle': ['Marty'], 'Marty': ['Cynthia', 'Danielle']}

You should make sure that each person's friends are stored in sorted order in your dictionary.
"""



"""
Write a function named has_duplicate_value that accepts a dictionary from strings to strings as a
parameter and returns True if any two keys map to the same value. For example, the dictionary
{'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Meghan': 'Miller', 'Hal': 'Perkins'}
would return True because both 'Jessica' and 'Meghan' map to the value 'Miller'. Return False if
passed an empty or one-element dictionary.
"""

def has_duplicate_value(dictionary):
    if len(dictionary) <= 1:
        return False
    else:
        values = list(dictionary.values())
        no_duplicates = list(set(dictionary.values()))
        return len(values) > len(no_duplicates)

dictionary = {'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Meghan': 'Miller'}

"""
Write a function named is_sub_dict that accepts two dictionaries from strings to strings as its
parameters and returns True if every key in the first dictionary is also contained in the second
dictionary and maps to the same value in the second dictionary.

map1: {Smith': '949-0504', 'Marty': '206-9024}
map2: {Marty': '206-9024', 'Hawking': '123-4567', 'Smith': '949-0504', 'Newton': '123-4567}

Constraints: You may not declare any auxiliary data structures in solving this problem.
"""

def is_sub_dict(sub_dict, dictionary):
    # return sub_dict.items() <= dictionary.items()
    return all(item in dictionary.items() for item in sub_dict.items())

dictionary = {'Marty': '206-9024', 'Hawking': '123-4567', 'Smith': '949-0504', 'Newton': '123-4567'}
sub_dict = {'Smith': '949-0504', 'Marty': '206-9024'}

"""
Write a function named start_letters that accepts a file name as a parameter, reads the text file,
and produces a dictionary of counters based on what character each word in the file starts with,
case-insensitively. For example, if the file contains "To be or not to be", the dictionary would
store {"b": 2, "n": 1, "o": 1, "t": 2}. Print the mappings in sorted order.

b 2
n 1
o 1
t 2
"""

def start_letters(file_name):
    handle = open(file_name)
    count = dict()
    for line in handle:
        words = line.split()
        for word in words:
            count[word[0]] = count.get(word[0], 0) + 1

    return count

letter_count = start_letters('words.txt')