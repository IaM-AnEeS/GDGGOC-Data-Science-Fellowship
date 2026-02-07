students={
    "001":{"name":"Muhammad Ahmad","age":23,"city":"Karachi","grade":"A"},
    "002":{"name":"Anees Ahmad","age":23,"city":"Islamabad", "grade":"B+"},
    "003":{"name":"Usman Ahmad","age":33,"city":"Riyadh", "grade":"C"},
    "004":{"name":"Waleed Ahmad","age":25,"city":"Jubail", "grade":"A+"},
    "005":{"name":"Muhammad Abdullah Azhar","age":23,"city":"Attock", "grade":"A"},
    "006":{"name":"Ali Haider","age":23,"city":"Swat", "grade":"c-"},
    "007":{"name":"Abdul Moiz Muhammad","age":23,"city":"Wah Cantt", "grade":"D"},
    "008":{"name":"Qaiser Mehmood","age":35,"city":"London", "grade":"B-"},
    "009":{"name":"Nasir Mehmood","age":43,"city":"Jubail", "grade":"A-"},  
}

## Accessing Dictionary elements
print(students['001']['name'])
print(students['003']['city'])

## Accessing using get() method
print(students['004'].get('grade'))
print(students['005'].get('age'))
print(students['006'].get('name'))


## Modifying Dicitonary Elements
## Dictionary are mutable,so you can add, update or delete elements
print(students)

students['002']["age"]=33  ##update value for the key
print(students)
students['002']["address"]="Berlin" ## added a new key and value to student 002
print(students)

del students['002']['grade'] ## delete key and value pair

print(students)

## Iterating over nested dictionaries
for student_id, student_info in students.items():
    print(f"\nStudent ID: {student_id}")
    for key, value in student_info.items():
        print(f"{key.capitalize()}: {value}")