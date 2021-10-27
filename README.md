# Identifying Lipid Residence Profile from MD Trajectories

This method is published in the manuscript "Endogenous (Lipid) / Exogenous (CBD) Ligands Modulation of TRPV2 Revealed by Computations". 



**Required programs**: ChimeraX, VMD

Automatic scripting: `chimerax-alllip.py`. 


### Converting PDB coordinates to EM map

1. Load each frame of lipid structure: 

   `open chol-1.pdb`;   

2. Convert to mrc file in Chimera:  

   `molmap #0 3`, here 3 is the resolution;   
   `volume #0.1 save chol-map-$d.mrc`;  

3. Remove the structure and load the map:  

   `open chol-map-1.mrc`;  

   Adjust the threshold bar to show the lipid density clearly. 



### Step I. Use VMD to write lipid-only PDB files (already aligned by protein backbone):

```tcl
#Set up a function for this purpose
proc write_lipids { resname } {
  set num [molinfo top get numframes]
  set lipid [string tolower $resname]
  for {set i 0} {$i < $num} {incr i} {
  animate goto $i
  set a [atomselect top "resname $resname and not hydrogen"]
  set filename $lipid-[format "%03d" $i].pdb
  file mkdir $lipid
  $a writepdb $lipid/$filename
}
}

#I have already make those dirs: chl1, pope, popc, sapi14, sapi13 etc.
write_lipids POPE
write_lipids POPC
write_lipids CHL1
write_lipids SAPI13
write_lipids SAPI14
write_lipids SAPI15

```



### Step II. Convert to EM map in ChimeraX and merge the maps

```python
# Take POPC lipid files as an example
lipid = 'popc'
for i in range(1, 524):
    print(f"open {lipid}-{i:03d}.pdb")
    print(f"molmap #1 3")
    print(f"save {lipid}-map-{i}.mrc #2")
    print("close all")

#Open the maps in the folder
open *mrc

#Print command for adding up volume
#Exec of this command takes a while
str_ls = []
for i in range(1, 524):
    str_ls.append(f"{i}")
string = "volume add #"
string += ','.join(str_ls)
print(string)

#Hide the dust
surface dust #524 size 
#Visuliaze the protein
#Drag and drop the protein PDB file

#Finally, save the merged Map:
save {lipid}-merged.mrc #524
```

#### 



Any questions? Contact shalltime@gmail.com, Shasha Feng
