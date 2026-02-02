t = int(input())
ans = []
for i in range(t):
    m, n = input().split()
M = int(m, 2)
N = int(n, 2)
temp = M + N
ans.append(temp)
final = bin(max(ans))
print(final[2:])
