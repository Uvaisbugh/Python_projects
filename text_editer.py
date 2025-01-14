import os 

def read_file(filename):
    with open (filename, 'r') as f:
        return f.read()
    
def write_file(filename, text):
    with open (filename, 'w') as f:
        f.write(text)
        
def get_user_input(prompt):
    print('\nEnter your text (type SAVE on a new line to save and exist):')
  
    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)  
  
    return '\n'.join(lines)

def main():
    filename = input('Enter the filename: ')