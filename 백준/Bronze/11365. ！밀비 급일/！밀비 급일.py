while True:
    string = input().strip()
    reverse_string = list(string)[::-1]
    
    if string == "END":
        break
    
    print("".join(reverse_string))