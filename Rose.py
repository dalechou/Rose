import base64, linecache

# Grab source_name.
target_order = 0
source_name = input("Enter a name: ")
list_of_names = r"census-derived-all-first.txt"

# Encode source_name.
for encoded_char in base64.b64encode(bytes(source_name, "utf-8")):
    target_order = target_order + encoded_char

# Pick a name.
target_order = target_order % len(open(list_of_names).readlines())
print("Recommended pseudonym: " + linecache.getline(list_of_names, target_order).partition(" ")[0])
