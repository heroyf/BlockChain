import hashlib
import requests


sha256 = hashlib.sha256()
sha256.update('heroyf1'.encode('utf-8'))
res1 = sha256.hexdigest()

# sha256.update('heroyf2'.encode('utf-8'))
# res2 = sha256.hexdigest()
# print(res1 ,res2)


def proofOfWork():
    data = 'heroyf'
    x = '1'
    sha256.update((data+x).encode('utf-8'))
    while True:
        if str(sha256.hexdigest())[0:1] != "0":
            x = str(int(x) + 1)
        else:
            print(str(sha256.hexdigest()))
            print(x)
            break


proofOfWork()
        