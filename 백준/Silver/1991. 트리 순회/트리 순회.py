N = int(input())
tree = [[] for _ in range(27)]

for _ in range(N):
    a, s1, s2 = input().split()
    
    a = ord(a) - 65
    s1 = ord(s1) - 65 if s1 != '.' else None
    s2 = ord(s2) - 65 if s2 != '.' else None

    tree[a] = [s1, s2]
    
pre_order_answer = ""
in_order_answer = ""
post_order_answer = ""

def pre_order(idx):
    global pre_order_answer
    
    if idx is None:
        return

    s1, s2 = tree[idx]
    pre_order_answer += chr(idx + 65)
    pre_order(s1)
    pre_order(s2)

def in_order(idx):
    global in_order_answer
    
    if idx is None:
        return
    
    s1, s2 = tree[idx]
    in_order(s1)
    in_order_answer += chr(idx + 65)
    in_order(s2)

def post_order(idx):
    global post_order_answer
    
    if idx is None:
        return
    
    s1, s2 = tree[idx]
    post_order(s1)
    post_order(s2)
    post_order_answer += chr(idx + 65)

pre_order(0)
in_order(0)
post_order(0)

print(pre_order_answer)
print(in_order_answer)
print(post_order_answer)