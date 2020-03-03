def no_of_e(element):
	symbol = [
            'H','He',
            'Li','Be','B','C','N','O','F','Ne',
            'Na','Mg','Al','Si','P','S','Cl','Ar',
            'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe',
            'Co', 'Ni', 'Cu', 'Zn',
            'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
            'Rh', 'Pd', 'Ag', 'Cd',
            'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm',  'Eu',
            'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
            'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
            'Tl','Pb','Bi','Po','At','Rn']
	e_num=symbol.index(element)+1
	#print('no of electrons '+str(e_num))
	return e_num
#no_of_e('Ni')
#no_of_e('Ho')

def find_distance(a,b):
	dist=0.0
	for i in range (3):
		dist+=((a[i]-b[i])*(a[i]-b[i]))
	return dist

O=[0.000000000000,-0.143225816552,0.000000000000]
H=[1.638036840407,1.136548822547,-0.000000000000]
nO=no_of_e('O')
nH=no_of_e('H')
#print('no of electrons in O are '+str(nO))
#print('no of electrons in H are '+str(nH))
dist=find_distance(O,H)
#print('distance_between O and H '+str(dist))
