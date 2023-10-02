def solution(k, ranges):
    
    def get_coordinates(k):
        arr = [k]
        
        while k != 1:
            if k % 2 == 0:
                k = k // 2
            else:
                k = k * 3 + 1
            arr.append(k)    
        return arr
    
    def get_area(arr):
        area = []
        for i in range(len(arr)-1):
            area.append((arr[i] + arr[i+1]) / 2)
        return area
    
    def get_integral(areas, ranges):
        n = len(areas) + 1
        result = []
        
        for r in ranges:
            x1, x2 = r
            x2 = x2 if x2 > 0 else n - abs(x2)
            
            total = 0.0
            
            if x1 >= x2:
                result.append(-1.0)
                continue
            
            for i in range(x1, x2-1):
                total += areas[i]
            
            result.append(total)
            
        return result
    coordinates = get_coordinates(k)
    areas = get_area(coordinates)
    answer = get_integral(areas, ranges)
    
    
    
    return answer