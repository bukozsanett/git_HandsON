s = input()
t = s.upper()

for i in range(len(s)):
    b = t.count(t[i])
    print(s[i],b/len(s)*100)
