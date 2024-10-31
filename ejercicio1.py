def funct1(a,b):
 
    if(a<b):
        print("value 0")
        return 0
    else:
        return funct1(a-b, b) + 1
    
  
def funct2(a, b):
 
    if (a<b):
        print("value" + str(a))
        return a
    else:
        return funct2(a-b, b)
    
 
 
if __name__ == "__main__":
 
    result_1 = funct1(16, 3)
    print("resultado 1:" + str(result_1))
 
    result_2 = funct2(16, 3)
    print("resultado 2:" + str(result_2))
 
    result_3 = funct1(312, 4)
    print("resultado 3:" + str(result_3))
 
    result_4 = funct2(312, 4)
    print("resultado 4:" + str(result_4))