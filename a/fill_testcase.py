import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

import re

b = open("b.txt","w")

def fill():
    count = 0
    a = open("a.txt","r").readlines()
    for i in a:
        if "START_TEST(" in i:
            #print(i)
            count += 1
            if "test" in i:
                tem = i.split("test")
                result = "\t START_TEST(" + "\"" + str(count) + ": test" + tem[-1]
            else:
                tem = i.split(":")
                tem_ = tem[-1].replace(" ","")
                result = "\t START_TEST(" + "\"" + str(count) + ": test_" + tem_
            b.writelines(result)
        else:
            if '"t;' in i:
                tem = i.split(';')
                result = '\t\t\t\t' + '"cover True case at line: '+ tem[1]
                if ')' in i:
                    result = result +';'
                b.writelines(result)
            elif '"f;' in i:
                tem = i.split(';')
                result =  '\t\t\t\t' + '"cover False case at line: '+ tem[1] 
                if ')' in i:
                    result = result +';'
                b.writelines(result)
            elif '"m;' in i:
                tem = i.split(';')
                result =  '\t\t\t\t' + '"cover MCDC case at line: '+ tem[1]
                if ')' in i:
                    result = result +';'
                b.writelines(result)
            elif '"<Insert test case description here>"' in i:
                result = '\t\t\t\t' + '" cover Default case ");'
                b.writelines(result)
            else:
                b.writelines(i)
    b.close()
 
fill()
