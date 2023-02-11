# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:09:47 2023

@author: Fancyui@Gobel
"""

import numpy as np
import math as math

# hex str request = SOI + VER + ADR + CID1 + CID2 + LENGTH + INFO + CHKSUM + EOI

# hex str response = SOI + VER + ADR + CID1 + RTN + LENGTH + INFO + CHKSUM + EOI

# hex str soi = "37 45"

# hex str ver = "11"

# hex str adr: XX, 01 ~ FE

# hex str cid1 = "46"

# hex str cid2: XX, check CID table

# hex str cid3: XX, check CID table

# hex str rtn: XX, check RTN table

# hex str length: XX XX

# hex str info = CID2 + CID3 + "C5 5C" + Data + CRC32

# hex str Data: NULL or various battery data

# hex str CRC32: NULL or XX XX, CRC32 check of Data

# hex str CHKSUM: XX XX

# hex str EOI = "0D"




# caculate hex value for field length

# example: hex str info = "C2 06 C5 5C"

def field_length(info):
    
    data_array = bytearray.fromhex(info)
    
    data_list = list(data_array)
    
    lenid = len(data_list)
    
    sum_lenid = math.floor(lenid/16/16) + math.floor(lenid/16) + np.mod(lenid,16)
    
    mod_lenid = np.mod(sum_lenid,16)
    
    # ~ bin(mod_lenid) + 1
    lchksum = 255-mod_lenid+1-240
    
    lchksum_up = lchksum * pow(2,12)
    
    length = hex(lchksum_up + lenid)
    
    return length


#caculate hex value for field chksum

# hex str middle_data = VER + ADR + CID1 + CID2 + LENGTH + INFO
# example: middle_data = "11 01 46 C2 C0 04 C2 06 C5 5C"

def field_chksum(middle_data):
    
    data_array = bytearray.fromhex(middle_data)
    
    data_list = list(data_array)
    
    sum_data_list = sum(data_list)
    
    mod_sum = np.mod(sum_data_list,65536)
    
    # ~ hex(mod_sum) + 1
    if mod_sum < 256:
        chksum = 255-mod_sum+1
        
    elif mod_sum < 65280:
        chksum = 65279-mod_sum+1+256
        
    else:
        chksum = 255-mod_sum+1+65280
        
    return hex(chksum)

