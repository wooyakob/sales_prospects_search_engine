# Define a list of sales prospects
prospects = [
    {'name': 'John Smith', 'company': 'ABC Corp', 'email': 'john.smith@abccorp.com', 'phone': '123-456-7890'},
    {'name': 'Jane Doe', 'company': 'XYZ Inc', 'email': 'jane.doe@xyzinc.com', 'phone': '234-567-8901'},
    {'name': 'Bob Johnson', 'company': 'ACME Corp', 'email': 'bob.johnson@acmecorp.com', 'phone': '345-678-9012'},
    {'name': 'Alice Lee', 'company': 'Foo Bar Inc', 'email': 'alice.lee@foobar.com', 'phone': '456-789-0123'}
]

# Get the search query from the user
query = input("Enter the prospect's full name: ")

# Search for the query in the prospects list
matches = []
for prospect in prospects:
    if query.lower() in prospect['name'].lower() or query.lower() in prospect['email'].lower() or query in prospect['phone']:
        matches.append(prospect)

# Print the matching prospects
if len(matches) == 0:
    print("No matches found.")
else:
    print("Matches found:")
    for prospect in matches:
        print(prospect['name'], '-', prospect['company'], '-', prospect['email'], '-', prospect['phone'])

