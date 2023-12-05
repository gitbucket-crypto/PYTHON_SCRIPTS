import socket
import subprocess, sys
import time
##############################################################################################################

TCP_IP = sys.argv[1]
TCP_PORT = 55502
BUFFER_SIZE = 1146  # Normally 1024, but we want fast response
NUMBER_OF_CONECTIONS = 2
EOL = '\n'

##############################################################################################################

print(" -------------------------------------------- "+EOL)
print("  Iniciando em "+str(TCP_IP)+" porta "+str(TCP_PORT)+"  "+EOL)
print(" -------------------------------------------- "+EOL)

##############################################################################################################
try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.bind((TCP_IP, TCP_PORT))
    #soc.bind((socket.gethostname(), TCP_PORT))
    soc.listen(NUMBER_OF_CONECTIONS)
    conn, addr = soc.accept()  
    #On：FF 55 04 21 01 01 01 7c
    ldfoff= bytes.fromhex('FF 55 04 21 01 02 00 7c')
    ret = conn.send(ldfoff)
    print('red_disable_ldr '+str(ret))
    time.sleep(5)
    data = bytes.fromhex('FF 55 04 00 01 02 56 B1')   
    ret = conn.send(data)
    print(ret)
    print(EOL)
    resp =  conn.recv(BUFFER_SIZE)
    print(str(bytes.hex(resp)))
    soc.close()

except:
    print("Socket bloqueado, matando codigo")
    subprocess.run("killall -s 9 python3.11", shell = True, executable="/bin/bash")



