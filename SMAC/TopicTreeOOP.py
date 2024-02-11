from ScriptP.ScriptGenerationOOP import ScriptGenerator
import os
import json

class TopicTree:
    def __init__(self, topic):
        self.topic = topic
        self.children = []
        self.ScriptGen = ScriptGenerator()

    def add_child(self, child):
        self.children.append(child)

    def expand_recursively_helper(self, levels, num_children, level=0):
        if levels <= 0:
            return
        subtopicsList = self.ScriptGen.generate_topics(self.topic, num_children)
        subtopicsList = subtopicsList.split(",")
        for i, subtopic in enumerate(subtopicsList):
            indent = "  " * level
            print(f"{indent}Generated Level {levels}: {subtopic}")
            child = TopicTree(f"{subtopic}")
            self.add_child(child)
            child.expand_recursively(levels - 1, num_children, subtopic, level + 1)

    def expand_recursively(self, levels, num_children, given_subtopic, level=0):
        if levels <= 0:
            return
        subtopicsList = self.ScriptGen.generate_topics(given_subtopic, num_children)
        subtopicsList = subtopicsList.split(",")
        for i, subtopic in enumerate(subtopicsList):
            indent = "  " * level
            print(f"{indent}Generated Level {levels}: {subtopic}")
            child = TopicTree(f"{subtopic}")
            self.add_child(child)
            child.expand_recursively(levels - 1, num_children, subtopic, level + 1)


    def save_to_file(self, filename):
        def serialize(node):
            return {'topic': node.topic, 'children': [serialize(child) for child in node.children]}

        with open(filename, 'w') as file:
            json.dump(serialize(self), file, indent=4)
    @staticmethod
    def load_from_file(filename):
        def deserialize(node_data):
            node = TopicTree(node_data['topic'])
            for child_data in node_data['children']:
                node.add_child(deserialize(child_data))
            return node

        with open(filename, 'r') as file:
            data = json.load(file)
            return deserialize(data)
    def get_leaf_nodes(self):
        """
        Retrieves all leaf nodes in the tree.
        """
        # If the current node has no children, it's a leaf node.
        if not self.children:
            return [self]

        # Otherwise, collect leaf nodes from all children.
        leaves = []
        for child in self.children:
            leaves.extend(child.get_leaf_nodes())
        
        return leaves

    def __str__(self, level=0):
        ret = "  " * level + str(self.topic) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    

'''
# Example Usage
root = TopicTree("Science")

# Expand the tree for 3 levels with each node having 2 children
root.expand_recursively_helper(3, 3)
root.save_to_file("tree.json")

# Print the tree structure
print(root)
'''
'''
loaded_tree = TopicTree.load_from_file("tree.json")

# Print the loaded tree structure
leaves = loaded_tree.get_leaf_nodes()
for i in leaves:
    print(i.topic)
'''
