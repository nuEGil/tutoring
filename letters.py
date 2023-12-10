
# coding: utf-8

# In[83]:


# import useful libraries first
import math
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from __future__ import division

# define the file path for the text file of interest - yours will be different
path = "data/metamorphosis.txt"

# open the text file and start reading the lines in
f = open(path,'r')

# Since we want to get transitions we should take this time to get rid of extraneous data.
# how to show what we have in the dictionary
cres = ['\xe2','\xc3','\x80','\x93','\x94', '\x99','\x9c','\x9d','\x9f','\xa6','\xb6','+']


chars = []
for line in f:
    # i want to make all of the letters lowercase for funsies, also less characters to mess with
    lowers = [a.lower() for a in line if not a in cres]
    # extend method adds all of this to a single list list
    chars.extend(lowers)
    
print(chars)
# now that I have all of the data in file I can close it 
f.close() # its just good form to close the file after use






# In[84]:


# Now that we have all of the data it is a good idea to get a running count of everything. 
# we could take some time to wirte a ton of code for this, or we can just use the counter method
char_counts = Counter(chars)
# how to show what we have in the dictionary
for k,v in sorted(char_counts.iteritems()):
    print(k,v)
    



# In[85]:


# so we want a histogram of all the frequencies of the characters. What is a histogram but a fancy barplot. 
# we will use the bar plot method here because histogram has you define bins, so it works better for numeric data. 
# we could change all the characters to ascii numbers then do a histogram that way, but since the concept of a bin implies
# character overlap, we dont want to do that. Hence bar plot

x= np.arange(len(char_counts))
print(x) # show the numpy array we made
width = 0.35

# make a bar plot
fig,ax = plt.subplots()

ax.bar(x + width,char_counts.values(), width)
ax.set_xticks(x + width/2)
ax.set_xticklabels(tuple(char_counts.keys()))
ax.set_title('Character Frequencies')
plt.show()


# In[86]:


# now we need to do the same for the transitions. To get this we can either count the number of occurences of every possible
# character transition, or just the ones that appear in this text. Lets go with just the ones that appear in the text.
# although if you want you can do permutaions of pairs of characters in the set that matches our dictionary keys. 

# so we make a list of pairs of data
ch_pairs = [chars[i]+chars[i+1] for i in range(len(chars)-1)]
#print(ch_pairs)

#get the frequencies of each transition
ch_pairs_counts = Counter(ch_pairs)
print(len(ch_pairs_counts))
for k,v in sorted(ch_pairs_counts.iteritems()):
    print(k,v)



# In[79]:


x2= np.arange(len(ch_pairs_counts))
#print(x2) # show the numpy array we made
width = 0.35

# make a bar plot
fig2,ax2 = plt.subplots()

ax2.bar(x2 + width,ch_pairs_counts.values(), width)
#ax2.set_xticks(x2 + width/2)
#ax2.set_xticklabels(tuple(ch_pairs_counts.keys()))
ax2.set_title('Character transition Frequencies')
plt.show()

# so there are 862 of these, you are going to want to play with the rectangle widths and tick marks


# In[93]:


# so now we need to create a markov chain. well the probability that a given transition occurs is the number of transitions 
# observed in each case divided by the total number of observations.
obs   = sum(ch_pairs_counts.values())
probs = [[k,v/obs] for k,v in ch_pairs_counts.iteritems()]
print(probs)

# check to see if it sums to one
print(sum([c[1] for c in probs]))

