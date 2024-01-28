from alright import WhatsApp
import time

def read_file_lines(path: str):
    texts = []
    with open(path,'r') as file:
        for line in file.readlines():
            texts.append(line)
        file.close()
    return texts;

def read_file(path: str):
    text = ''
    with open(path,'r') as file:
        text = file.read()
    return text;

#Leyendo archivos:
message = read_file('msg.txt')
numbers = read_file_lines('numbers.txt')

#Procede a abrir Whatsapp
messenger = WhatsApp();

for number in numbers:
    messenger.find_user(number)
    messenger.send_message(message)
    time.sleep(2)
