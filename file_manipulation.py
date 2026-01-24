import os

# Create a new file and write some text into it
#
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
    file.write('\nThis is a sample file for file manipulation.')

# Remvoe the file
os.remove('example.txt')
