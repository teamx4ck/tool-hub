from time import sleep
from os import system as sy
import sys
from pyfiglet import figlet_format as ff
def dp(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.1)
def git(link):
	sy('git clone '+link)
red = '\u001b[31;1m'
cyn='\u001b[34;1m'
res='\u001b[0m'
print('\u001b[36;1m',ff('Tool-Hub'),'\u001b[0m')
print(red+'[1] '+cyn+'Install Tool\n\n'+red+'[2] '+cyn+'More Tools by Me\n\n'+red+'[3] '+cyn+'Join FB\n\n'+red+'[0] Exit'+res)
opt = input('\n[>] \u001b[36mEnter Your Option : \u001b[0m')
if opt=='1':
	sy('clear')
	dp(cyn+'\nPlease wait....\u001b[0m\n')
	sleep(1)
	sy('clear')
	print(red+ff('Tool-Hub'))
	sleep(.5)
	print(cyn)
	print(open('config','r').read())
	print(red+'[00] Back')
	print(res)
	top=input('\n[>] \u001b[36mEnter Your Option : \u001b[0m')
	if top=='1':
		sy('git clone https://github.com/sqlmapproject/sqlmap')
	elif top=='2':
		sy('git clone https://github.com/cyweb/hammer')
	elif top=='3':
		sy('git clone https://github.com/teamx4ck/x4dos')
	elif top=='4':
		sy('git clone https://github.com/teamx4ck/xcan')
	elif top=='5':
		sy('git clone https://github.com/teamx4ck/x4sms')
	elif top=='6':
		sy('git clone https://github.com/teamx4ck/x4web')
	elif top=='7':
		sy('git clone https://github.com/Ign0r3dH4x0r/BloodyIP')
	elif top=='8':
		sy('git clone https://github.com/Audi0x01/D-TECT-1')
	elif top=='9':
		sy('git clone https://github.com/xadrian57/psqli')
	elif top=='10':
		sy('apt install nmap')
	elif top=='11':
		sy('git clone https://github.com/rapid7/metasploit-framework')
	elif top=='12':
		sy('git clone https://github.com/htr-tech/zphisher')
	elif top=='13':
		sy('git clone https://github.com/htr-tech/nexphisher')
	elif top=='14':
		sy('git clone https://github.com/teamx4ck/X4URL')
	elif top=='15':
		sy('git clone https://github.com/teamx4ck/Xzip')
	elif top=='16':
		sy('git clone https://github.com/adi1090x/termux-style')
	elif top=='17':
		sy('git clone https://github.com/maurosoria/dirsearch')
	elif top=='18':
		git('https://github.com/Oseid/FaceBoom')
	elif top=='19':
		sy('git clone https://github.com/htr-tech/afgcrack')
	elif top=='20':
		sy('git clone https://github.com/htr-tech/track-ip')
	elif top=='21':
		sy('git clone https://github.com/htr-tech/haxorbd')
	elif top=='22':
		git('https://github.com/htr-tech/unfollow-plus')
	elif top=='23':
		git('https://github.com/htr-tech/indocreak')
	elif top=='24':
		git('https://github.com/htr-tech/pakcreak')
	elif top=='25':
		git('https://github.com/root-plinix/Floxin')
	elif top=='26':
		git('https://github.com/root-plinix/BrutEye')
	elif top=='27':
		git('https://github.com/root-plinix/Brutal')
	elif top=='28':
		git('https://github.com/Ign0r3dH4x0r/GenVirus')
	elif top=='29':
		git('https://github.com/Ign0r3dH4x0r/Quack')
	elif top=='30':
		git('https://github.com/noob-hackers/spamx')
	elif top=='31':
		git('https://github.com/noob-hackers/ighack')
	elif top=='32':
		git('https://github.com/noob-hackers/hacklock')
	elif top=='33':
		git('https://github.com/noob-hackers/grabcam')
	elif top=='34':
		git('https://github.com/noob-hackers/mrphish')
	elif top=='35':
		git('https://github.com/noob-hackers/ipdrone')
	elif top=='36':
		git('https://github.com/noob-hackers/infect')
	elif top=='37':
		git('https://github.com/Amerlaceset/Virus4')
	elif top=='38':
		git('https://github.com/htr-tech/host')
	elif top=='39':
		git('https://github.com/rajkumardusad/onex')
	elif top=='40':
		git('https://github.com/rixon-cochi/Lucifer.git')
	elif top=='0' or top=='00':
		sy('python tool-hub.py')
	else:
		print(red+ff('Error')+'option not found!!'+res)
elif opt=='2':
	sy('xdg-open https://www.github.com/teamx4ck')
elif opt=='3':
	sy('xdg-open https://m.facebook.com/groups/x4ckcyberarmy')
elif opt=='0' or opt=='00':
	sleep(1.5)
	print(cyn+ff('bye')+res)
else:
	print(red+ff('Error')+'option not found!!'+res)
