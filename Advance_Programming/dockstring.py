
def myFunction(arg1, arg2=None):
    """_summary_ myFunction --> doesn't do really anythings, just prints

    Args:
        arg1 (_type_): _description_ . whaterverr you feel like pass.
        arg2 (_type_, optional): _description_. Defaults to None.
    """
    print(arg1, arg2)
    
    
def main():
    print(myFunction.__doc__)
    
if __name__ == "__main__":
    main()