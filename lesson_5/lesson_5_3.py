# Завдання 3*

# Зашифрувати текст, введений користувачем, за допомогою шифру Цезаря. Знаки пунктуації та регістр букв не змінюються.
# Ключ для шифрування також вводиться користувачем.


# encrypts "a" as "b" using 1 as key
# encrypts "barfoo" as "yxocll" using 23 as key
# encrypts "BARFOO" as "EDUIRR" using 3 as key
# encrypts "BaRFoo" as "FeVJss" using 4 as key
# encrypts "barfoo" as "onesbb" using 65 as key
# encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key


#############

def crypt_text (text, key):
    crypt_text = ''

    while key > 26 :    
        key -= 26   
    
    for letter in text:    
        char = ord(letter)
        slide = char + key
        if ((char > 64 and char < 91) or (char > 96 and char < 123)):
            if letter.isupper():            
                if slide > 90:                
                    slide -= 26                
            
            if letter.islower():            
                if slide > 122:                
                    slide -= 26   

            crypt_text += chr(slide)
        else:
            crypt_text += chr(char)            

    return crypt_text


print("Привіт! Це простий шифрувальник методом Цезаря.")

key = int(input("Введіть ключ шифрування (ціле число): "))

plaintext = input("Введіть текст для шифрування (латиниця): ")

ciphertext = crypt_text(plaintext, key)

print(f"Зашифрований текст: {ciphertext}\n")