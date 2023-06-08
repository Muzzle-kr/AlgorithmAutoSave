import string
ascii_uppercase = string.ascii_uppercase

# 밑에 잘못된거 있나봐줘 
def next_permutation(arr):
    i = len(arr)-2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    
    if i == -1:
            return False
        
    j = len(arr)-1
    while j >= 0 and arr[i] >= arr[j]:
        j -= 1
        
    arr[i], arr[j] = arr[j], arr[i]
    result = num_arr[:i+1] 
    result.extend(list(reversed(num_arr[i+1:])))
    return result

for _ in range(int(input())):
    word = input()
    num_arr = [ascii_uppercase.index(w) for w in word]
    np = next_permutation(num_arr)
    
    if not np:
        print(word)
    else:
        print("".join([ascii_uppercase[n] for n in np]))