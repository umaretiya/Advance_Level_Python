
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result 

def main():
    print(addition(1,2,3,4))
    print(addition(10,20,30,-40))
    
    myNum = [10,1,10,4,5,6]
    print(addition(*myNum))
    
if __name__ == "__main__":
    main()