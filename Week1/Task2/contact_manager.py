import os
from pathlib import Path

# Change to the script's directory
os.chdir(Path(__file__).parent)

# Read a Whole File
with open('data.txt','r') as file:
    content=file.read()
    print(content)



## Read a file line by line
with open('data.txt','r') as file:
    for line in file:
        print(line.strip()) ## sstrip() removes the newline character




## Writing a file(Overwriting)
''' with open('data.txt','w') as file:
     file.write('This is a new contact\n')
     file.write('03015978164') '''



## Write a file(without Overwriting)
with open('data.txt','a') as file:
    file.write("Append operation taking place!\n")


### Writing a list of lines to a file
lines=['03219416461 \n','03219416461 \n','03219416461\n']
with open('data.txt','a') as file:
    file.writelines(lines)


### Read the content from a text from data fiile and write to a data1 file
# Copying a text file
with open('data.txt', 'r') as source_file:
    content = source_file.read()

with open('data2.txt', 'w') as destination_file:
    destination_file.write(content)


### Writing and then reading a file

with open('example.txt','w+') as file:
    file.write("Hello world\n")
    file.write("This is a new line \n")

    ## Move the file cursor to the beginning
    file.seek(0)

    ## Read the content of the file
    content=file.read()
    print(content)