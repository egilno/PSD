print (" Welcome , everyone , to the GitHub tutorial !")

def introduction_task () :
    print ("\n- - - Python Task ---")
    print ("Let ’s start by writing a function that adds two numbers !")

    def add_numbers (a , b ) :
        return a + b

    num1 = 5
    num2 = 7
    
    result = add_numbers ( num1 , num2 )
    
    print ( f"The result of adding { num1 } and { num2 } is: { result }")

introduction_task ()