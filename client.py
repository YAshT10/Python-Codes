import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
       m =input("Enter data to send server: ")
       res = s.sendto(m.encode(),("192.168.56.1",2222)) 
       if res:
          print("\nSuccessfully send")
