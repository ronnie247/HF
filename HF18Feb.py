#This a program to calculate the Hatree-Fock energy of a closed shell molecule
import numpy as np
from hf2 import no_of_e
from distance import find_distance
#from read_two_e import read_2_e
from file_read import file_read
#Read the geometry
input_file=open('geom.dat')   #open the file

file_content=input_file.readlines()# read the content

input_file.close()            # close the file

#print(file_content)


# store the input in list
temp_geom=[]
for line in file_content:
  v_line=line.rstrip()
  if len(v_line)>0:
   temp_geom.append(v_line.split())

print(temp_geom)


#no of atoms
NATOM=int(temp_geom[0][0])

print('Total no of atom '+str(NATOM))

ATOM_SYMBOL=[] # this list contains the atom symbols

GEOM=[] # cartesian coordinate

for i in range(1,NATOM+1): 
 ATOM_SYMBOL.append(temp_geom[i][0])
 GEOM.append(temp_geom[i][1:4])
 
 
print('Atom Symbol')
#print(ATOM_SYMBOL)

print('Cartesian Coordinate in a.u.')
#print(GEOM)

# count the total no of electrons

NE=0  #this is the total no of electron

for i in range(len(ATOM_SYMBOL)):
 k=no_of_e(ATOM_SYMBOL[i])
 NE+=k 
 
print('Total no of electron is '+str(NE))

#calculate the nuclear repulsion energy
E_nuc=0.0
for i in range(NATOM):
    for j in range(0,i):
         Z_a=no_of_e(ATOM_SYMBOL[i])
         Z_b=no_of_e(ATOM_SYMBOL[j])
         R_ab=find_distance(GEOM[i],GEOM[j])
         print(R_ab)
         E_nuc+=(Z_a*Z_b)/R_ab
print('Nuclear repulsion energy '+str(E_nuc)+ ' a.u.')

#basis set dimension
nbasis=7
#Read one electron integrals 
#Read S,V,T
S=np.zeros([nbasis,nbasis])
V=np.zeros([nbasis,nbasis])
T=np.zeros([nbasis,nbasis])
Hcore=np.zeros([nbasis,nbasis])
S=file_read('s.dat',nbasis)
V=file_read('v.dat',nbasis)
T=file_read('t.dat',nbasis)
#store the core potential
Hcore=V+T
#print(Hcore)
#twoe=read_2_e(nbasis)
#print(twoe)



