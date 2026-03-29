"""
Gridfinity nozzle-tip holder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Imports 2x3x6U-bin.step and adds one cylindrical peg per cell.
Nozzle tips press onto the pegs.  Each peg has a lead-in chamfer at
the top to guide the tip on.
"""

from build123d import *

# ── Tune these ────────────────────────────────────────────────────────────────
TIP_INNER_DIAMETER = 21.62   # measured inside diameter of nozzle tip, mm
FIT_CLEARANCE      =  0.30   # subtracted from diameter so peg slides into tip, mm
PEG_HEIGHT         = 12.00   # how tall each peg stands above the bin top, mm
LEAD_IN            =  1.50   # chamfer size on top of peg to guide insertion, mm

CELL_SIZE          = 42.00   # gridfinity cell pitch (spec), mm
GRID_X             =  2      # cells in X
GRID_Y             =  3      # cells in Y

INPUT_STEP         = "2x3x3U-unadorned-bin.step"
OUTPUT_STEP        = "nozzle-tip-bin.step"
# ─────────────────────────────────────────────────────────────────────────────

peg_radius = (TIP_INNER_DIAMETER - FIT_CLEARANCE) / 2

# Import base bin
base = import_step(INPUT_STEP)

# Reference geometry — interior floor is the largest upward-facing face
floor_z = base.faces().filter_by(Axis.Z).sort_by(SortBy.AREA)[-1].center().Z
bb      = base.bounding_box()
cx      = bb.center().X
cy      = bb.center().Y

# Build the peg shape: cylinder + lead-in cone on top, both growing upward
with BuildPart() as peg_tool:
    Cylinder(
        radius=peg_radius,
        height=PEG_HEIGHT,
        align=(Align.CENTER, Align.CENTER, Align.MIN),
    )
    # Lead-in cone narrows toward the top to guide the tip on
    with Locations(Location((0, 0, PEG_HEIGHT))):
        Cone(
            bottom_radius=peg_radius,
            top_radius=peg_radius - LEAD_IN,
            height=LEAD_IN,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )

peg = peg_tool.part

with BuildPart() as bp:
    add(base)

    for i in range(GRID_X):
        for j in range(GRID_Y):
            x = cx + (i - (GRID_X - 1) / 2) * CELL_SIZE
            y = cy + (j - (GRID_Y - 1) / 2) * CELL_SIZE
            with Locations(Location((x, y, floor_z))):
                add(peg, mode=Mode.ADD)

export_step(bp.part, OUTPUT_STEP)
print(f"Wrote {OUTPUT_STEP}")
print(f"  {GRID_X * GRID_Y} pegs  ⌀{peg_radius * 2:.2f} mm × {PEG_HEIGHT} mm tall")
print(f"  Lead-in chamfer {LEAD_IN} mm at tip")

# OCP CAD Viewer (VS Code extension)
from ocp_vscode import show, set_port
set_port(3939)
show(bp.part)
