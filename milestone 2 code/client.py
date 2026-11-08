import socket
from des import des_ecb_encrypt

STATIC_KEY = b"8bytekey"  # shared 64-bit key, same as the server
HOST = "127.0.0.1"
PORT = 65432
TRANSACTION = "TXID:0001 FROM:ACC-100 TO:ACC-200 AMT:500.00 EGP"  # test message


def main():
    ciphertext = des_ecb_encrypt(TRANSACTION.encode("utf-8"), STATIC_KEY)  # DES-ECB encrypt

    print(f"[CLIENT] Plaintext transaction : {TRANSACTION}")
    print(f"[CLIENT] Static 64-bit key(hex): {STATIC_KEY.hex()}")
    print(f"[CLIENT] Ciphertext (hex)      : {ciphertext.hex()}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(ciphertext)
        print(f"[CLIENT] Server reply          : {s.recv(1024).decode('utf-8')}")


if __name__ == "__main__":
    main()
