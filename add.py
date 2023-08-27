import json
import os

file_path = os.path.join(os.getcwd(), 'knowledge_base.json')
# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str):

    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

knowledge_base: dict = load_knowledge_base(file_path)

def add():
    print('what do you want to add')
    user_input: str = input("question: ")
    answer: str = input("answer: ")
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    knowledge_base["questions"].append({"question": user_input, "answer": answer})
    save_knowledge_base('knowledge_base.json', knowledge_base)
    add()

add()