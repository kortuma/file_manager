# main.py

from file_manager import FileManager

# Пример использования
FileManager.read_file('example.txt')
FileManager.write_to_file('example.txt', 'Hello, World!')
FileManager.copy_file('source.txt', 'destination.txt')

FileManager.list_files('/path/to/directory')
# Don't forget to replace /path/to/directory with the actual path to your directory.
