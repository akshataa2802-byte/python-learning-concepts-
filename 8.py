birthday={
    "akshata":"28-02-2005",
    "abhishek":"08-01-2006",
    "pooja":"13-08-2006"
}
print(birthday)
print(birthday["akshata"])
print(type(birthday))
print(birthday.get("chandan","not found"))
birthday["harsha"]="19-11-2013"
print(birthday)
birthday.pop("harsha")
print(birthday)
print(birthday.keys())
print(birthday.values())
print(birthday.items())

