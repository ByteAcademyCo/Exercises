def create(file_name):
    open(f'{file_name}.txt', 'w')

def write(file,content):
    with open(f'{file}.txt', 'w') as file_writer:
        file_writer.write(content)

def read(file):
    with open(f'{file}.txt', 'r') as file_reader:
        x = file_reader.read()
    return x