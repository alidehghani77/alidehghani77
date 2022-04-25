from dataclasses import replace
import re
TEXTO = "VAR"
subject = r"Var\boundary"

if re.search(rf"\b(?=\w){TEXTO}\\boundary(?!\w)", subject, re.IGNORECASE):
    print(TEXTO)
    
    
pattern = '\d+-\d+-\d+'
s = '[2022-12-01 12:22:30][thread1  ][class:30][DEBUG] - Hello Ali Agha'
result = re.sub(pattern,'',s)

print(result)  

s = "black, blue and brown"
pattern = r'bl\w+'
matches = re.findall(pattern,s)

print(matches) 


a_string = "The quick brown fox 2022-02-24 12:22:30 jumped over the tm: 25 lazy dog."
Date = "\d+-\d+-\d+"
Time = "\d+:\d+:\d+"
St = 'tm: \d+'
match = re.findall("%s" % Date, a_string)
print(match) 
match = re.findall("%s" % Time, a_string)
print(match) 
match = re.findall("%s" % St, a_string)
print(str(match).replace("tm: ","")) 

print("***************************************")
with open("d:\\1.txt","r") as f:
    for line in f.readlines():
        dt = re.findall("%s" % Date, line)
        tm = re.findall("%s" % Time, line)
        keyVal = re.findall("%s" % St, line)
        if len(dt) > 0 and  len(tm) > 0  and len(keyVal) > 0:
            print(f"date:{dt[0]} time: {tm[0]} spentTime: {str(keyVal[0])}" )
    
