# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:09:47 2023

@author: Fancyui@Gobel
"""

import numpy as np
import math as math

# caculate hex value for field length

# str info = "C2 06 C5 5C"

def field_length(info):
    
    hex_data_array = bytearray.fromhex(info)
    
    hex_data_list = list(hex_data_array)
    
    lenid = len(hex_data_list)
    
    sum_lenid = math.floor(lenid/16/16) + math.floor(lenid/16) + np.mod(lenid,16)
    
    mod_lenid = np.mod(sum_lenid,16)
    
    lchksum = 255-mod_lenid+1-240
    
    lchksum_up = lchksum * pow(2,12)
    
    length = hex(lchksum_up + lenid)
    
    return length


#caculate hex value of field chksum

# str middle_data = "C2 06 C5 5C"

def field_chksum(middle_data):
    
    data_array = bytearray.fromhex(middle_data)
    
    data_list = list(data_array)
    
    sum_data_list = sum(data_list)
    
    mod_sum = np.mod(sum_data_list,65536)
    
    if mod_sum < 256:
        chksum = 255-mod_sum+1
        
    elif mod_sum < 65280:
        chksum = 65279-mod_sum+1+256
        
    else:
        chksum = 255-mod_sum+1+65280
        
    return hex(chksum)

