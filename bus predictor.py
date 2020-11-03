#!/usr/bin/env python
# coding: utf-8

# In[10]:


import urllib.request as urllib2
import requests
import json
import xmltodict
import time

key = '777tdaSyL5yegA7kLHExam43g'
        
req = urllib2.urlopen('http://www.ctabustracker.com/bustime/api/v1/getpredictions?key=777tdaSyL5yegA7kLHExam43g&stpid=6013').read()


# In[11]:


req_dict = xmltodict.parse(req)


# In[12]:


req_dict


# In[16]:


req_dict['bustime-response']['prd'][1]


# In[19]:


stop = urllib2.urlopen('http://www.ctabustracker.com/bustime/api/v2/getstops?key=777tdaSyL5yegA7kLHExam43g').read()
stop = xmltodict.parse(stop)
stop


# In[4]:


#instantiate init values
pred_str = req_dict['bustime-response']['prd']['prdtm']
time = pred_str[9:14]
pred_hr = int(time[0:2])
pred_mn = int(time[3:5])
tmstmp = req_dict['bustime-response']['prd']['tmstmp']
check_time = tmstmp[9:14]
check_hr = int(check_time[0:2])
check_mn = int(check_time[3:5])


# In[5]:


#produce result
#pred>check

if(check_hr == pred_hr):
    eta = pred_mn-check_mn
else:
    eq = pred_mn + 60
    eta = eq-check_mn
eta   



# In[7]:


#gui

import tkinter


# In[14]:


top = tkinter.Tk()
txt = tkinter.Text(top)
txt.insert(eta)

top.mainloop()


# In[ ]:




