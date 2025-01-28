# import os
# from playsound import playsound
# print("hello world !")
# playsound('C:\\Users\\adity\\Music\\WhatsApp Audio 2024-07-25 at 22.53.51_4ace00c0.mp3')
# print(os.listdir())
n = int(input("enter any no"))
 
if(n%2!=0):
    print("Weird") 
else:
    if(n<=2 and n>=5):
        print("Not Weird")
    elif(n<=6 and n>=20):
        print("Weard")
    elif(n>20):
        print("Not Weird") 