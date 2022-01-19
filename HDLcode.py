# code for HDL portion of in class activity 1

def accept_input(test_name):
	entry=input("Enter the {} test result: ".format(test_name))
	return int(entry)
    
def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60> HDL_value >= 40:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer
    
def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
