import socket as s
host="127.0.0.1"
port=64623
with s.socket(s.AF_INET,s.SOCK_STREAM) as ss:
    ss.bind((host,port))
    ss.listen()
    conn,addr=ss.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


