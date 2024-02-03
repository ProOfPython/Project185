import tkinter as tk
import hashlib as hash

root = tk.Tk()
root.title('Showcase Of Encryption 2')
root.geometry('300x300')
root.config(bg = 'mistyrose1')

fileEntry = open('Project185+/entry.txt', 'r')

def writeMd5():
    global fileEntry
    fileEntry.seek(0)
    text = fileEntry.read()
    
    encoded = hash.md5(text.encode())
    encodedStr = str(encoded.hexdigest())
    print('MD5 Data:\n' + encodedStr)

    fileMd5 = open('Project185+/md5.txt', 'w')
    fileMd5.write(encodedStr)
    fileMd5.close()


def writeSha256():
    global fileEntry
    fileEntry.seek(0)
    text = fileEntry.read()
    
    encoded = hash.sha256(text.encode())
    encodedStr = str(encoded.hexdigest())
    print('SHA256 Data:\n' + encodedStr)

    fileSha256 = open('Project185+/sha256.txt', 'w')
    fileSha256.write(encodedStr)
    fileSha256.close()

btnApplyMd5 = tk.Button(root, bg = 'salmon', text = 'Apply MD5', command = lambda: writeMd5())
btnApplyMd5.place(relx = 0.3, rely = 0.4, anchor = tk.CENTER)

btnApplySha256 = tk.Button(root, bg = 'salmon4', fg = 'white', text = 'Apply SHA256', command = lambda: writeSha256())
btnApplySha256.place(relx = 0.7, rely = 0.4, anchor = tk.CENTER)

root.mainloop()