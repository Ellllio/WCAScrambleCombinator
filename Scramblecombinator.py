import os
import zipfile
import shutil
vlightning = 'Round'
vmcqueen = 'Scramble Set'
vkachoow ='.txt'
print('░██████╗░█████╗░██████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗  ')
print('██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝  ')
print('╚█████╗░██║░░╚═╝██████╔╝███████║██╔████╔██║██████╦╝██║░░░░░█████╗░░  ')
print('░╚═══██╗██║░░██╗██╔══██╗██╔══██║██║╚██╔╝██║██╔══██╗██║░░░░░██╔══╝░░  ')
print('██████╔╝╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██████╦╝███████╗███████╗  ')
print('╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚══════╝')
print('░█████╗░░█████╗░███╗░░░███╗██████╗░██╗███╗░░██╗░█████╗░████████╗░█████╗░██████╗░')
print('██╔══██╗██╔══██╗████╗░████║██╔══██╗██║████╗░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗')
print('██║░░╚═╝██║░░██║██╔████╔██║██████╦╝██║██╔██╗██║███████║░░░██║░░░██║░░██║██████╔╝')
print('██║░░██╗██║░░██║██║╚██╔╝██║██╔══██╗██║██║╚████║██╔══██║░░░██║░░░██║░░██║██╔══██╗')
print('╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝██║██║░╚███║██║░░██║░░░██║░░░╚█████╔╝██║░░██║')
print('░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝')
print('██╗░░░██╗██████╗░░█████╗░██████╗░░░███╗░░░░░██████╗░')
print('██║░░░██║╚════██╗██╔══██╗╚════██╗░████║░░░░░╚════██╗')
print('╚██╗░██╔╝░░███╔═╝██║░░██║░░███╔═╝██╔██║░░░░░░░███╔═╝')
print('░╚████╔╝░██╔══╝░░██║░░██║██╔══╝░░╚═╝██║░░░░░██╔══╝░░')
print('░░╚██╔╝░░███████╗╚█████╔╝███████╗███████╗██╗███████╗')
print('░░░╚═╝░░░╚══════╝░╚════╝░╚══════╝╚══════╝╚═╝╚══════╝')
print(' What is your filename? ', end='')
filename = str(input()) 
with zipfile.ZipFile(filename,'r') as zip:
	zip.printdir()
	zip.extractall('temp/')
print ('What event?')
print ('[A]3x3 [B]Pyraminx [C]Clock [D]Square-1 [E]4x4 [F]Skewb [G]2x2x2 [H]3x3x3 OH')
event = str(input())
if event =='A' or event =='a':
   vevent = '3x3x3'
elif event == 'B' or event =='b':
   vevent = 'Pyraminx'
elif event =='C'or event =='c':
	vevent = 'Clock'
elif event == 'D' or event =='d':
	vevent = 'Square-1'
elif event == 'E' or event =='e':
  vevent = '4x4x4'
elif event == 'F' or event =='f':
  vevent = 'Skewb'
elif event == 'G' or event =='g':
  vevent = '2x2x2'
elif event == 'H' or event =='h':
  vevent = '3x3x3 One-Handed'
else: 
	print ('That input is not valid')
print ('How many text files? (max 26)')
vtxtfls = int(input())
print ('How many rounds? (max 4)')
vrounds = int(input())
vfilename =[]
for vround in range (vrounds):
 for vset in range(vtxtfls):
  if vset == 25: 
   vfilename1 = 'temp/Interchange/txt/' + vevent + ' ' + vlightning + ' ' + str(vround+1) + ' ' + vmcqueen + ' '	+ chr(vset+64) + vkachoow 
  else:
   vfilename1 = 'temp/Interchange/txt/' + vevent + ' ' + vlightning + ' ' + str(vround+1) + ' ' + vmcqueen + ' '	+ chr(vset+65) + vkachoow
   vfilename.append (vfilename1)
with open('combined/Combined.txt', 'w') as outfile:
    for names in vfilename:
        with open(names) as infile:
            outfile.write(infile.read())
        outfile.write("\n")

shutil.rmtree('temp')