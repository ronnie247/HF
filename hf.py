#program to calculate hf energy
#read the geometry
import os
import numpy as np
from hf2 import no_of_e

input_file=open('geom.dat','r') #r to read, w to write, a to append
file_content=input_file.readlines()
input_file.close() #closing is important
#print(file_content)

#store the input in list

temp_geom=[]
for line in file_content:
	v_line=line.rstrip() #only remove the whitespaces after the line
	#f=v_line.split()
	if (len(v_line)>0):  #take in only non zero lines, in case any whitespace was there, it would have been removed by rstrip
		temp_geom.append(v_line.split())

#print(temp_geom[1][0])

#number of atoms
NATOM=int(temp_geom[0][0])
#print('No. of atoms '+str(NATOM))

#geom=temp_geom[1:(NATOM+1)]
#print(geom)
#above could be used, creating a new geometry matrix, but uses double memory

ATOM_SYMBOL=[] #contains the atom symbols
GEOM=[] #contains coordinates
for i in range(1, NATOM+1):
	ATOM_SYMBOL.append(temp_geom[i][0])
	GEOM.append(temp[i][1:3]) #slicing
#print(ATOM_SYMBOL)

#total e in the molecule
totale=0
for i in range(1, NATOM+1):
	totale+=no_of_e(temp_geom[i][0])
print('Total electrons are '+str(totale))
