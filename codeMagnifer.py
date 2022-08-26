from ast import main
from dataclasses import dataclass
import os
def main():
    f=open("PasteHere.txt",'r')
    data=f.readlines()
    print(data)
    updatedData=""
    for line in data:
        line=line.replace('\n','')
        updatedData+=line.replace(' ','')
    w=open("PasteHere.txt",'w')
    w.write(updatedData)
main()