# Get the name of the file and open it
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "kk.txt"
try:
    handle = open(fname,'r')
except:
    print('Cannot open file: ', fname)
    quit()
# Count word frequency
counts = dict()#or {}
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
# Find the most common word: alternate for this sec in one line:
#list=sorted([(c,n) for n,c in counts.items()], reverse=True
list=list()
for name, count in counts.items():
    newtup=(count, name)#tuple
    list.append(newtup)#tuple appended in list
list=sorted(list, reverse=True)
#All done
for count, name in list[:10]:
    print(name, count)
