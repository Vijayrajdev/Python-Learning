
def find_max(num):

    maximum = num[0]

    for number in num:
        if number > maximum:
            maximum = number

    return (maximum)
