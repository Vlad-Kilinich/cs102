def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    alfbig="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf="abcdefghijklmnopqrstuvwxyz"
    keyword = keyword.upper()
    k=-1
    if len(plaintext) > len(keyword):
        s = len(plaintext)//len(keyword)
        keyword= keyword*(s+1)
    plaintext = list(plaintext)
    for i in plaintext:
        k+=1
        if i in alf:
            n = alf.index(i)
            cheslo = alfbig.find(keyword[k])
            x=n+cheslo
            if x >= len(alf):
                x = x % 26
            ciphertext = ciphertext + alf[x]
        elif i in alfbig:
            n = alfbig.index(i)
            cheslo = alfbig.find(keyword[k])
            x = n+cheslo
            if x >= len(alf):
                x = x % 26
            ciphertext = ciphertext + alfbig[x]
        else:
            ciphertext = ciphertext + i
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alfbig="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf=   "abcdefghijklmnopqrstuvwxyz"
    keyword = keyword.upper()
    k=-1
    if len(ciphertext) > len(keyword):
        s = len(ciphertext)//len(keyword)
        keyword= keyword*(s+1)
    ciphertext= list(ciphertext)
    for i in ciphertext:
        k+=1
        if i in alf:
            n = alf.index(i)
            cheslo = alfbig.find(keyword[k])
            x=n-cheslo
            if x < 0:
                x = x + 26
            plaintext = plaintext + alf[x]
        elif i in alfbig:
            n = alfbig.index(i)
            cheslo = alfbig.find(keyword[k])
            x = n-cheslo
            if x < 0:
                x = x + 26
            plaintext = plaintext + alfbig[x]
        else:
            plaintext = plaintext + i
    return plaintext
