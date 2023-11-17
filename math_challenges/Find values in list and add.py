def find(list, s):
    for a in range(0, len(list)):
        for b in range(a+1, len(list)):
            if list[a] + list[b] == s:
                return True
    return False


if __name__ == "__main__":
    list=[10,20,30,40,50,60,70,80,90,100]
    if find(list, 100):
        print("There are two values which sum to 100")
    else:
        print("There are no such values")
                    

        