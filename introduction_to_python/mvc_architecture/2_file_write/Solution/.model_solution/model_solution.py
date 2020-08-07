def create(file_name):
    open(f'{file_name}.txt','w')
    return 

def write(file,content):
    with open(f'{file}.txt','a') as file_writer:
        file_writer.write(content)
    return 

def read(file):
    with open(f'{file}.txt','r') as file_reader:
        data=file_reader.read()
    return data 