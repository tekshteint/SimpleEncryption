import os
import json
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as tkmb

class scrambler():
    def __init__(self):
        self.encryptHistory=[]
        self.decryptHistory=[]
        self.encrypt=str()
        self.decrypt=str()
        while True:
            option=input("Would you like to (1)encrypt, (2)decrypt, (3)view history,\n(4)save to a text file, or (5)exit?\n")
            if option=="1":
                self.encryption()
            elif option=="2":
                self.decryption()
            elif option=="3":
                self.view()
            elif option=="4":
                self.save()
            elif option=="5":
                print("Goodbye!")
                raise(SystemExit(0))
            else:
                print("Please pick an option from the menu")
        
    def encryption(self):
        myList=[]
        getText=input("Enter text to encrypt\nIf you want to reuse the decrypted text, type 'reuse'\n")
        if getText=="reuse":
            getText=self.decrypt        
        for i in getText:
            for j in i:
                myList.append(chr(ord(j)+1))
        self.encrypt=("".join(myList))
        self.encryptHistory.append(self.encrypt)
        print(self.encrypt)    

    def decryption(self):
        myList=[]
        getText=input("Enter text to decrypt\nIf you want to reuse the decrypted text, type 'reuse'\n")
        if getText=="reuse":
            getText=self.encrypt
        for i in getText:
            for j in i:
                myList.append(chr(ord(j)-1))
        self.decrypt=("".join(myList))
        self.decryptHistory.append(self.decrypt)
        print(self.decrypt)    
        
    def view(self):
        print("Encrypted text:",self.encryptHistory,"\nDecrypted text:",self.decryptHistory)
        
    def save(self):
        root=tk.Tk()
        root.withdraw()
        CWD=tk.filedialog.askdirectory(initialdir='.')
        with open("PreviousEncryptions.txt","w") as file:
            for i in self.encryptHistory:
                file.write(i+"\n")
        tkmb.showinfo("File Saved",f"File PreviousEctryptions.txt has been saved to {CWD}",parent=root)
        
run=scrambler()