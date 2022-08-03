# template string 
from string import Template


def main():
    # this is a normal string
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    # initializinng Template strings
    templ = Template("You're watching ${title} by ${author}")

    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)
    
    # dictonry with template str
    data = {
        "author": "Joe marini",
        "title": "Advanced Python",
        }
    str3 = templ.substitute(data)
    print(str3)
    
if __name__ == "__main__":
    main()