"""
************
*          *
*          *
*          *
*          *
************

"""

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception("'Symbol' needs to be a string of length 1")
    for i in range(height):
        if i == 0 or i == height - 1:
            for k in range(width):
                print(symbol,end="")
            print("")    
        else:
            for i in range(width):            
                if i == 0 or i == width - 1:
                    print(symbol,end="")
                else: print(" ",end="")
            print("")    


boxPrint('00',10,5)