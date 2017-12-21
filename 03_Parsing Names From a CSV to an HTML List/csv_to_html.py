import csv

html_output = ''
names = []
# Using reader method ...

# with open('patrons.csv', 'r') as file:
#     csv_data = csv.reader(file)
#     # skip headers and first line of the csv data
#     next(csv_data)
#     next(csv_data)
#     for line in csv_data:
#         if line[0] == 'No Reward':
#             break
#         names.append(f"{line[0]} {line[1]}")  # append first and last name from line (list)
#
# html_output += f"<p>There are currently {len(names)} contributors. Big up! </p>"
# html_output += '\n<ul>'
#
# for name in names:
#     html_output += f"\n\t<li>{name}</li>"
#
# html_output += '\n</ul>'
#
# print(html_output)


# using DictReader method ...
with open('patrons.csv', 'r') as file:
    csv_data = csv.DictReader(file) # turns each line into a dictionary instead of a list

    next(csv_data) # skip over first value
    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f"<p>There are currently {len(names)} contributors. Big up! </p>"
html_output += '\n<ul>'

for name in names:
    html_output += f"\n\t<li>{name}</li>"

html_output += '\n</ul>'

# Generate HTML code
print(html_output)
