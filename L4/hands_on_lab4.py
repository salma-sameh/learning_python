class FileManager:
    
    def read_file(self, filename):
        """Read and return file content."""
        try:
            with open(filename, 'r') as file:
                content = file.read()
            return content
        
        except FileNotFoundError:
            return f"Error: '{filename}' not found."
        
        except PermissionError:
            return f"Error: Permission denied for '{filename}'."
        
        except Exception as e:
            return f"Unexpected error: {e}"


    def write_file(self, filename, content):
        """Write content to file (overwrite if exists)."""
        try:
            with open(filename, 'w') as file:
                file.write(content)
            return f"File '{filename}' written successfully."
        
        except PermissionError:
            return f"Error: Permission denied for '{filename}'."
        
        except Exception as e:
            return f"Unexpected error: {e}"


    def append_file(self, filename, content):
        """Append content to file."""
        try:
            with open(filename, 'a') as file:
                file.write(content)
            return f"Content appended to '{filename}' successfully."
        
        except PermissionError:
            return f"Error: Permission denied for '{filename}'."
        
        except Exception as e:
            return f"Unexpected error: {e}"
        
# Example usage
fm = FileManager()

# Write
print(fm.write_file("test.txt", "Hello World\n"))

# Append
print(fm.append_file("test.txt", "This is appended text.\n"))

# Read
print(fm.read_file("test.txt"))