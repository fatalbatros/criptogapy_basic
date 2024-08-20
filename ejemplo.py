from auxiliar import char_to_int, int_to_char, text_to_bits, cipher, bits_to_text

texto = "mensaje privado"
llave = "llave muy segura"

print('Dado un mensaje m primero se pasa cada caracter a un numero segun la tabla fat_ascii')
print('Despues ese numero se pasa a un binario de bits (la tabla fat_ascii tiene 2**6 entradas)')
print(f'Como ejemplo tomemos m = "{texto}" \n')

for c in texto:
    i = int(char_to_int(c))
    j = bin(i).replace('0b','').zfill(6)
    print(f'{c} -> {i} -> {j}')

print('')
print('El mensaje en binario es entonces:')
print((texto_bits := text_to_bits(texto)) + '\n')

print('El cifrado consiste en tener una key k de al menos la misma longitud que le mensaje')
print(f'por ejemplo: k = "{llave}" que se escribe como' + '\n')
print((llave_bits := text_to_bits(llave)) + '\n')

print('El cifrado consiste en sumar bit a bit el texto y la llave, para cada bit del texto \n')

cifrado_bits = ''
for i in range(len(texto_bits)):
    cifrado_bits += str((int(texto_bits[i]) + int(llave_bits[i]))%2)

print(cifrado_bits + '\n')

print('Eso pasado a texto es:')
print(bits_to_text(cifrado_bits) +'\n')

print('Para decifrar se usa el mismo metodo sobre el texto cifrado con la misma llave')






