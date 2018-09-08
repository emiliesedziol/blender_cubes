# 4 cubes starting at the same point but going in opposite directions
import bpy

print("start");
# start at
xaxis = -1.5;
yaxis = 3;
zaxis = .0;
c = 0;

print ("inside spiral")

def add_image():
    global zaxis;
    global xaxis;
    global yaxis;
    global c;

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(xaxis, yaxis, zaxis), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False));
    c = c + 1
    activeObject = bpy.context.active_object
    mat = bpy.data.materials.new(name="MaterialName")
    activeObject.data.materials.append(mat) 
    if only_even(c):
        bpy.context.object.active_material.diffuse_color = (0, 0, 0)
    else:
        bpy.context.object.active_material.diffuse_color = (250, 0, 0) 
        
    bpy.context.scene.update();


def only_even(e):
    if (e % 2 == 1):
        return False
    return True


bpy.app.driver_namespace['add_image'] = add_image;
for x in range(2):
    if x == 1:
        xaxis = -1.5;
        yaxis = 3;
        zaxis = .0; 

    if x == 2:
        xaxis = 1.5;
        yaxis = -3;
        zaxis = .0;

    for i in range(12):
        print("x " + str(x) + " xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
        add_image()
        zaxis = zaxis + .5
        if i <=4:
            xaxis = xaxis - .75;
            yaxis = yaxis - 1.2;
                
        if i > 4 and i <= 8:
            xaxis = xaxis + .75;
            yaxis = yaxis - 1.2;

        if i > 8 and i <= 12:
            xaxis = xaxis + .75;
            yaxis = yaxis + 1.2;
                
        if i > 12:
            xaxis = xaxis - .75;
            yaxis = yaxis + 1.2;



# exec(compile(open('d:/blender/spiral.py').read(), 'd:/blender/spiral.py', 'exec'))

