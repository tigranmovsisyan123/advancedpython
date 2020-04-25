def int32_to_ipv4(num):
    
    o1 = int(num / 16777216) % 256
    o2 = int(num / 65536) % 256
    o3 = int(num / 256) % 256
    o4 = int(num) % 256
    
    return f'{o1}.{o2}.{o3}.{o4}'