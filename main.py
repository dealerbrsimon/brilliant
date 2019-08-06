'''
Functions that could be used to familiarize the student with different topics, including encryption, decryption, data visualisation, generating a python Dictionnary and contrast the difficulty between Ceasar and Vigenes while also showing the similarities 
'''

import matplotlib.pyplot as plt
from ex import original_message,crypted_message

def gen_distribution(message) : 
	'''
	This function allows to generate the distribution for each letter. We assume that space between letters is not a crypted letter. I make use of if, elif, else, continue and break in a clear way to allow the student to fully grasp the logic behing every step.
	'''

	letter_distribution = {}

	for letter in message:

		if letter == ' ' :

			continue

		if letter not in letter_distribution:

			letter_distribution[letter] = 1

		elif letter in letter_distribution:

			letter_distribution[letter] += 1	

		else:
			print('Something went wrong ! ')
			break	

	return letter_distribution		


def gen_cypher(shift) :
	'''
	This function allows to generate a chart and the appropriate decypher chart for a given shift. For learning purpose we will only use lower caps letter and a reduced num of chars. The function is not very optimised, the goal is more to display the chart generation process. 
	'''

	x = shift 

	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	
	encrypt = alphabet[x::] + alphabet[:x:]

	cypher_chart = {key: value for (key, value) in zip(alphabet,encrypt)}

	decypher_chart = {value:key for (key, value) in zip(alphabet,encrypt)}



	return cypher_chart,decypher_chart


def encrypt(message,cypher):
	'''
	This function takes a message a a cypher chart 
	to encrypt the given message 
	'''

	encrypted_message = ''

	for letter in message:

		if letter == ' ' :

			encrypted_message += letter

		else:	
		
			letter = cypher[letter]

			encrypted_message += letter


	return encrypted_message


def decrypt(message,cypher):
	'''
	This function allows to decrypt a given message 
	with the appropriate chart 
	'''

	decrypted_message = ''

	for letter in message :

		if letter == ' ':

			decrypted_message += letter 

		else:

			letter = cypher[letter]

			decrypted_message += letter 

	return decrypted_message			


'''
Vigen's encrypt and decrypt functions. The student could use 
them to crypt and decrypt different messages with different keys and visualize them. For learning purposes we could simplify the Vigenes function to only use lower caps and a more simple alphabet, depending on the student level and the rest of the course content. Since it is more about visualization, I would probably simplify it further if we move forward :) 
'''



'''
First function takes a message to be crypted and 
the key you want to use to do so.
'''


def encryptVigen(message, key):

    key_length = len(key)

    key_as_int = [ord(letter) for letter in key]

    plaintext_int = [ord(letter) for letter in message]

    ciphertext = ''

    for i in range(len(plaintext_int)):

        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26

        ciphertext += chr(value + 65)

    return ciphertext


'''
Second function takes the encrypted message and the key 
to decrypt it 
'''

def decryptVigen(message, key):

    key_length = len(key)

    key_as_int = [ord(letter) for letter in key]

    ciphertext_int = [ord(letter) for letter in message]

    decrypted_message = ''

    for i in range(len(ciphertext_int)):

        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26

        decrypted_message += chr(value + 65)
				
    return decrypted_message


'''
Visualization using Pyplot, first distribution is in red 
Second is in green. I could use another program for more intuitive Visualization, I feel like Pyplot is a good introduction to these tasks due to the big online community and ease of use. Exemple is with Ceasar_cypher.
You can change the variables first_distribution and second_distribution to plot different distributions.

'''

def visualize_distribution(original,crypted):


	first_distribution = gen_distribution(crypted)

	second_distribution = gen_distribution(original)

	plt.bar(first_distribution.keys(), first_distribution.values(), width=0.5, color='r')

	plt.bar(second_distribution(), second_distribution(), width=0.5, color='g')


visualize_distribution(original_message,crypted_message)
