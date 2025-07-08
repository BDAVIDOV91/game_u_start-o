# save_manager.py

import json

class SaveManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_game(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def load_game(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
