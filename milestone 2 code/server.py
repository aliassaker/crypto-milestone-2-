import socket
from des import des_ecb_decrypt

STATIC_KEY = b"8bytekey"  # shared 64-bit key, same as the client
HOST = "127.0.0.1"
PORT = 65432


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[SERVER] Legacy Bank mainframe listening on {HOST}:{PORT}")
        print(f"[SERVER] Static 64-bit key (hex): {STATIC_KEY.hex()}")

        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connection from {addr}")
            ciphertext = conn.recv(4096)
            print(f"[SERVER] Received ciphertext (hex): {ciphertext.hex()}")

            plaintext = des_ecb_decrypt(ciphertext, STATIC_KEY).decode("utf-8")  # DES-ECB decrypt
            print(f"[SERVER] Decrypted transaction    : {plaintext}")

            conn.sendall(b"ACK: transaction received and decrypted")


if __name__ == "__main__":
    main()
