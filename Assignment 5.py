# Q1. File Handling - Write and Read Names
# 1. Open a file "names.txt" in write mode
# 2. Write 5 names (one per line) entered by the user
# 3. Then open the same file in read mode and print all names


with open('C:/Users/rushi/Downloads/names.txt','w') as f:
    for _ in range(5):
        names=input('enter your name')
        f.write(f'{names}\n')
        




# 2
with open('C:/Users/rushi/Downloads/names.txt','w+') as f:
    for _ in range(5):
        names=input('enter your name')
        f.write(f'{names}\n')
        
    f.seek(0)
    print(f.read())



# Q2. File Handling - Append Logs
# 1. Open a file "log.txt" in append mode
# 2. Add a new log entry (like "Program run successfully")
# 3. Open the file in read mode and print all logs


with open('C:/Users/rushi/Downloads/logs.txt','a+') as f:
    
    f.write('prgram run successfully')
    f.seek(0)
    print(f.read())
    

    
    

# Q3. List Comprehension
# 1. Have a list of numbers: [5, 10, 15, 20, 25]
# 2. Use a list comprehension to create a new list with only numbers greater than 15
# 3. Print the new list

nums=[5, 10, 15, 20, 25]

new_list=[ value for value in nums if value >15]

print(new_list)


# Q4. Dictionary + JSON
# 1. Create a Python dictionary of 3 cities and their populations
# 2. Save it to "cities.json"
# 3. Load the JSON and print each city and its population
# 4. Ask the user for a new city & its population - update this info in the json file


import json

data={'delhi':123,
      'karad':345,
      'kolhapur':678
      }

with open('C:/Users/rushi/Downloads/city.json','w+') as f:
    
    json.dump(data,f,indent=4)
    f.seek(0)
    pyth_obj=json.load(f)
    print(type(pyth_obj))
    print(pyth_obj)
    
with open('C:/Users/rushi/Downloads/city.json','w') as f:
    
    city=input('enter your city name')
    population=input('enter your population')
    
    pyth_obj[city]=population
    print(pyth_obj)
    json.dump(pyth_obj,f,indent=4,sort_keys=True)

    
# Q5. Exception Handling
# 1. Try to open "data.txt" in read mode
# 2. If the file does not exist, catch the exception
# 3. Print "File not found!"

try:
    with open('C:/Users/rushi/Downloads/city.json') as f:
        data=f.read()

except FileNotFoundError:
    
    print('File not found!')

else:
    print(data)

finally:
    
    print('completed the opeartaion')
    
 
i=0

while i<10:
   i+=1
   if( i % 6 ==0):
      break
   print(i)
   
print("outside of loop",i)


def sum(a,b):
   calcculate=a+b
   return calcculate

a=sum
print(a(3,5)) # we can store function n variable
print(sum(1,2),a)




