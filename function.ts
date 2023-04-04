#caculate hex value for field chksum

# hex str middle_data = VER + ADR + CID1 + CID2 + LENGTH + INFO
# example: middle_data = "11 01 46 C2 C0 04 C2 06 C5 5C"

def field_chksum(middle_data):
    
    sum_data_list = sum(middle_data)
    
    mod_sum = np.mod(sum_data_list,65536)
    
    # ~ hex(mod_sum) + 1
    if mod_sum < 256:
        chksum = 255-mod_sum+1
        
    elif mod_sum < 65280:
        chksum = 65279-mod_sum+1+256
        
    else:
        chksum = 255-mod_sum+1+65280
        
    return chksum
