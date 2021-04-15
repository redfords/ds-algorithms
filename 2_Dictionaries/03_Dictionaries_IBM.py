# You will need this dictionary for the next two questions:

# soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}

# In the dictionary soundtrack_dic what are the keys?

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic.keys()
dict_keys(['The Bodyguard', 'Saturday Night Fever'])

#  In the dictionary soundtrack_dic what are the values ?

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