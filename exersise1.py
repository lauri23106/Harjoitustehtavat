# 1. Create a list and assign furniture as values (like table, chair, shelf...).
furniture_list = ["table", "chair", "shelf", "sofa", "bed", "desk"]

# 2. Print the whole list.
print("Whole list of furniture:")
print(furniture_list)

# 3. Print only the first two elements of the list.
print("First two elements of the list:")
print(furniture_list[:2])

# 4. Print "Sofa" if it is found in the list.
print("Checking for 'Sofa' in the list:")
found_sofa = False

for item in furniture_list:
    if item == "sofa" or item == "Sofa":
        print("Sofa")
        found_sofa = True

if not found_sofa:
    print("Sofa not found in the list")
