country = input("Enter African country: ")
gdp_per_capita = float(input("Enter GDP per capita: "))

if gdp_per_capita < 1500:
    category = "Low income"
elif gdp_per_capita < 5000:
    category = "Middle income"
else:
    category = "High income"

print(country, "is classified as:", category)