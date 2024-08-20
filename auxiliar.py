fat_ascii = {'0':'0',
         '1':'1',
         '2':'2',
         '3':'3',
         '4':'4',
         '5':'5',
         '6':'6',
         '7':'7',
         '8':'8',
         '9':'9',
         '10':'a',
         '11':'b',
         '12':'c',
         '13':'d',
         '14':'e',
         '15':'f',
         '16':'g',
         '17':'h',
         '18':'i',
         '19':'j',
         '20':'k',
         '21':'l',
         '22':'m',
         '23':'n',
         '24':'o',
         '25':'p',
         '26':'q',
         '27':'r',
         '28':'s',
         '29':'t',
         '30':'u',
         '31':'v',
         '32':'w',
         '33':'x',
         '34':'y',
         '35':'z',
         '36':'?',
         '37':'Z',
         '38':' ',
         '39':'A',
         '40':'B',
         '41':'C',
         '42':'D',
         '43':'E',
         '44':'F',
         '45':'G',
         '46':'H',
         '47':'I',
         '48':'J',
         '49':'K',
         '50':'L',
         '51':'M',
         '52':'N',
         '53':'O',
         '54':'P',
         '55':'Q',
         '56':'R',
         '57':'S',
         '58':'T',
         '59':'U',
         '60':'V',
         '61':'W',
         '62':'X',
         '63':'Y',
}

fat_ascii_inverse= {v:k for k,v in fat_ascii.items()}

def int_to_char(number):
    return fat_ascii[number]
    

def char_to_int(character):
    return fat_ascii_inverse[character]
    

def text_to_bits(text):
    return ''.join([bin(int(char_to_int(c))).replace('0b','').zfill(6) for c in text])
    

def bits_to_text(binary):
    return ''.join([int_to_char(str(int(binary[6*i:6*(i+1)],2))) for i in range(int(len(binary)/6))])


def cipher(message,key):
    ciph = ''
    message = text_to_bits(message)
    key = text_to_bits(key)
    for i in range(len(message)):
        ciph += str((int(message[i]) + int(key[i]))%2)
    return bits_to_text(ciph)
    
