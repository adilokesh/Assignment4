#!/usr/bin/env python
# coding: utf-8

# # 1. What exactly is []?

# 1. The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.
# 

# # 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as thethird value? (Assume [2, 4, 6, 8, 10] are in spam.)
# 

# 2. spam[2] = 'hello' (Notice that the third value in a list is at index 2 because the first index is 0.)

# # Let's pretend the spam includes the list ['a','b','c','d']  for the next three queries.
# 

# In[2]:


spam = ['a','b','c','d']


# # 3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?

# 3. 'd' (Note that '3' * 2 is the string '33', which is passed to int() before being divided by 11. This eventually evaluates to 3. Expressions can be used wherever values are used.)

# In[3]:


spam[int(int('3' * 2) / 11)]


# # 4. What is the value of spam[-1]?

# In[4]:


spam[-1]


# # 5. What is the value of spam[:2]?

# In[5]:


spam[:2]


# 
# # Let&#39;s pretend bacon has the list [3.14, &#39;cat,&#39; 11, &#39;cat,&#39; True] for the next three questions.

# In[19]:


bacon=[3.14,'cat',11,'cat',True]


# # 6. What is the value of bacon.index(&#39;cat&#39;)?

# In[20]:


bacon.index('cat')


# # 7. How does bacon.append(99) change the look of the list value in bacon?

# In[21]:


bacon.append(99)
print(bacon)


#  it adds or appends 99 to the end of list

# # 8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?

# In[22]:


bacon.remove('cat')
print(bacon)


# It removes the first 'cat'

# # 9. What are the list concatenation and list replication operators?

# List can be concatenated and replicated just like strings. The + operator combines two list to create new list vcalue and * operator can be used with two lists and a integer value to replicate the list.

# In[24]:


[1,2,3]+['a','b','c']


# In[25]:


['a','b','c']*3


# # 10. What is difference between the list methods append() and insert()?

# 10. While append() will add values only to the end of a list, insert() can add value at any index  in the list.

# In[37]:


bacon=[3.14,'cat',11,'cat',True]
bacon.append(99)
print(bacon)


# In[38]:


bacon.insert(1,'Adi')
print(bacon)


# # 11. What are the two methods for removing items from a list?

# 11. The del statement and the remove() list method are two ways to remove values from a list.

# # 12. Describe how list values and string values are identical.

# 12. Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.

# # 13. What&#39;s the difference between tuples and lists?

# 13. Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists use the square brackets, [ and ].

# # 14. How do you type a tuple value that only contains the integer 42?

#  14. (42,) (The trailing comma is mandatory.)

# In[49]:


t = (42)
type(t)


# # 15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?

# The tuple() and list() functions, respectively

# # 16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they contain?

# 16. They contain references to list values.

# # 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# 17. The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy .deepcopy() will duplicate any lists inside the list

# In[ ]:




