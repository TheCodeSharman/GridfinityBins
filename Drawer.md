Width: 1045mm / 42mm = 24.88 
Depth: 370mm / 42mm = 8.8 

build plate 
Width: 250mm / 42mm = 5.95
Depth: 210mm / 42mm = 5

so lets do 5 x 5 bases, in a grid like:

5x34mm - 5x34mm - 5x34mm - 5x34mm - 4x34mm - 
  5x3  -   5x3  -   5x3  -   5x3  -   4x3  - 37mmx3 
  5x5  -   5x5  -   5x5  -   5x5  -   4x5  - 37mmx5

1045mm - ((5*4+4)*42mm) = 37mm
370mm - ((5 + 3)*42mm) = 34mm

gfbase -x 5 -y 5 -o drawer-base-5x5.step --short
gfbase -x 4 -y 5 -o drawer-base-4x5.step --short
gfbase -x 5 -y 3 -o drawer-base-5x3.step --short
gfbase -x 4 -y 3 -o drawer-base-4x3.step --short
gfedge -x 5 -y 34 -o drawer-top-edge-5x34mm.step --short
gfedge -x 4 -y 34 -o drawer-top-edge-4x34mm.step --short
gfedge -x 5 -y 37 -o drawer-right-edge-37mmx5.step --short
gfedge -x 3 -y 37 -o drawer-right-edge-37mmx3.step --short

