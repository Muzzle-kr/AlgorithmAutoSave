import sys
input = sys.stdin.readline

ans = []

while True:
    word = input().strip()
    
    if word == "EOI":
        break
    
    word = word.lower()
    
    print("Found" if "nemo" in word else "Missing")