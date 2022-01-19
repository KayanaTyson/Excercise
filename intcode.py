# Python code for in class activity 1 

def interface():
    keeprunning=True
    while keeprunning:
        print("My Program")
        print("1-HDL")
        print("2-LDL")
        print("3-total cholestoral")
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keeprunning=False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()

    return
  
def accept_input(test_name):
	entry=input("Enter the {} test result: ".format(test_name))
	return int(entry)

def print_results(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)
    return

def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60> HDL_value >= 40:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer

def check_LDL(LDL_value):
    if LDL_value <= 130:
        answer = "Normal"
    elif 130< LDL_value <= 159:
        answer = "Borderline High"
    elif 159< LDL_value <= 189:
        answer = "High"
    else:
        answer = "Very High"
    return answer
    
def total_chol(chol_value):
    if chol_value <= 200:
        answer = "Normal"
    elif 200< LDL_value <= 239:
        answer = "Borderline High"
    else:
        answer = "High"
    return answer
    
def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_results("HDL", HDL_value, classification)
    
def LDL_driver():
    LDL_value=accept_input("LDL")
    classification=check_LDL(LDL_value)
    print_results("LDL", LDL_value,classification)
    
def total_driver():
    chol_value=accept_input("Total cholestoral")
    classification=total_chol(chol_value)
    print_results("Total cholestoral", chol_value,classification)

interface() 