print("=== CARBON FOOTPRINT CALCULATOR ===")

distance = float(input("Enter daily travel distance (km): "))
emission_factor = 0.21

carbon_footprint = distance * emission_factor

print("\nTotal Carbon Footprint:",
      round(carbon_footprint, 2), "kg CO2e")
