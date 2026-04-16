capitals = {
    "Uganda": "Kampala",
    "Kenya": "Nairobi",
    "Tanzania": "Dodoma",
    "Rwanda": "Kigali",
    "Ghana": "Accra",
    "Nigeria": "Abuja",
    "Ethiopia": "Addis Ababa",
    "Egypt": "Cairo",
    "South Africa": "Pretoria",
    "Senegal": "Dakar"
}

country = input("Enter country name: ")

if country in capitals:
    print("Capital:", capitals[country])
else:
    print("Country not found")