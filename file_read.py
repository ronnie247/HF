import numpy as np 

def file_read(file_name,nbasis):
    input_file=open(file_name)
    file_content=input_file.readlines()
    input_file.close()
    A=np.zeros([nbasis,nbasis])
    for line in file_content:
        V_line=line.rstrip()
        V_line=V_line.split()
        i=int(V_line[0])-1
        j=int(V_line[1])-1
        A[i][j]=float(V_line[2])
        A[j][i]=float(V_line[2])
    return A
