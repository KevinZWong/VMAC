# Script Management Ai Complier
from SMAC.TopicTreeOOP import TopicTree
import os
import json


def create_unique_filename(base_path, filename):
    counter = 1
    unique_filename = filename

    # Check if the file already exists
    while os.path.exists(os.path.join(base_path, unique_filename)):
        # If it exists, append a number to the filename
        unique_filename = f"{filename}_{counter}"
        counter += 1

    return os.path.join(base_path, unique_filename)

try:
    current_directory = os.getcwd()
    if os.path.basename(current_directory) != 'VMAC':
        raise Exception("Current directory is not 'VMAC'.")
    print("Current directory is 'VMAC'.")

except Exception as e:
    print(f"Error: {e}")

while(True):
    print("0. Exit")
    print("1. Fully Generate")
    print("2. Add Prompt")
    selection1 = input("Enter a number:")
    if selection1 == "0":
        exit()
    elif selection1 == "1":
        topic = input("Enter a base topic:")
        subtopicLevels = int(input("Enter number of subtopic levels:"))
        subtopicsChildren = int(input("Enter a number of child topics per node:"))
        #style = input("Enter style of topics.")
        filename = input("Enter filename for data (default is the topic name): ")
        if filename == "":
            filename = topic
        root = TopicTree(topic)
        # Expand the tree for subtopicLevels levels with each node having subtopics children
        root.expand_recursively_helper(subtopicLevels, subtopicsChildren)

        leaves = root.get_leaf_nodes()
        AllTopics = []
        for i in leaves:
            AllTopics.append(i.topic)
        AllTopics = [item.replace('\"', '') for item in AllTopics]
        base_path = "Topics/Prepared"
        filePath = create_unique_filename(base_path, filename)
        with open(f"{filePath}.json", "w") as file:
            json.dump(AllTopics, file, indent=4)
        print(f"{filePath}.json created\n")
    elif selection1 == "2":
        user_input = input("Enter prompt: ")
        filename = "Prompts/" + input("Enter filename: ") + ".json"
        data = {"prompt": user_input}
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    else:
        print("Invalid selection. Please enter a number between 1 and 4.")

