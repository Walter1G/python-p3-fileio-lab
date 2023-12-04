def write_file(file_name, file_content):
    with open(f'{file_name}.txt', encoding='utf-8', mode='w') as text_file:
        text_file.write(file_content)
    
    
def append_file(file_name, append_content):
    with open(f'{file_name}.txt', encoding='utf-8', mode='a') as text_file:
        text_file.write(append_content)
    pass

def read_file(file_name):
    with open(file_name, encoding='utf-8') as text_file:
        text_file.read()
        
    
