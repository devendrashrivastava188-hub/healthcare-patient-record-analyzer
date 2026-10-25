#Healthcare patient record Analyzer
#I made this project to practice python data handling with healthcare-related data.
#I created a list to store the patient records-

Patients = [
    #I created the first patient's record
    {
        #I gave the patient an id number
        "id": 101,
        #I stored the patient's name
        "name": "Rahul",
        #I stored the patient's age
        "age": 22,
        #I stored the patient's department
        "department": "General Medicine"
        },
    #I created the second patient's record
    {
        "id": 102,
        "name": "Anjali",
        "age": 25,
        "department": "Dermatology"
        },
    #I created the third patient's record
    {
        "id": 103,
        "name": "Aman",
        "age": 30,
        "department": "Cardiology"
        },
    #I created the fourth patient's record

    {
        "id": 104,
        "name": "Aman",
        "age": 28,
        "department": "General Medicine"
        },
    ]
#I displayed the project title on the screen
print("--- Helthcare Patient Record Analyzer ---")

#I counted the total number of patients in the list
#len() tells me how many patient records are present
print("\nTotal Patients:",len(Patients))

#I created a variable to store the total age of all patients
total_age = 0

#I used a for loop to go through each patient record
for Patient in Patients:

    #I added each patient's age to the total age    
    total_age = total_age + Patient["age"]
    
#I calculated the average age of all patients    
average_age = total_age/len(Patients)

#I displayed the average age on the screen
print("Average Age:", average_age)

#I asked the user to enter the patient ID they want to search
search_id = int(input("\nEnter Patient Id to search: "))

#I created a variable to remember whether the patient was found
# False means the patient has not been found yet
found = False

#I used a for loop to check each patient record
for Patient in Patients:
    
    #I compared the entered ID with the current patient's ID 
    if Patient["id"] == search_id:

        #I displayed a massage when the patient was found
        print("\n---Patient Record Found ---")
        print("Patient Id:",Patient["id"])
        print("Name:",Patient["name"])
        print("Age:",Patient["age"])
        print("Department",Patient["department"])

        #I changed found to True because the patient was found
        found = True

        #I stopped the loop because the required patient was found
        break

#I displayed this massage was not found    
if found == False:
    #I displayed this massage when no matching patient ID was found
    print("\nPatient record not found,")
        

            
            
                                
        
