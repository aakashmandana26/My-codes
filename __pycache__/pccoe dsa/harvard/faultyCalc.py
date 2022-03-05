# ---------------Faulty Calculator----------------
# faults = {"45 * 3" : "555", "56 + 9" : "77", "56 / 6" : "4"}

n1 = input("Enter first number: ")
operator = input("Enter operation to perform (+ , - , * , /): ")
n2 = input("Enter second number: ")

if(n1=='45' and n2=='3' and operator== '*'):
    print("555")
elif(n1=='56' and n2=='9' and operator=='+'):
    print('77')
elif(n1=='56' and n2=='6' and operator=='/'):
    print('4')
elif(operator=='+'):
    print(int(n1)+int(n2))
elif(operator=='-'):
    print(int(n1)-int(n2))
elif(operator=='*'):
    print(int(n1)*int(n2))
elif(operator=='/'):
    print(int(n1)/int(n2))
else:
    print("Invalid operation")
