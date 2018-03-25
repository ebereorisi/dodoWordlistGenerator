import itertools

print("""               ____   __  ____   __                                                               
              (    \ /  \(    \ /  \                                                              
               ) D ((  O )) D ((  O )                                                             
              (____/ \__/(____/ \__/                                                              
 ____  _  _  ____     __   ____  _  _   __   __ _   ___  ____  ____                               
(_  _)/ )( \(  __)   / _\ (    \/ )( \ / _\ (  ( \ / __)(  __)(    \                              
  )(  ) __ ( ) _)   /    \ ) D (\ \/ //    \/    /( (__  ) _)  ) D (                              
 (__) \_)(_/(____)  \_/\_/(____/ \__/ \_/\_/\_)__) \___)(____)(____/                              
 _  _   __  ____  ____  __    __  ____  ____     ___  ____  __ _  ____  ____   __  ____  __  ____ 
/ )( \ /  \(  _ \(    \(  )  (  )/ ___)(_  _)   / __)(  __)(  ( \(  __)(  _ \ / _\(_  _)/  \(  _ \
\ /\ /(  O ))   / ) D (/ (_/\ )( \___ \  )(    ( (_ \ ) _) /    / ) _)  )   //    \ )( (  O ))   /
(_/\_) \__/(__\_)(____/\____/(__)(____/ (__)    \___/(____)\_)__)(____)(__\_)\_/\_/(__) \__/(__\_)



""")

chars = input("Input characters: ")
min_val = int(input("Input minimum value: "))
max_val = int(input("Input maximum value: "))


saveFile = input(r"Save file(location + filename): ")
f = open(saveFile+".txt", "w")        
for n in range(min_val, max_val+1):
    for xx in itertools.product(chars, repeat=n):
        yy = "".join(xx)
        f.write(yy+"\n")
f.close()
