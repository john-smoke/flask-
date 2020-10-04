import binascii
import random
import string
from PIL import Image
import re


def openhex(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    hexcode = binascii.hexlify(content)
    hexcode = hexcode.decode()
    return hexcode

def generate_random():
    return random.choice('abcdef1234567890')

def string_to_list(string):
    lst = []
    lst[:0] = string
    return lst

def list_to_string(lst):
    strng = ''
    for h in lst:
        strng += h
    return strng

def put_back_together(hexcode,name):
    data = hexcode
    data = data.strip()
    data = binascii.a2b_hex(data)
    with open(name+'.gif', 'wb') as image_file:
        image_file.write(data)

def fuckery(hexcode):
    return hexcode.replace(generate_random(),generate_random())


if __name__ == '__main__':
    for s in range(32,100):
        
        hexcode = openhex('image' + str(s) + '.gif')
        #hexcode = string_to_list(hexcode)
            
        x = re.finditer('002c',hexcode)

    
        zerozerotwobstart = random.choice(list(x))
        print(zerozerotwobstart)

        data_start = zerozerotwobstart.start() + 22
        
        
        print(data_start)
        print(type(data_start))

        data_length = hexcode[data_start +2:data_start +4]
        print(data_length)


        print(int(data_length,16))

        hexcode = string_to_list(hexcode)

        hexcode[random.randint(data_start+4,data_start+2*int(data_length,16)+2)] = generate_random()

           
        hexcode = list_to_string(hexcode)
        put_back_together(hexcode,'image' + str(s+1)  )
        print('nice')

        f = Image.open('image' + str(s+1)+ '.gif')
        f.verify()


           
    print('all done')
    
    






