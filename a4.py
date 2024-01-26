
#Advanced Calculator Project



print("----Temperature Converter----")
decision = input("---- Would you like to convert farenheit to celsius? Yes/No ") #asking the user if they would like to convert farenheit to celsius
if decision.lower() == "yes":# if yes check used .lower() so that way it doesnt matter if there are cap errors 
    degree = float(input("---- Okay cool! Input the temperature in farenheit: "))#if yes then it will ask for the users degree
    finalValue = (degree - 32) * 5/9# will do the math to convert the temperature from farenhiet to celsius
    print("---- Temperature Converted Successfuly {:.2f}".format(finalValue))#return the final value back to user
elif decision.lower() == "no": #if no check
    decision = input("---- Okay would you like to do celsius to farenheit? Yes/No ")#ask if they would like to do celsius to farenheit
    if decision.lower() == "yes":#if yes then retrieve the degree from the user
        degree = float(input("---- Okay cool! Input the temperature in celsius: "))
        finalValue = (degree * 9/5) + 32#then do the math to convert it
        print("---- Temperature Converted Successfuly {:.2f}".format(finalValue))#then return the final temp after conversion
    elif decision.lower() == "no":#if no say goodbye and close the application
        print("---- Okay goodbye! ")      
else:#if they put anything else it will sayd wrong input goodbye and then exit the application
    print("---- Wrong Input Goodbye")
    
    
        
