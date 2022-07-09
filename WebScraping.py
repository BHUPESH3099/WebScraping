
from bs4 import BeautifulSoup
import requests


# In[31]:


url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

result=requests.get(url_link).text

doc=BeautifulSoup(result, "html.parser")


# In[36]:


my_table=doc.find("table", class_="wikitable sortable plainrowheaders")


# In[49]:


th_tags = my_table.find_all("th")
names = []
for elem in th_tags:
    a_links = elem.find_all("a")
    for i in a_links:
      names.append(i.string)
print(names)


# In[48]:


final_list = names[9: ]
states = []
for str in final_list:
  if len(str) > 3:
      states.append(str)
print(states)


# In[50]:


divs = my_table.find_all("div")
pop = []
for i in divs:
  pop.append(i.string)
print(pop)


# In[52]:


pop_final = []
for i in pop:
  if len(i) > 3:
      pop_final.append(i)
print(pop_final)


# In[53]:


import pandas as pd

df = pd.DataFrame()

df['state'] = states
df['population'] = pop_final

print(df)


# In[54]:


df.to_csv('us_info.csv')







