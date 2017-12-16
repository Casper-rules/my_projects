#python hash tabe is dictionary
n=int(input("Enter the number of entries to be made : "))
key=[]
d={}
for i in range(n):
	key.append(int(input("Enter key for data "))) #take in values for keys
for i in key:
	d[i]=input("Enter data corrresponding to key %d : "%i) #input data in dictionary for corresponding key
print(d) #show the dictionatry created
print(d[1])#print value for key = 1
del d[2] #deletes data in key 2
print(d[2])
