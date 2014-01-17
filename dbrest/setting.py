#!/usr/bin/env python

import random
import string

IDCODE='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
MULTICODE=[2, 3, 5, 7, 11, 13]

def codegen():
    codelist = []
    thelist = [ch for ch in IDCODE]
    
    for i in range(len(thelist)):
        rd = random.randrange(0, len(thelist))
        #codelist.append(thelist[rd])
        codelist.append(thelist.pop(rd))
    
    return codelist 

def multigen():
    return random.sample(MULTICODE, 2)

if __name__ == '__main__':
    # Yes, run as standalone
    print("# Custom setting")
    print("PROFILE_CODE='"+string.join(codegen(), '')+"'")
    print("PROFILE_MULTI=["+','.join([str(i) for i in multigen()])+"]")

#else:
    # no, 
