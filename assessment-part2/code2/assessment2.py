def one(word, chars):
    list = []
    for char in word:
        if char in chars:
            list.append('_')
        else:
            list.append(char)
    return ''.join(list)

def two(total_seconds):
    days = total_seconds/86400
    # check difference
    difference_day = days-int(days)
    if difference_day == 0:
        return (int(days), 0, 0, 0)
    # if there is a difference, we convert that to hours, minutes, seconds
    else:
        # convert the difference back to seconds
        seconds_left = total_seconds - (int(days)*86400)
        hours = seconds_left/3600
        # checking difference in hours
        difference_hour = hours - int(hours)
        if difference_hour == 0:
            return (int(days), int(hours), 0, 0)
        else:
            # convert difference into seconds
            seconds_left = seconds_left - (int(hours)*3600)
            minutes = seconds_left/60
            # checking difference in minutes
            difference_minutes = minutes - int(minutes)
            if difference_minutes == 0:
                return (int(days), int(hours), int(minutes), 0)
            else:
                seconds_left = seconds_left - (int(minutes)*60)
                return (int(days), int(hours), int(minutes), int(seconds_left))


def three(dictionary):
    {v: k for k, v in dictionary.items()}

def four(number):
    new_number = number - 1
    while True:
        if number % new_number == 0:
            return new_number
            break
        else:
            new_number -= 1

def five(chars):
    list = []
    for char in chars:
        list.append(ord(char))

    lowest_no = min(list)
    return chr(lowest_no)

def six(paragraph, limit):
    pass
