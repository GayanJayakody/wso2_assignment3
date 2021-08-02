import hashlib
leak = "3c2223212b6dde34bcf86b580bdb71d4"
with open('phpbb.txt','r') as file:
   
    # reading each line    
    for line in file:
        hashval = hashlib.md5(line.strip().encode()).hexdigest()
        #print(hashval) 
        if( hashval == leak):
            print(line)