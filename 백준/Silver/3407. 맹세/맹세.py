one_periodic_table = ['h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u'];
two_periodic_table = ["ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
	"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
	"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
	"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
	"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
	"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
	"pu", "ru", "lv", "dy"];

from collections import deque
# 1글자도 맞고, 2글자도 맞을 경우 둘 다 q에 넣어줘야함.

def bfs(i, word):
    q = deque()
    q.append(0)
    
    visited[0] = True
    flag = False

    while q:
        idx = q.popleft()
        
        if idx >= len(word):
            flag = True
            break

        if word[idx] in one_periodic_table and not visited[idx+1]:
            visited[idx+1] = True
            q.append(idx+1)
        
        if word[idx:idx+2] in two_periodic_table and not visited[idx+2]:
            visited[idx+2] = True
            q.append(idx+2)
    
    if flag:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    word = input()
    visited = [False] * (len(word) + 2)
    bfs(0, word)