Employee = {
    "Name" : "Vignesh",
    "Email" : "vicky0220@gmail.com",
    "Age" : 29,
    "Gender" : "Male",
    "Birthday" : "02|08|1996",
    "Designation" : "Software engineer",
    "Salary" : 40000,
    "Favorite food" : ["Dosa","Biriyani","Prawn fry"]
}
print(Employee["Birthday"])
print(Employee.get("Age"))

print(Employee.keys())

print(Employee.values())

for key, value in Employee.items():
    print(key,":",value)

Employee.update({"Employee location" : "Chennai"})
print(Employee)

Employee.pop("Gender")
print(Employee)

print(Employee["Favorite food"][1])

for food in Employee["Favorite food"]:
    print(food)

trips= {
    "AB1234": {"trip_id":"AB1234", "pickup": "Porur", "drop": "Koyambedu", "fare": 350},
    "BA1234": {"trip_id":"BA1234", "pickup": "Tambaram", "drop": "Guindy", "fare": 450},
    "CD1234": {"trip_id":"CD1234", "pickup": "Pallavaram", "drop": "Chrompet", "fare": 550}
}

print(trips)

print(trips["AB1234"]["pickup"])

print("AB1234 fare", trips["AB1234"]["fare"])


for trip_id, details in trips.items():
  print(trip_id)
  print(details["pickup"],"-->",details["drop"])