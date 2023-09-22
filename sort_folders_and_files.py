import requests

def get_creation_date(owner, repo, path):
    """Gets the creation date of a file or folder in a GitHub repository.

    Args:
        owner: The owner of the repository.
        repo: The name of the repository.
        path: The path to the file or folder in the repository.

    Returns:
        The creation date of the file or folder as a timestamp (UNIX epoch).
    """
    
    # Get commit information for the specified path.
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits', params={'path': path})

    # Convert the response to a JSON object.
    json_response = response.json()

    # Check if there are commits for the specified path.
    if json_response:
        # Get the timestamp of the first commit for the path.
        creation_date = json_response[0]['commit']['committer']['date']
        return creation_date

    # If there are no commits, return None.
    return None

def sort_folders_and_files_by_creation_date(owner, repo, folder):
    """Sorts the folders and files in a GitHub repository by creation date.

    Args:
        owner: The owner of the repository.
        repo: The name of the repository.
        folder: The subfolder within the repository.

    Returns:
        A list of folders and files sorted by creation date in ascending order.
    """
    
    # Get the list of files and folders in the repository.
    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/contents/{folder}')

    # Convert the response to a JSON object.
    json_response = response.json()

    # Create a list to store items with their creation dates.
    items_with_creation_dates = []

    # Retrieve the creation date for each file or folder.
    for item in json_response:
        item_path = item['path']
        creation_date = get_creation_date(owner, repo, item_path)
        if creation_date is not None:
            items_with_creation_dates.append((item, creation_date))

    # Sort the items by creation date in ascending order.
    sorted_items = sorted(items_with_creation_dates, key=lambda x: x[1], reverse=False)

    # Extract the items without creation dates for the final result.
    files_and_folders = [item[0] for item in sorted_items]

    return files_and_folders

# Example usage:
files_and_folders = sort_folders_and_files_by_creation_date('hemanthbabu164', 'DSA-Challenge', 'CHB')

# Print the files and folders in the repository.
for file_or_folder in files_and_folders:
    print(file_or_folder['name'])
