# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:40:35 2019

@author: Dalia
"""

import sys
def convert(list): 
    s =""
# Converting integer list to string list 
    s = [str(i) for i in list] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res) 
  
# Driver code 
list = [1, 2, 3] 
print(convert(list)) 
