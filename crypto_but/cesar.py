###########################################################
####       Programmation du chiffrement de césar       ####
###########################################################

def chiffrement_cesar(message, k):
    longeur_msg = len(message)
    message_crypte = ""

    for i in range(longeur_msg):
        if message[i] == " ":
            message_crypte += chr(255)
            continue

        ascii = ord(message[i]) + k
        message_crypte += chr(ascii)
    return message_crypte


def dechiffrement_cesar(message_chr, k):
    longeur_chr = len(message_chr)
    message = ""

    for i in range(longeur_chr):
        if message_chr[i] == chr(255):
            message += " "
            continue

        ascii = ord(message_chr[i]) - k
        message += chr(ascii)
    return message

