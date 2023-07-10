"""
	Authors: Ananya, Nadir, Kuldeep, Hemant, Vasu, Yash
	Group: [INSERT NAME HERE]
	Details: Workflow for device's workflow.
"""
import sys, hashlib, binascii
from Crypto.Cipher import AES

class Pineapple:
	input_string = ""
	Morse_Dict = {}
	
	def __init__(self):
		self.input_string = ""
		self.Morse_Dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '+':'.-.-.'}
	
	def banner(self):
		print("")
	
	def check_chars(self):
		"""
			Checks if valid ascii is given in Plain Text.
		"""
		for x in self.input_string:
			if not (x.encode('ascii').isalpha() or (ord(x) >= 46 and ord(x) <= 54) or (ord(x) == 32)):
				return False
		return True
		
	def pad_key(self, key, size=16):
		"""
			Pad the key according to the size mentioned, default is 16.
		"""
		return 	key.encode() + b'\x00'*(size-len(key.encode()))
		
	def enc_AES(self, key):
		"""
			Encrypt the string in AES Output Feedback Mode, uses IV as null bytes, will edit out later. Output in hex.
		"""
		key = self.pad_key(key, 16)
		cipher = AES.new(key, AES.MODE_OFB, iv=b'\x00'*16)
		cipher_string = cipher.encrypt(self.input_string.encode())
		self.input_string = binascii.hexlify(cipher_string)
	
	def dec_AES(self, key):
		"""
			Decrypt the hex string in AES Output Feedback mode. decodes to utf-8 encoding.
		"""
		key = self.pad_key(key, 16)
		cipher = AES.new(key, AES.MODE_OFB, iv=b'\x00'*16)
		cipher_string = cipher.decrypt(binascii.unhexlify(self.input_string))
		self.input_string = cipher_string.decode('utf-8')
			
	def sha_3(self):
		"""
			calculates SHA3 and appends to the string.
		"""
		hasher = hashlib.sha3_224()
		hasher.update(self.input_string.encode())
		hashed_string = hasher.hexdigest()
		self.input_string = self.input_string + "*" + str(hashed_string)
	
	def morse_encode(self):
		"""
			Encode a given hex pattern to morse.
		"""
		encoded_message=""
		for i in str(self.input_string.decode()):
			if i != " ":
				encoded_message += self.Morse_Dict[i.upper()]+" "
			else:
				encoded_message += " "
		self.input_string = encoded_message
	
	def Encryption(self):
		"""
			separate function to understand the workflow easily.
		"""
		self.input_string = input("Plaintext: ")
		if not self.check_chars():
			print("Invalid Characters Detected.\n Stick only to Alpha Numeric codes.")
			return False
		self.sha_3()
		key = input("KEY: ")
		if len(key.encode()) > 16:
			print("only 16 bytes Key size is supported.")
			return False
		self.enc_AES(key)
		self.morse_encode()
		print("Encrypted Text: ", end='')
		print(self.input_string)
	
	def check_morse(self):
		"""
			checks if valid morse in entered while decryption, only dots dashes and spaces allowed.
		"""
		for i in self.input_string:
			if not (i == '.' or i == '-' or i == ' '):
				print("Invalid Morse Data")
				return False
		return True
	
	def morse_decode(self):
		"""
			Decode dots and dashes to hex string.
		"""
		decipher = ""
		citext = ""
		self.input_string += " "
		for i in self.input_string:
			if i != " ":
				c = 0
				citext += i
			else:
				c += 1
				if c == 2:
					decipher += " "
				else:
					decipher += list(self.Morse_Dict.keys())[list(self.Morse_Dict.values()).index(citext)]
					citext = ""
		self.input_string = decipher

	def check_hash(self):
		"""
			Checks the sha3 hash of the recovered plaintext and the appended plaintext.
		"""
		hash_value = self.input_string[self.input_string.find('*')+1:]
		recovered = self.input_string[:self.input_string.find('*')]
		self.input_string = recovered

		self.sha_3()
		self.input_string = self.input_string[len(recovered)+1:]
		if str(self.input_string) == hash_value:				
			self.input_string = recovered
			return True
		return False
	
	def Decryption(self):
		"""
			separate function to understand the workflow easily.
		"""
		self.input_string = input("Morse: ")
		self.check_morse()
		self.morse_decode()
		key = input("KEY: ")
		if len(key.encode()) > 16:
			print("only 16 bytes Key size is supported.")
			return False
		self.dec_AES(key)
		if self.check_hash():
			print("DECRYPTED TEXT: ", end='')
			print(self.input_string)
		else:
			print("Hash Check Failed.")
	
	def start(self):
		"""
			Program Starts interaction here.
		"""
		while True:
			self.banner()
			choice = int(input("1. Encryption\n2. Decryption\n3. Exit\n >> "))
			if choice <= 0 or choice > 3:
				print("This does not make sense.")
				continue
			if choice == 1:
				self.Encryption()
				continue
			elif choice == 2:
				self.Decryption()
			else:
				sys.exit(0)

if __name__ == '__main__':
	"""
	Encryption process:

	
	INPUT ------> H[P.T.]   ----------->   AES[MODE OFB, IV=NULL, KEY=16BYTES] ---------> Ciphertext -------> hexdigest  -------> Morse OUTPUT
	[P.T.]        SHA3 hash of
	              plaintext.
	
	Decryption Process:


	Morse Output =====> HEXDIGEST =====> AES[MODE OFB, IV=NULL, KEY=16BYTES] =====> TEMP_STRING[P.T. + HASH[P.T.]] ====> Extract and compare hash ====> PLAINTEXT

	"""
	banana = Pineapple()
	banana.start()
