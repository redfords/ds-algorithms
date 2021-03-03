""" Take the following string: str = 'X-DSPAM-Confidence:0.8475'
Extract the portion of the string after the colon character and
convert the extracted string into a floating point number.
"""

def convert_to_float(str):
    atpos = str.find(':')
    print(float(str[atpos+1:]))
