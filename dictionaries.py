# Dictionaries can store keys and values
# {} are used for dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    12: "December",
}


print(monthConversions["Nov"])
print(monthConversions[12])
print(monthConversions.get("Oct"))
print(monthConversions.get("Apr", "Not a valid key"))
print(monthConversions.get("Joe", "Not a valid key"))
