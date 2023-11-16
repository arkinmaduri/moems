# list= [1,2,3,4,5,6,7,8,9,10]
# print(str(list))
# a=70
# if a in list:

#     print(str(True))

# else:
#     print(str(False))

def search(a, list):
    for v in list:
        if a == v:
            return True
    return False
    
if __name__ == "__main__":
    list= [1,2,3,4,5,6,7,8,9,10]
    a = 70
    print(search(a, list))