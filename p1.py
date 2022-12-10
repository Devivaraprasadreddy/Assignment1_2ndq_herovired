# Create a dictionary name as car and insert some keys and values
# Take input from user as brandname of car
# Take another input from user as color of car

car = {'bmw' : 'blue', 'honda' : 'red', 'toyota' : 'white', 'skoda' : 'white', 'duster' : 'black', 'renault' : 'orange'}
b_name = raw_input("Please specify your Brandname of car: ")
color = raw_input("Please specify your color of car: ")

# Write some loop for dictionary
# check the condition 
# 'if' conditon says enter the user brandname is there in dictionary or not
# if it is there then proceed the next steps 
# otherwise it will goes to the elif condition
# in this case also not matched go to next and so on
# lastly goes to else block and execute the block 


for i in car:
    if b_name=='bmw':
        print("The Brandname And Color Of Car Data Is :::: ")
        print(" The  Brandname Of Car Is : ")
        print(b_name.upper()) 
        print("The Color Of Car Is : ")
        print(color.upper())
        print("The Data Is In Dictionary Format : ")
        dict[b_name] = color
        print(dict)
       
 # The output data will be send to data.txt file using file handling concept 
       
        x = open('data.txt',"a")
        x.write(str("The Car Data  Is : "))
        x.write(str("\n"))
        x.write(str(b_name))
        x.write(str("\n"))
        x.write(str(color))
        x.write(str("\n"))
        x.write(str("The brandname And Color Of Car Data Is ::: "))
        x.write(str('\n'))
        x.write(str("   The Brandname Of Car Is :  "))
        x.write(str.upper(b_name))
        x.write(str('\n'))
        x.write(str("   The Color Of Car Is : "))
        x.write(str.upper(color))

#create one empty dictionary beacuse the output data will append to the empty dictionary and send to the file easily

        dict ={}
        
# here break we are using stop the condition beacuse for loop is conitinous loop it will exexute until the conidition will be true but i want if the condition is true it will stops the operation so i'm using break condition.
 
        break
    elif b_name=='honda':
        print("The Brandname And Color Of Car Data Is :::: ")
        print(" The  Brandname Of Car Is : ")
        print(b_name.upper()) 
        print("The Color Of Car Is : ")
        print(color.upper())
        print("The Data Is In Dictionary Format : ")
        dict[b_name] = color
        print(dict)

# The output data will be send to data.txt file using file handling concept 

        x = open('data.txt',"a")
        x.write(str("The Car Data  Is : "))
        x.write(str("\n"))
        x.write(str(b_name))
        x.write(str("\n"))
        x.write(str(color))
        x.write(str("\n"))
        x.write(str("The brandname And Color Of Car Data Is ::: "))
        x.write(str('\n'))
        x.write(str("   The Brandname Of Car Is :  "))
        x.write(str.upper(b_name))
        x.write(str('\n'))
        x.write(str("   The Color Of Car Is : "))
        x.write(str.upper(color))

        dict ={}
        break
    elif b_name=='toyota':
        print("The Brandname And Color Of Car Data Is :::: ")
        print(" The  Brandname Of Car Is : ")
        print(b_name.upper()) 
        print("The Color Of Car Is : ")
        print(color.upper())
        print("The Data Is In Dictionary Format : ")
        dict[b_name] = color
        print(dict)

# The output data will be send to data.txt file using file handling concept 

        x = open('data.txt',"a")
        x.write(str("The Car Data  Is : "))
        x.write(str("\n"))
        x.write(str(b_name))
        x.write(str("\n"))
        x.write(str(color))
        x.write(str("\n"))
        x.write(str("The brandname And Color Of Car Data Is ::: "))
        x.write(str('\n'))
        x.write(str("   The Brandname Of Car Is :  "))
        x.write(str.upper(b_name))
        x.write(str('\n'))
        x.write(str("   The Color Of Car Is : "))
        x.write(str.upper(color))

        dict ={}
        break
    elif b_name=='skoda':
        print("The Brandname And Color Of Car Data Is :::: ")
        print(" The  Brandname Of Car Is : ")
        print(b_name.upper()) 
        print("The Color Of Car Is : ")
        print(color.upper())
        print("The Data Is In Dictionary Format : ")
        dict[b_name] = color
        print(dict)

# The output data will be send to data.txt file using file handling concept 

        x = open('data.txt',"a")
        x.write(str("The Car Data  Is : "))
        x.write(str("\n"))
        x.write(str(b_name))
        x.write(str("\n"))
        x.write(str(color))
        x.write(str("\n"))
        x.write(str("The brandname And Color Of Car Data Is ::: "))
        x.write(str('\n'))
        x.write(str("   The Brandname Of Car Is :  "))
        x.write(str.upper(b_name))
        x.write(str('\n'))
        x.write(str("   The Color Of Car Is : "))
        x.write(str.upper(color))

        dict ={}
        break
    elif b_name=='duster':
        print("The Brandname And Color Of Car Data Is :::: ")
        print(" The  Brandname Of Car Is : ")
        print(b_name.upper()) 
        print("The Color Of Car Is : ")
        print(color.upper())
        print("The Data Is In Dictionary Format : ")
        dict[b_name] = color
        print(dict)

# The output data will be send to data.txt file using file handling concept 

        x = open('data.txt',"a")
        x.write(str("The Car Data  Is : "))
        x.write(str("\n"))
        x.write(str(b_name))
        x.write(str("\n"))
        x.write(str(color))
        x.write(str("\n"))
        x.write(str("The brandname And Color Of Car Data Is ::: "))
        x.write(str('\n'))
        x.write(str("   The Brandname Of Car Is :  "))
        x.write(str.upper(b_name))
        x.write(str('\n'))
        x.write(str("   The Color Of Car Is : "))
        x.write(str.upper(color))

        dict ={}
        break
    elif b_name=='renault':
        print("The Brandname And Color Of Car Data Is :::: ")
        print(" The  Brandname Of Car Is : ")
        print(b_name.upper()) 
        print("The Color Of Car Is : ")
        print(color.upper())
        print("The Data Is In Dictionary Format : ")
        dict[b_name] = color
        print(dict)

# The output data will be send to data.txt file using file handling concept 

        x = open('data.txt',"a")
        x.write(str("The Car Data  Is : "))
        x.write(str("\n"))
        x.write(str(b_name))
        x.write(str("\n"))
        x.write(str(color))
        x.write(str("\n"))
        x.write(str("The brandname And Color Of Car Data Is ::: "))
        x.write(str('\n'))
        x.write(str("   The Brandname Of Car Is :  "))
        x.write(str.upper(b_name))
        x.write(str('\n'))
        x.write(str("   The Color Of Car Is : "))
        x.write(str.upper(color))

        dict ={}
        break
    else:
        dict = {}
        print("The Brandname and Car is : ")
        print("Brandname Of Car Is : ")
        print(b_name.upper())
        print("Color Of Car Is : ")
        print(color.upper())
        dict[b_name] = color
        print("The Data Is In Dictionary Format : ")
        print(dict)
        print("Data Not Found!")

# The output data will be send to data.txt file using file handling concept 

        x= open("data.txt","a")
        x.write(str("Brandname And Color Of Car Data Is Not Found!"))
        x.write(str('\n'))
        x.write(str(b_name))
        x.write(str("\n"))
        x.write(str(color))
        x.write(str("\n"))
        x.write(str("Condition : Please Enter Correct Data! "))
        break
       


  