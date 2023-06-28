# 🕵🏼‍ REVERSE SHELL - DEMO - v1.4 🕵🏼‍♂️ 

![Foto](https://www.techslang.com/wp-content/uploads/2021/03/tglo209-reverse-1024x540.png)

<br>
<br>

### 😈 ANTIVIRUS
It has been checking all the Windows that can be run and these are:
<br>
##### ⚜️ WINDOWS 10:

| Windows Defender | Windows 10 |
| --- | --- |
| ✅ | Windows 10 Home |
| ✅ | Windows 10 Pro |
| ✅ | Windows 10 Enterprise |
| ✅ | Windows 10 Enterprise LTSB/LTSC |
| ✅ | Windows 10 Education |
| ✅ | Windows 10 Mobile |
| ✅ | Windows 10S |
| ✅ | Windows 10 Pro for Workstation |
| ✅ | Windows 10 Mobile Enterprise |
| ✅ | Windows 10 Team |
| ✅ | Windows 10 Pro Education |
| ✅ | Windows 10 N and KN |
<br>
 🎯 NOT DETECTABLE BY WINDOWS 10 DEFENDER 🎯 

##### ⚜️ WINDOWS 11:
| Windows Defender | Windows 11 |
| --- | --- |
| ❌ | Windows 11 Home |
| ❌ | Windows 11 Pro |
| ❌ | Windows 11 Enterprise |
| ❌ | Windows 11 Pro Education |
| ❌ | Windows 11 Pro for Workstations |
| ❌ | Windows 11 Education |
| ❌ | Windows 11 Mixed Reality |
| ❌ | Windows 11 Mixed Reality |
<br> 
 🎯 DETECTABLE BY WINDOWS 11 DEFENDER 🎯 
<br>
<br>
<br>

### 📹 VIDEO TUTORIAL
Video Tutorial: https://www.youtube.com/watch?v=gwfAshinEAw
<br>
<br>

###  🎃 INSTALL (LINUX)
``git clone https://github.com/zapeee/reverse-shell`` <br>
``cd reverse-shell`` <br>
``python start.py ``<br>

<br>

### ♻️ REVERSE SHELL EXPLEIN
What is a reverse shell?
A shell is a remotely connected terminal with another that allows you to execute commands remotely on a server. This is useful in different scenarios, but above all, it can be exploited by an attacker to steal sensitive information or run malicious tasks on a system.

<br>

A reverse shell refers to a process in which the victim's machine connects to the attacker's to receive commands. It is an efficient technique, since it evades firewalls and security filters of the traffic that enters the computer. For this reason, attackers often use these types of shells and it is also recommended to do so in penetration tests.

### 🦠 REVERSE SHELL EXPLEIN (code)
This section is to explain about the code, the code is obfuscated.<br>
What does obfuscated mean?<br>
Obfuscated means as hidden, not discoverable.<br>
<br>
The code is only made for WINDOWS, if you try it with Linux it will NOT let you do a reverse shell<br>

<br>

### 🪐 MAIN CONFIGURATION
Once you have established the session with the victim, you will have to execute this command ``shell`` ``ìd victim`` and you will be inside your pc

<br>

### 🔧 DOCKER
```FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip git

RUN git clone https://github.com/zapeee/reverse-shell.git /app
WORKDIR /app

RUN sed -i '/os/d' requirements.txt && \
    pip3 install -r requirements.txt

CMD [ "python3", "start.py" ]
```

<br>

### ⚖️ OUT OF LAN
Then we will go to our browser and write the address of our router, in most it is 192.168.1.1 and to start the default admin section. Then we will look for where it says port forwarding:
<br>
![Foto](https://i.ibb.co/bRkysnM/puertos-1.jpg)
<br>
We will open port 4444 and we will put the IP of our Kali Linux.

<br>

### ❓ HELP
Command              Description
help         [+]     Print this message.<br>
<br>
connect      [+]     Connect with a sibling server.<br>
<br>
siblings             Print sibling servers data table.<br>
<br>
sessions             Print established backdoor sessions data table.<br>
<br>
backdoors            Print established backdoor types data table.<br>
<br>
sockets              Print Villain related running services' info.<br>
<br>
shell        [+]     Enable an interactive pseudo-shell for a session.<br>
<br>
exec         [+]     Execute command/file against a session.<br>
<br>
upload       [+]     Upload files to a backdoor session.<br>
<br>
alias        [+]     Set an alias for a shell session.<br>
<br>
reset        [+]     Reset alias back to the session's unique ID.<br>
<br>
kill         [+]     Terminate an established backdoor session.<br>
<br>
conptyshell  [+]     Slap Invoke-ConPtyShell against a backdoor session.<br>
<br>
repair       [+]     Manually correct a session's hostname/username info.<br>
<br>
id                   Print server's unique ID (Self).<br>
<br>
cmdinspector [+]     Turn Session Defender on/off.<br>
<br>
threads              Print information regarding active threads.<br>
<br>
clear                Clear screen.<br>
<br>
exit                 Kill all sessions and quit.<br>

<br>

###  👾 Credits
The project to start the riversa shell is created by [t3l3machus](https://github.com/t3l3machus/Villain) , The project to create the riversa shell code NOT detect for Windows 10 is created by [zapeee](https://github.com/zapeee/reverse-shell) and the dockfile is by [El Pingüino de Mario](https://t.me/elpinguinohack)

<br>

by: @zapeee & @t3l3machus
Código ofuscado por: @asparuxz
