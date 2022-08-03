
def main():
    # any() and all() functions
    list1 = [1, 2, 3, 0, 5, 6]
    
    # any() return true or flase if any is true 
    print(any(list1))

    # all() return true or flase if all true then true else flase
    print(all(list1))
    
    # min(), max()
    print("min: ", min(list1))
    print("max: ", max(list1))
    
    # sum()
    print("sum: ", sum(list1))
if __name__ == "__main__":
    main()