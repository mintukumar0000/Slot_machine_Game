text = open("/Users/mintukumar/Desktop/Cursor_AI/Projects/Simple.txt","r")
d = dict()

for line in text:
    line = line.strip()#Remove the leading and space 
    line = line.lower()#Lower
    words = line.split()# split the line into the matche 

    for word in words:
        if word in d:
            d[word] = d[word]+1
        else:
            d[word]=1
        for key in list(d.keys()):
            print(key,":",d[key]) 