#ex1
#?????

#ex2
print("_________________________________________________________")
import os
print('Exist:', os.access('c:\\Users\\Public\\C programming library.docx', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C programming library.docx', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C programming library.docx', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C programming library.docx', os.X_OK))
print("successfully")
#ex3
print("_________________________________________________________")
import os
print("Test a path exists or not:")
path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))
path = r'g:\\testpath\\p.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
print("successfully")
#ex4
print("_________________________________________________________")
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)
print("successfully")

#ex5
print("_________________________________________________________")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())
print("successfully")
#ex6
print("_________________________________________________________")
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
print("successfully")
#ex7
print("_________________________________________________________")
with open('first.txt', 'w') as first_file:
    first_file.write("Привет, это содержимое первого файла.")

with open('first.txt', 'r') as first_file, open('second.txt', 'a') as second_file: 
    data = first_file.read()
    second_file.write(data)

print("successfully")

#ex8
print("_________________________________________________________")
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")

file_to_delete = "file_to_delete.txt"
delete_file(file_to_delete)
print("successfully")