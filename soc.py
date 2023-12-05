import socket
import subprocess, sys
import requests
import uuid
#from api_nuc import msg
##############################################################################################################
#python3 -m venv env
#source env/bin/activate

TCP_IP = sys.argv[1]
TCP_PORT = 55502
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
NUMBER_OF_CONECTIONS = 1
EOL = '\n'

##############################################################################################################
subprocess.run("killall -s 9 python3.11", shell = True, executable="/bin/bash")
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((TCP_IP, TCP_PORT)) 
soc.listen(NUMBER_OF_CONECTIONS)
fdata = '';
conn, rmc_addr = soc.accept()

print ('1 - ENDEREÇO DE CONEXAO:', rmc_addr)

mac_address = uuid.getnode()
mac_address_hex = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])

publicIP = requests.get('http://ipinfo.io/json').json()['ip']

localIP = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

#print ('--- ENDEREÇO DE CONEXAO:'+ str(addr))
go = True
res= '';
while(go):
    data = conn.recv(BUFFER_SIZE)
    if not data:
        print('NO DATA !!!')
        go = False
        break
    string_len = len(data)
    #data = str(bytes.hex(data)) 
    if(len(res) <  1024):    
        #echo 'result';
        res= res + data
    elif(len(res) >= 1024):    
        bytes.hex(res)
        params = {'data': data, 'localip': localIP, 'pubip': publicIP ,'mac':mac_address_hex, 'csfr':str('93174923749') }
        r = requests.post("http://localhost/boe/parser.php", data=params)
        print(r.text)
        go =False;
     

    
  