# Python code for in class activity 1 

def interface():
    keeprunning=True
    while keeprunning:
        print("My Program")
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keeprunning=False
    return
   
interface()