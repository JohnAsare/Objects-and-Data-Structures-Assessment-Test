# John Asare
# May 9 2020 18:26


"""Using keys and indexing, grab the 'hello' from the following dictionaries:"""

d = {'k1': {'k2': 'hello'}}

# Grab 'hello'
#print(d['k1']['k2'])


# Getting a little tricker
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

# Grab hello
print(d['k1'][0]['nest_key'][1][0])




