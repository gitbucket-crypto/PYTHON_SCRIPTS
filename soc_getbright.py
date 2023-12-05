import socket
import subprocess, sys
##############################################################################################################

TCP_IP = sys.argv[1]
TCP_PORT = 55502
BUFFER_SIZE = 1146  # Normally 1024, but we want fast response
NUMBER_OF_CONECTIONS = 2
EOL = '\n'

##############################################################################################################

#print(" -------------------------------------------- "+EOL)
#print("  Iniciando em "+str(TCP_IP)+" porta "+str(TCP_PORT)+"  "+EOL)
#print(" -------------------------------------------- "+EOL)

##############################################################################################################
try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.bind((TCP_IP, TCP_PORT))
    #soc.bind((socket.gethostname(), TCP_PORT))
    soc.listen(NUMBER_OF_CONECTIONS)
    conn, addr = soc.accept()  
    data = bytes.fromhex('FF 55 04 40 01 01 00 9a')   
    ret = conn.send(data)
    print(ret)
    print(EOL)
    resp =  conn.recv(BUFFER_SIZE)
    print(str(bytes.hex(resp)))
    soc.close()

except:
    print("Socket bloqueado, matando codigo")
    subprocess.run("killall -s 9 python3.11", shell = True, executable="/bin/bash")



