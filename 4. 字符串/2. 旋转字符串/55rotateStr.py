k = int(input())
s = list(map(str,input()))

def rotate(s):
    temp = s[:-1]
    s[0] = s[-1]
    s[1:] = temp
    return s

for i in range(k):
     s = rotate(s)
print(''.join(s))