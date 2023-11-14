def adding_number(num):
    sum=0
    start= 1
    while start <= num:
        sum = sum + start
        start = start + 1
    return sum

if __name__ == "__main__":
    for a in range(1,11):
        value = adding_number(a)
        print ("adding all numbers less than or equal to " + str(a) + " is equal to " + str(value))
      