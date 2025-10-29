class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст 
        # с учетом переданного смещения shift.
        result = []
        for char in original_text.lower():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                new_index = (index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(char)
        return ''.join(result)
    
    
    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        # Дешифровка - это шифрование с обратным сдвигом
        return self.cipher(cipher_text, -shift)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))