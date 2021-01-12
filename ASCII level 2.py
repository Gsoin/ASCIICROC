#LEVEL 2 ACCESS
def level_2_decrypt(encrypted_passphrase):
    """Decrypt the string and return the plaintext"""
    result = ''
    for encrypted in encrypted_passphrase:
        try:
            # shift of 11
            decrypting = (key.index(encrypted) - -11) % 26
            result += key[decrypting]
        except ValueError:
            result += encrypted
    return result


key = 'abcdefghijklmnopqrstuvwxyz'
text = " phhti gt paadrpixdc psyjhipqat gpit bdgivpvth deedgijcxin rdhi hwdgi htaaxcv vdktgcbtci qdcsh vtgbpc wnetg xcuapixdc utstgpa gthtgkt qpczh ugdci tcs utth uxmts gpit bdgivpvt ipm adhh hpat igjhi ujcs"
decrypted = level_2_decrypt(text)
print('Decrypted:', decrypted)