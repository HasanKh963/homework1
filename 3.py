name=input("enter your name")
print()
file=open("hassan.txt",'r')
outfile=open("outfile.txt",'w')
s=file.read()
l=s.splitlines()
file.close()
print("welcome to python quize")
numoftrueanswers=0
for i in l:
    q=i.split(':')
    print(q[0])
    a=input()
    if a==q[1]:
        numoftrueanswers+=1
r=[name+"\n","answered true of {} from {}".format(numoftrueanswers,len(l))]
print(r[0])
print(r[1])
outfile.writelines(r)
outfile.close()