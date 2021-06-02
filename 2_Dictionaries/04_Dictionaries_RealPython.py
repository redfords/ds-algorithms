import string
import datetime as dt

"""
Sum of Integers Up To n
Write a function, add_it_up(), that takes a single integer as input and returns the sum of the
integers from zero to the input parameter.
The function should return 0 if a non-integer is passed in.
"""

def add_it_up(num):
    sum_n = 0
    for n in range(num + 1):
        sum_n += n
    return sum_n

def add_it_up_improved(num):
    return sum(range(num + 1))

"""
Caesar Cipher
A Caesar cipher is a simple substitution cipher in which each letter of the plain text is
substituted with a letter found by moving n places down the alphabet. For example, assume
the input plain text is the following:

abcd xyz
If the shift value, n, is 4, then the encrypted text would be the following:

efgh bcd
You are to write a function that accepts two arguments, a plain-text message and a number
of letters to shift in the cipher. The function will return an encrypted string with all
letters transformed and all punctuation and whitespace remaining unchanged.

Note: You can assume the plain text is all lowercase ASCII.
"""

def caesar_cipher(message, num):
    letters = string.ascii_lowercase
    mask = letters[num :] + letters[: num]
    translation_table = str.maketrans(letters, mask)

    return message.translate(translation_table)

"""
Log Parser
Accepts a filename on the command line. The file is a Linux-like log file from a system you
are debugging. Mixed in among the various statements are messages indicating the state of the
device. They look like this:

Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
The device state message has many possible values, but this program cares about only three:
ON, OFF, and ERR.

Your program will parse the given log file and print out a report giving how long the device
was ON and the timestamp of any ERR conditions.

Device was on for 7 seconds
Timestamps of error events:
   Jul 11 16:11:54:661
   Jul 11 16:11:56:067
"""

