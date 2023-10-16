def mode(numbers):
    if not numbers:
        return []
    mode = []
    max_count = 0
    for num in numbers:
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            mode = [num]
        elif count == max_count and num not in mode:
            mode.append(num)
    return mode
