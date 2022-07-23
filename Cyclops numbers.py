while True:
    num =input(' Enetr your number: ')
    
   #checking the num is negative or not
    if not num.isnumeric():
        print('please enter an integer number')
    elif int(num)<0:
       print('please enter a posetive number')
    elif len(str(num))%2 == 0:
       print('your lenght of number must be odd')

    else: 
        break
    
len_list = len(str(num))
middle_index = int((len_list-1) / 2)
both_mid = num[:middle_index] + num[middle_index+1:]

      
flag = 0

if (int(num[middle_index])) == 0:
    for digit in both_mid:
        if (int(digit)) == 0:
            print('false')
            flag =1 
            break
    if flag == 0 :
        print ("True\n")
else:
    print('false')

        
    



    
        
