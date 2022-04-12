# Be care for hidden files like /.DStore

import os
workdir='/Users/.../seed number/'

ls=[]
os.chdir(workdir)
ls = filter(os.path.isfile, os.listdir(workdir))
ls = [os.path.join(workdir, f) for f in ls] # add path to each file
ls.sort(key=lambda x: os.path.getmtime(x))

ls_name = []
for a in range(1, len(ls)+1):
    tmp = '{}NO_{}.JPG'.format(workdir,str(a))
    ls_name.append(tmp)

if len(ls)==len(ls_name):
    for a in range(0,len(ls)):
        ori=ls[a]
        new=ls_name[a]
        os.rename(ori,new)
