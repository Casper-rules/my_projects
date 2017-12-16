n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
pdiag=0
j=0
for i in range(n):
#    pdiag+=a[j][i]
	print(a[j][i])
	j+=1
#    print(pdiag)
sdiag=0
j=0
for i in range(n):
#    sdiag+=a[j][i]
	print(a[j][n-i-1])
	j+=1
#    print(sdiag)
#p=abs(sdiag-pdiag)
#print(p)
