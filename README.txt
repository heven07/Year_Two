Encryption process:

INPUT[P.T.] ------> H[P.T.]   ----------->   AES[MODE OFB, IV=NULL, KEY=16BYTES] ---------> Ciphertext -------> hexdigest  -------> Morse OUTPUT

Decryption Process:

Morse Output =====> HEXDIGEST =====> AES[MODE OFB, IV=NULL, KEY=16BYTES] =====> TEMP_STRING[P.T. + HASH[P.T.]] ====> Extract and compare hash ====> PLAINTEXT

Observations:
1. All functions are implemented as modules, combinations of these can be used according to the need to encrypt/decrypt data.
2. AES 128bit is used for encryption/decryption.[working on results to check which function is best for implementation/realtime usage]
3. Morse and hex encodes the data, workflow can be modified easily to add or remove parts from the workflow.

Limitations:
1. AES in OFB mode requires an IV to work, that has to be stored or some other mode has to be used.
2. Addition of SHA increases the size of the HEX OUTPUT, thereby increasing the size of the morse code.
3. A few global constants like Morse lookup table and the IV(as discussed above), need to be hardcoded, which might be harder to implement in hardware mode.
4. Protecting the code from side channel attacks and timing attacks will require decent time to properly implement.
5. Current key size limit is 16 bytes, which has to be changed to deal with bigger keys.


