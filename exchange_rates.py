# Exchange rates (example values)
ugx_to_kes = 0.035
ugx_to_tzs = 0.64

amount_ugx = float(input("Enter amount in UGX: "))

kes = amount_ugx * ugx_to_kes
tzs = amount_ugx * ugx_to_tzs

print("In Kenyan Shillings:", kes)
print("In Tanzanian Shillings:", tzs)