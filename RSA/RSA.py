import random
import math

def main():
    while True:
        menu_principal()
        op = input('Select one choice(1/2): ')
        print()
        if op == '1':
            print("-----------------------------KEY GENERATE-----------------------------")
            p = int(input("Enter a prime number: "))
            q = int(input("Enter another prime number (Not one you entered above): "))
            print()
            print("Generating your public/private now . . . /")
            public, private = generate_keypair(p, q)
            print("Your public key is ", public, " and your private key is ", private)
            print()
            print("-----------------------------MESSAGE TO ENCRYPT-----------------------------")
            message = input("Enter a message to encrypt: ")
            print()
            encrypted_msg = encrypt(private, message)
            print("-----------------------------ENCRYPTED MESSAGE-----------------------------")
            print("Your encrypted message is: ")
            print(''.join(map(lambda x: str(x), encrypted_msg)))
            print("-----------------------------DECRYPTED MESSAGE-----------------------------")
            print("Decrypting message with public key ", public, " . . .")
            print("Your message is: ")
            print(decrypt(public, encrypted_msg))

        if op == '2':
            print('Bye !')
            return

def menu_principal():
    print(''' 
  ___  ___   _     ___                       _               __  ___                       _           
 | _ \/ __| /_\   | __|_ _  __ _ _ _  _ _ __| |_ ___ _ _    / / |   \ ___ __ _ _ _  _ _ __| |_ ___ _ _ 
 |   /\__ \/ _ \  | _|| ' \/ _| '_| || | '_ \  _/ -_) '_|  / /  | |) / -_) _| '_| || | '_ \  _/ -_) '_|
 |_|_\|___/_/ \_\ |___|_||_\__|_|  \_, | .__/\__\___|_|   /_/   |___/\___\__|_|  \_, | .__/\__\___|_|  
                                   |__/|_|                                       |__/|_|                                  

    by: Rafael Moreno
        Karla López 
        Eric Bautista
        
                            MENU
    ------------------------------------------------------
    (1) Encrypt
    (2) Exit
    ------------------------------------------------------
        ''')

#ALgorithm to find the multiplicative inverse of two numbers
def multiplicative_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

        # Make x positive
    if (x < 0):
        x = x + m0

    return x

#Determine whether a number is prime or not
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('NOTE: Both numbers must be prime.')
    elif p == q:
        raise ValueError('NOTE: p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

main()