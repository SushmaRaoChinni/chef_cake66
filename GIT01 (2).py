t = int(input())

def pattern(c):
    if c =="R":
        return 5
    return 3
    
for q in range(t):
    n,m = map(int,input().split())
    str_list =[]
    for i in range(n):
        str_list.append('')
        str_list[i] = input()
    a,b = [],[]
    for i in range(n):
        a.append([])
        b.append([])
        for j in range(m):
            if(i+j)%2 ==0:
                a[i].append('R')
                b[i].append('G')
            else:
                a[i].append('G')
                b[i].append('R')
    pattern1,pattern2 =0,0
    for i in range(n):
        for j in range(m):
            if str_list[i][j]== a[i][j]:
                pattern2+= pattern(str_list[i][j])
            else:
                pattern1+= pattern(str_list[i][j])
                
    print(min(pattern1,pattern2))   