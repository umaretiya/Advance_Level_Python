
def main():
    # days name is english and french
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
    
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    
    # itermethods
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)
            
    # simple for loops        
    for m in days:
        print(m)
   
    # indexing a iter items
    for m in range(len(days)):
        print(m, days[m])
        
     # indexing a iter items with enumarete   
    for i, m in enumerate(days, start=1):
        print(i, m)
        
    # zip functions 
    for m in zip(days, daysFr):
        print(m)
        
    # enumerating a with zip
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], " in french")
if __name__ == "__main__":
    main()