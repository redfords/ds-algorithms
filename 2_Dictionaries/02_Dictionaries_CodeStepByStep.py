"""
Write a function named by_age that accepts three parameters: 1) a dictionary
where each key is a person's name (a string) and the associated value is that
person's age (an integer) 2) an integer for a minimum age and 3) an integer
for a max age. Your function should return a new dictionary with information
about people with ages between the min and max, inclusive.

For example, if a dictionary named ages stores the following key:value pairs:

{"Allison": 18, "Benson": 48, "David": 20, "Erik": 20, "Galen": 15, "Grace: 25,
 "Helene": 40, "Janette": 18, "Jessica": 35, "Marty": 35, "Paul": 28, "Sara": 15,
 "Stuart": 98, "Tyler": 6, "Zack": 20}
The call of by_age(ages, 16, 25) should return the following dictionary:

{18: "Allison and Janette", 20: "David and Erik and Zack", 25: "Grace"}
"""

