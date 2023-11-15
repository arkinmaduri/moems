def multiplying_number(num):
    product=1
    start=1
    while start <= num:
        product= product*start
        start=start+1
    return product    

if __name__ == "__main__":
    for a in range(1,11):
        value=multiplying_number(a)
        print("multiplying all numbers less than or equal to " + str(a) + " is equal to " + str(value))