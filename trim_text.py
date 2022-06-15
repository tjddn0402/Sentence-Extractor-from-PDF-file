import re
import pyperclip

with open('text.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

    text = ""
    for line in lines:
        print(line)
        line = line[:-1]+' '
        text += line
    
print(text)
pyperclip.copy(text)

with open("text.txt",'w',encoding='utf8') as f:
    f.writelines(text)

