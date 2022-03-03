a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False
a_none = None

print(type(a_number))

days = ["Mon","Tue","Wed","Thur","Fri"]
print(days[2])

print("Mon" in days)
print(len(days))

print(days)
days.append("Sat")
days.reverse()
print(days)

days_tuple = ("Mon","Tue","Wed","Thur","Fri")
print(type(days_tuple))




nico = {
  "name" : "Nico",
  "age" : 29,
  "Korean" : True,
  "fav_food" : ["Kimchi","Sashmi"]
}

print(nico["name"])
print(nico["fav_food"])
nico["handsome"] = True
print(nico)
print(type(nico))