from chimerax.core.commands import run # use 'rc' as shorthand for runCommand
import os
#from chimerax import replyobj 

basedir = "/home/sf/Documents/work/simulations/trpv2_proj/traj/"
for lipid in ["popc", "pope", "chl1", "sapi14"]: 
    #["sapi13", "sapi14", "sapi15"]:
    #lipid = "chl1"
    os.chdir(f"{basedir}/{lipid}")
    for i in range(1, 524):
        run(session,f"open {lipid}-{i:03d}.pdb")
        run(session,"molmap #1 3")
        run(session,f"save {lipid}-map-{i}.mrc #2")
        run(session,"close all")
    
    run(session, "open *mrc")
    
    str_ls = []
    for i in range(1, 524):
        str_ls.append(f"{i}")
    string = "volume add #"
    string += ','.join(str_ls)
    run(session, string)
    
    run(session, f"save {lipid}-merged.mrc #524")
    run(session, "close all")
