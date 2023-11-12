
def is_num_triagular(num):
    if num < 1:
        return False
    if num == 1:
        return True
    start = 1
    while num > 0:
        num = num - start
        start = start + 1
    return num == 0

if __name__ == "__main__":
    for a in range(1,10000):
        if is_num_triagular(a):
            print ("I am a triangular number " + str(a))
        else:
            print ("I am not a triangular number " + str(a))