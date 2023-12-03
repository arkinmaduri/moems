def countNumbersDivisibleBy2(n):
     count = 0
     for a in range(1,n+1):
         if a % 2 == 0:
             count = count + 1
     return count
       
   
if __name__ == "__main__":
     print(countNumbersDivisibleBy2(100000))