def solution(bandage, health, attacks):
    global current_time
    global continual_time
    current_time = 0
    continual_time = 0
    
    maximum_health = health
    bandage_addition_time, recovery, addition_recovery = bandage
    

    for attack_time, damage in attacks:
        
        # 붕대를 감는다.
        while current_time < attack_time:
            # 시간 추가
            current_time += 1
            continual_time += 1
            
            # 체력 회복
            health = min(maximum_health, health + recovery)
            # 체력 회복 보너스
            if continual_time % bandage_addition_time == 0:
                health = min(maximum_health, health + addition_recovery)
        
        # 몬스터가 공격한다.
        else:
            health -= damage
            current_time += 1
            continual_time = 0
            
            if health < 1:
                return -1
    
    return health