def search_prospects(query, prospects_list):
    """
    Search for the query in the given prospects list.

    :param query: The search query (full name).
    :type query: str
    :param prospects_list: List of dictionaries containing prospect information.
    :type prospects_list: list
    :return: List of matching prospects.
    :rtype: list
    """
    query = query.lower()
    matches = [prospect for prospect in prospects_list if query in prospect['name'].lower()]
    return matches


def print_matches(matches):
    """
    Print the matching prospects.

    :param matches: List of matching prospects.
    :type matches: list
    """
    if not matches:
        print("No matches found.")
    else:
        print("Match found:")
        for prospect in matches:
            print("Name:", prospect['name'], "\nEmail:", prospect['email'], "\nPhone:", prospect['phone'], "\n")


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
matches = search_prospects(query, prospects)

# Print the matching prospects
print_matches(matches)
