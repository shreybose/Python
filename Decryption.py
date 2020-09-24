#!/usr/bin/env python
# coding: utf-8

# In[ ]:


f = open('myfile.txt','r')
text = f.read()
for letter in 'abcdefghijklmnopqrstuvwxyz123456789':
    #print('%s : %d' % (letter, c[letter])) 
    alph = {'e':'E','4':'T','l':'H','9':'A','f':'V','y':'I','b':'N','2':'S','d':'O','r':'C','3':'L',
            'g':'W','v':'D','u':'B','1':'F','7':'K','s':'Q','c':'Z','o':'R','k':'M','j':'U','q':'P',
            'a':'G','m':'Y','x':'J'}
    for keys,values in alph.items():
        text = text.replace(keys,values)
print(text)


# In[ ]:





# In[ ]:





# In[ ]:




