# file_manager.py

import os
import shutil

class FileManager:
    @staticmethod
    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Content of {file_path}:\n{content}")
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    @staticmethod
    def write_to_file(file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
                print(f"Content written to {file_path}")
        except Exception as e:
            print(f"Error writing to file: {e}")

    @staticmethod
    def copy_file(source_path, destination_path):
        try:
            shutil.copy(source_path, destination_path)
            print(f"File copied from {source_path} to {destination_path}")
        except FileNotFoundError:
            print(f"File not found: {source_path}")
        except Exception as e:
            print(f"Error copying file: {e}")

    @staticmethod
    def list_files(directory_path):
        try:
            files = os.listdir(directory_path)
            print(f"Files in {directory_path}:\n{files}")
        except FileNotFoundError:
            print(f"Directory not found: {directory_path}")
        except Exception as e:
            print(f"Error listing files: {e}")
