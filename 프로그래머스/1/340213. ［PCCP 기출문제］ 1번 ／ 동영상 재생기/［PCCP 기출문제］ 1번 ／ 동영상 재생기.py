def solution(video_len, pos, op_start, op_end, commands):
    seconds = convert_time_to_seconds(pos)
    video_len_to_seconds = convert_time_to_seconds(video_len)
    op_start_to_seconds = convert_time_to_seconds(op_start)
    op_end_to_seconds = convert_time_to_seconds(op_end)
    
    
        
    for command in commands:
        seconds = skipOpeningWhenConditionIsTrue(seconds, op_start_to_seconds, op_end_to_seconds)
        
        if command == "prev":
            seconds = max(0, seconds - 10)
        else:
            seconds = min(video_len_to_seconds, seconds + 10)

    seconds = skipOpeningWhenConditionIsTrue(seconds, op_start_to_seconds, op_end_to_seconds)
    return convert_seconds_to_time(seconds)

def skipOpeningWhenConditionIsTrue(seconds, op_start, op_end):
    if op_start <= seconds <= op_end:
        return op_end
    return seconds

def convert_time_to_seconds(time):
    minute, second = time.split(":")
    return int(minute) * 60 + int(second)

def convert_seconds_to_time(time):
    minutes = str(time // 60).zfill(2)
    seconds = str(time % 60).zfill(2)

    return minutes + ":" + seconds