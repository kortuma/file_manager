# File Manager Module

A Python module providing basic file management operations.

## Features

- Read the content of a file
- Write content to a file
- Copy a file from one location to another
- List files in a directory

## Usage

1. Import the `FileManager` class from the module:

    ```python
    from file_manager import FileManager
    ```

2. Use the methods as needed:

    ```python
    # Example usage
    FileManager.read_file('example.txt')
    FileManager.write_to_file('example.txt', 'Hello, World!')
    FileManager.copy_file('source.txt', 'destination.txt')
    FileManager.list_files('/path/to/directory')
    ```

3. Replace file paths and directory paths with your actual file and directory locations.

## Notes

- Ensure that you have the necessary permissions to read, write, and copy files.
- Make sure that the specified files and directories exist before using the methods.
