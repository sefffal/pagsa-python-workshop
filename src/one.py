target_names = ["M31", "Sgr A*"]
catalog = [...] #... some table from pandas/astropy

found_row = None
for i in range(len(taget_names)):
    for j in range(len(catalog)):
        row = catalog[j]
        if row["name"] == target_names[i]:
            found_row = row
# Now do something with found_row




