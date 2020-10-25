import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alfbig="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf="abcdefghijklmnopqrstuvwxyz"
    plaintext = list(plaintext)
    for i in plaintext:
        if i in alf:
            n = alf.index(i)
            x = n + shift
            if x > len(alf):
                x = x % 26
            ciphertext = ciphertext + alf[x]
        elif i in alfbig:
            n = alfbig.index(i)
            x = n + shift
            if x > len(alfbig):
                x = x % 26
            ciphertext = ciphertext + alfbig[x]
        else:
            ciphertext = ciphertext + i
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """ 
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alfbig="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf="abcdefghijklmnopqrstuvwxyz"
    ciphertext = list(ciphertext)
    for i in ciphertext:
        if i in alf:
            n = alf.index(i)
            x = n - shift
            if x < 0:
                x = x + 26
            plaintext = plaintext - alf[x]
        elif i in alfbig:
            n = alfbig.index(i)
            x = n - shift
            if x < 0:
                x = x + 26
            plaintext = plaintext - alfbig[x]
        else:
            plaintext = plaintext - i
    return plaintext 
