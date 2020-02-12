from sys import argv

script, file_name = argv

def print_all(f):
    print(f.read())
    
def print_begin(f):
    f.seek(0)
    
def print_a_line(lc, f):
    print (lc, f.readline())
    
current_file = open(file_name)

print_all(current_file);
print("+++")
print_begin(current_file);
print("+++")
line = 1
print_a_line(line,current_file);
print("+++")
line = 1+1
print_a_line(line,current_file);