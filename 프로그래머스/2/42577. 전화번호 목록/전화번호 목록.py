def solution(phone_book):
    phone_book.sort()
    prefix_dict = {}
    
    for idx, phone_number in enumerate(phone_book):
        comb = ''
        
        for p in phone_number:
            comb += p
            if comb in prefix_dict:
                return False
            
        prefix_dict[phone_number] = 1
    
    return True