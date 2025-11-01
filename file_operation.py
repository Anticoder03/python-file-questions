# 1) Write a Python program to create a text file and write user input into it.
file_name  = input("Enter the file name to create: ")
content = input("Enter the content to write into the file: ")
with open(file_name, 'w') as file:
    file.write(content)
    print(f"Content written to {file_name} successfully.")
    
# 2) Write a program to read a text file and display its content.
with open('test.txt', 'r') as file:
    data = file.read()
    print("Content of the file:")
    print(data)

# 3) Write a Python program to append data to an existing file.
with open('test.txt', 'a') as file:
    additional_content = "\nAppended line."
    file.write(additional_content)
    print("Content appended successfully.")

# 4) Write a program to count lines, words, and characters in a file.
with open('test.txt', 'r') as file:
    content_list = file.readlines()
    line_count = len(content_list)
    word_count = sum(len(line.split()) for line in content_list)
    char_count = sum(len(line) for line in content_list)
    print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")

# 5) Write a program to read a file line by line.
with open('test.txt', 'r') as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())

# 6) Write a program to copy content of one file into another.
with open('test.txt', 'r') as source_file:
    content = source_file.read()
with open('copy_of_test.txt', 'w') as dest_file:
    dest_file.write(content)
    print("Content copied to copy_of_test.txt successfully.")

# 7) Write a program to check if a file exists or not.
import os
file_path = 'test.txt'
if os.path.isfile(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")


# 8) Write a program to handle FileNotFoundError exception.
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file was not found. Please check the file name and try again.")
    

# 9) Write a program to write a list of names into a file.
names = ["Alice", "Bob", "Charlie", "David"]
with open('names.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')
    print("Names written to names.txt successfully.")


# 10) Write a program to read only the first 10 characters from a file.
with open('test.txt', 'r') as file:
    first_10_chars = file.read(10)
    print("First 10 characters of the file:")
    print(first_10_chars)
