import json
import os


class FileHandler:

    def __init__(self, file_path="students.json"):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []