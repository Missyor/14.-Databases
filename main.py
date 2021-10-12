# ###Create a CSV file

# file = open("myCSVFile.csv", "w")
# file.write("1, 2, 4, 3, 5")
# file.close()

# ###Read CSV file
# file = open("myCSVFile.csv", "r")
# dataIn = file.read()
# file.close() 
# print(dataIn)

# myList = dataIn.split(",")
# print(myList)

###Sorting data

# myList = [1, 3, 2, 5, 4]
# myList.sort()
# print("Ascending order: ", myList)
# myList.sort(reverse = True)
# print("Descending order: ", myList)

# ##Removing Data

# numbers = [-19, 1, -19, 2, -4]

# for i in numbers:
#   if i < 0:
#     numbers.remove(i)
# print(numbers)

# numbers = [-19, 1, -19, 2, -4, 5]

# numbers.remove(-19)
# print(numbers)

# ##Imputation - replacing errors in a database

# totalNonErrors = 0
# nonErrorCount = 0
# for i in numbers:
#   if i >= 0:
#     totalNonErrors += i
#     nonErrorCount += 1
    
# averageNum = totalNonErrors/nonErrorCount

# print(round(averageNum, 2))

# ##replacing data with an average
# for counter in range(len(numbers)):
#   if numbers[counter] < 0:
#     numbers[counter] = round(averageNum, 2)
# print(numbers)    

# ###Analysis

##Min & Max values

# myList = [1, 19, 27, 8, 5, 9, 1, 1]
# myList.sort()
# maxValue = myList[0]
# minValue = myList[-1]
# print(minValue)
# print(maxValue)

# ##Averages

# ##Mean

# average = sum(myList)/len(myList)
# print(myList)

# import statistics

# average = statistics.mean(myList)
# print(average)

### Median - middle number when data is sorted

# import statistics

# median = statistics.median(myList)
# print(median)

# ### Mode = most commen element

# import statistics

# mode = statistics.mode(myList)
# print(mode)







#Creating  a database

# import csv 
#lets us create a csv file

# header = ["firstName", "lastName", "phoneNum", "dob", "age"]
# ## create a csv file called patients. "a" lets us add info to our database
# file = open("patients.csv", "a", newline = "")

##create connection to patients.csv
# db = csv.writer(file)

# ##writes header list to the csv file
# db.writerow(header)

# ## close the file
# file.close()

# import csv

# ##create lists and append them to the csv file - could be created from user inputs
# record1 = ["Joan", "Byrne", "098", "2/2/75", "45"]
# record2 = ["Gideon", "Jones", "888", "4/7/59", "61"]
# file = open("patients.csv", "a", newline = "")

# db=csv.writer(file)
# db.writerow(record1)
# db.writerow(record2)
# file.close()

# import csv
# file = open("patients.csv", "r")
# records = list(csv.reader(file))
# file.close()
# print(records)

# import csv
# # file = open("patients.csv", "r")
# # records = list(csv.reader(file))
# # file.close() 
# # for record in records:
# #   print(record)

# file = open("patients.csv", "r")
# records = list(csv.reader(file))
# file.close() 
# print("First Name\t Last Name\t Phone Number\t DOB\t Age")
# print("------------------------------------------------")
# for record in records[1:]:
#   print(record[0]),"\t\t",record[1]  

# import csv
# file = open("patients.csv", "r")
# records = list(csv.reader(file))
# file.close() 
# for record in records[1:]:
#   print(record[4])

##page 249

 #Create a database (csv file) with  headings make, model and reg. Call it myGarage.csv. Enter 3 records

# import csv
# header = ["make", "model", "reg"]
# file = open("myGarage1.csv", "a", newline = "")
# db = csv.writer(file)

# db.writerow(header)

# file.close()

# record1 = ["Renault", "Magane", "01D2222"]
# record2 = ["Nissan", "Micra", "121D3214"]
# record3 = ["Fiat", "Punto", "12D335"]

# file = open("myGarage1.csv", "a", newline = "")

# db = csv.writer(file)
# db.writerow(record1)
# db.writerow(record2)
# db.writerow(record3)

# file = open("myGarage1.csv", "r")
# records = list(csv.reader(file))
# file.close()
# print(records)
# for record in records:
#   print(record)

# import csv

# ##open
# header = ["Name", "Profession"]

# file = open("personel.csv", "a", newline = "")


# db = csv.writer(file)

# db.writerow(header)

# db = csv.writer(file)

# record1 = ['Derek', 'Software Developer']
# record2 = ['Steve', 'Software Developer']
# record3 = ['Jane', 'Manger']

# db=csv.writer(file)

# db.writerow(record1)
# db.writerow(record2)
# db.writerow(record3)

# file = open("personel.csv", "r")
# records = list(csv.reader(file))
# file.close()
# print(records)

# file = open("personel.csv", "r") 

# records = list(csv.reader(file)) 

# file.close() 

# for record in records: 
#   print(record) 



# import csv

# header = ["Make", "Model", "Reg"]

# file = open("myGarage2.csv", "a", newline = "")

# record1 = ["Nissan", "Micra", "jkiv99"]
# record2 = ["Opel", "Corsa", "t78gu"]
# record3 = ["Ford", "Focus", "6789pgu"]

# db = csv.writer(file)
# db.writerow(header)
# db.writerow(record1)
# db.writerow(record2)
# db.writerow(record3)

# file.close()

# file = open("myGarage2.csv", "r")
# records = list(csv.reader(file))
# file.close()

# print(records)