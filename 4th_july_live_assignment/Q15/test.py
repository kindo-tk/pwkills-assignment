import file_operations

# Write to a file
file_operations.write_to_file("example.txt", "Hello, World!")

# Read from a file
content = file_operations.read_from_file("example.txt")
print(content)

# Append to a file
file_operations.append_to_file("example.txt", "Appending some more text.")
