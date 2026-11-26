
def tray(spec, n=3, clearance=0.3,
         wall=4.0, thickness=6.0,
         depth=3.0, rows=2):

    pocket_r = spec.r_cell + clearance
    pitch = 2 * pocket_r + wall

    plate = cf.box(
        n * pitch + wall,
        rows * pitch + wall,
        thickness
    )

    pocket = cf.cylinder(
        d=2 * pocket_r,
        h=depth + 1
    ).moved(z=thickness - depth)

    for i in range(n):
        for j in range(rows):
            x = (i - (n - 1) / 2) * pitch
            y = (j - (rows - 1) / 2) * pitch

            plate = plate - pocket.moved(x=x, y=y)

    return plate
