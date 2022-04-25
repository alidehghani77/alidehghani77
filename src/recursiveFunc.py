def count_down(start):
    """ Count down from a number  """
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)


count_down(10)

def sum(n):
    if n > 0:
        return n + sum(n-1)
    return 0


result = sum(100)
print(result)