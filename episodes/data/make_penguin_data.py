# Running this script with the variables below pointing to the appropriate files will produce the palmer_penguin_data.csv file for use in the lesson.
import random
import pandas as pd
import urllib.request

# Path to the file containing names to assign to the penguins
# Names file sourced from: https://github.com/imsky/wordlists/tree/master, Chicago street names.
name_file = urllib.request.urlopen(
    "https://raw.githubusercontent.com/imsky/wordlists/master/names/streets/chicago.txt"
)
potential_names = name_file.read().decode("utf-8").split("\n")
name_file.close()

# Path to the raw .csv Palmer Penguins data
# Palmer penguin data sourced from https://github.com/allisonhorst/palmerpenguins/tree/main
# citation("palmerpenguins")
# >
# > To cite palmerpenguins in publications use:
# >
# >   Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer
# >   Archipelago (Antarctica) penguin data. R package version 0.1.0.
# >   https://allisonhorst.github.io/palmerpenguins/. doi:
# >   10.5281/zenodo.3960218.
# >
# > A BibTeX entry for LaTeX users is
# >
# >   @Manual{,
# >     title = {palmerpenguins: Palmer Archipelago (Antarctica) penguin data},
# >     author = {Allison Marie Horst and Alison Presmanes Hill and Kristen B Gorman},
# >     year = {2020},
# >     note = {R package version 0.1.0},
# >     doi = {10.5281/zenodo.3960218},
# >     url = {https://allisonhorst.github.io/palmerpenguins/},
# >   }
penguin_file = urllib.request.urlopen(
    "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins_raw.csv"
)
penguin_data = pd.read_csv(penguin_file)
penguin_file.close()

cols_to_drop = sorted(
    [
        "studyName",
        "Region",
        "Island",
        "Stage",
        "Date Egg",
        "Sex",
        "Sample Number",
        "Comments",
        "Delta 15 N (o/oo)",
        "Delta 13 C (o/oo)",
        "Clutch Completion",
    ]
)

penguin_data.drop(cols_to_drop, axis="columns", inplace=True)

# Drop the Latin species name, but keep the species
penguin_data.loc[:, "Species"] = penguin_data.loc[:, "Species"].str.split(n=1).str[0]
# Convert body mass to SI kg
penguin_data.loc[:, "Body Mass (g)"] /= 1000.0
penguin_data.rename(
    columns={
        "Body Mass (g)": "Mass (kg)",
        "Individual ID": "ID",
    },
    inplace=True,
)

# Drop all rows with NaNs so that the lesson doesn't have to deal with those
penguin_data.dropna(axis="rows", inplace=True)

# Give remaining penguins names
# with open(name_file) as file:
#     potential_names = [line.rstrip() for line in file]
selected_names = random.sample(range(0, len(potential_names)), penguin_data.shape[0])
selected_names = [potential_names[i] for i in selected_names]
penguin_data["name"] = selected_names

# All headers to lowercase
penguin_data.columns = penguin_data.columns.str.lower()
# Order columns alphabetically, but move ID, name, and species to the front
ordered_columns = sorted(penguin_data.columns)
ordered_columns.remove("id")
ordered_columns.remove("species")
ordered_columns.remove("name")
ordered_columns.insert(0, "id")
ordered_columns.insert(1, "name")
ordered_columns.insert(2, "species")
penguin_data = penguin_data[ordered_columns]

# Mix up the dataset so that it doesn't appear ordered (so you can't index slice to get all of one species, for example)
penguin_data = penguin_data.sample(frac=1, axis="rows")

# Write to data file
penguin_data.to_csv("penguin_data.csv", index=False)
