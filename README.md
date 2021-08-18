# md-traj-lipid-residence

### Routine of analyzing lipid map on protein

1. Load each frame of lipid structure:  
   `open chol-1.pdb`;   
2. Convert to mrc file in Chimera:  
   `molmap #0 3`, here 3 is the resolution; 
   `volume #0.1 save chol-map-$d.mrc`;  
3. Remove the structure and load the map:   
   `open chol-map-1.mrc`;  
   Adjust the threshold bar to show the lipid density clearly. 