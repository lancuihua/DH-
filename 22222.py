import tkinter as tk
from tkinter import simpledialog, messagebox
from sympy import primerange, is_primitive_root
from random import randint

# Function to find a primitive root modulo a prime number
def find_primitive_root(prime):
    for i in range(2, prime):
        if is_primitive_root(i, prime):
            return i
    return None

# Generate a list of primes from 100 to 255
primes = list(primerange(100, 256))

# Choose a prime from the list and find a primitive root for it
p = primes[randint(0, len(primes) - 1)]
g = find_primitive_root(p)

# If no primitive root is found, we'll pick another prime
while g is None:
    p = primes[randint(0, len(primes) - 1)]
    g = find_primitive_root(p)

# Function to get private key from user and calculate public key
def calculate_keys():
    try:
        # Get private key from user
        private_key = simpledialog.askinteger("Input", "Enter your private key (integer):",
                                              parent=root, minvalue=2, maxvalue=p-2)
        if private_key is not None:
            # Calculate public key
            public_key = pow(g, private_key, p)
            # Show the calculation in the console
            print(f"Chosen prime (p): {p}")
            print(f"Primitive root (g): {g}")
            print(f"Your private key: {private_key}")
            print(f"Your public key (g^private_key mod p): {public_key}")
            
            # Display the public key to the user
            messagebox.showinfo("Public Key", f"Your public key is: {public_key}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the main application window
root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")

# Button to trigger the calculation
calculate_button = tk.Button(root, text="Select Private Key", command=calculate_keys)
calculate_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
