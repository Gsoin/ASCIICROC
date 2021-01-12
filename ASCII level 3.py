#LEVEL 3 ACCESS
def level_3_decrypt(encrypted_passphrase):
    # Replacing '_' by spaces in the encrypted message
    message = encrypted_passphrase.replace('_', ' ')
    decodedMessage = " "
    for item in message.split():
        # Convert to int then decrypt it with chr() and adding it to decodedMessage
        decodedMessage += chr(int(item))
    return decodedMessage  # Return decodedMessage


encrypted_passphrase = "110_97_116_105_111_110_97_108_ 97_115_115_111_99_105_97_116_105_111_110_111_102_ 115_101_99_117_114_105_116_105_101_115_100_101_97_108_101_114_115_ 97_117_116_111_109_97_116_101_100_113_117_111_116_97_116_105_111_110_115_115_101_99_117_114_105_116_105_101_115_ 97_110_100_101_120_99_104_97_110_103_101_ 99_111_109_109_105_115_115_105_111_110_116_105_109_101_ 118_97_108_117_101_ 111_102_ 109_111_110_101_121_"
decodedMessage = level_3_decrypt(encrypted_passphrase)
print("Decoded message:", decodedMessage)
