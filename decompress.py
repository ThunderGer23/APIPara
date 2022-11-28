import sys
import os
import zipfile

def main(input,output):
    comm = 'cat '+input+'.* > '+input
    print(comm)
    os.system(comm)
    with zipfile.ZipFile(input,"r") as zip_ref:
        print('Extracting '+input+' into '+output)
        zip_ref.extractall()    
    print(os.system('ls '+output))
    return

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])