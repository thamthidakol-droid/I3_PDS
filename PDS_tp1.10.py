# ---------------------------------------------------------------------------
#Problem 9: Electricity Bill with Progressive Tiers
# ---------------------------------------------------------------------------
#Part A:
def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    charge = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)

    total = (charge + 2000) * 1.10
    return round(total)

# Part B: Print the electricity bill table
consumptions = [0, 35, 50, 120, 200, 350]

for kwh in consumptions:
    bill = electricity_bill(kwh)
    usd = bill / 4100

    print(f"{kwh} kWh -> {bill:,} riel (~ {usd:.2f} USD)")

# Part C: Ask the user for consumption
try:
    kwh = float(input("\nEnter your monthly consumption (kWh): "))

    bill = electricity_bill(kwh)

    if bill is None:
        print("Invalid consumption!")
    else:
        print(f"Your electricity bill is {bill:,} riel.")

except ValueError:
    print("Please enter a valid number.")