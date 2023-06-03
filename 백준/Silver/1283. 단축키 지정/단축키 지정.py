shorten_key = []

for _ in range(int(input())):
    options = list(input().split())
    isFind = False
    
    for idx, option in enumerate(options):
        if options[idx][0].lower() not in shorten_key:
            shorten_key.append(options[idx][0].lower())
            options[idx] = "[" + options[idx][0] + "]" + options[idx][1:]
            isFind = True
            break
    if isFind:
        print(" ".join(options))
    else:
        for idx, option in enumerate(options):
            isFind2 = False
            for i, o in enumerate(option):
                if o.lower() not in shorten_key:
                    shorten_key.append(o.lower())
                    options[idx] = options[idx][:i] + "[" + options[idx][i] + "]" + options[idx][i+1:]
                    isFind2 = True
                    break
            if isFind2:
                break
        print(" ".join(options))