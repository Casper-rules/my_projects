l=[[[8,3,4],[1,5,9],[6,7,2]],
[[6,7,2],[1,5,9],[8,3,4]],
[[4,9,2],[3,5,7],[8,1,6]],
[[2,9,4],[7,5,3],[6,1,8]],
[[2,7,6],[9,5,1],[4,3,8]],
[[4,3,8],[9,5,1],[2,7,6]],
[[6,1,8],[7,5,3],[2,9,4]],
[[8,1,6],[3,5,7],[4,9,2]]]

mnm=[]

s = []
for s_i in range(3):
   s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
   s.append(s_t)


for k in range(8):
	a=l[k]
	sim=0
	for i in range(3):
		for j in range(3):
			sim+=abs(a[i][j]-s[i][j])
	mnm.append(sim)

mnm.sort()

print(mnm[0])
