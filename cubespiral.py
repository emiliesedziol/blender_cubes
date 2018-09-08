# 4 cubes starting at: x 7 - y 1, x 1 - y -7, x 1 - y 7, x -7 y 1
# ending at the same x y coordinates.  z started at 1 up to 29 
import bpy

print("start");
c = 0;
even_color_1 = 0
even_color_2 = 0
even_color_3 = 0
odd_color_1 = 255
odd_color_2 = 225
odd_color_3 = 225

print ("inside spiral")

def add_image():
    global zaxis;
    global xaxis;
    global yaxis;
    global c;
    global even_color_1;
    global even_color_2;
    global even_color_3;
    global odd_color_1;
    global odd_color_2;
    global odd_color_3;

    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(xaxis, yaxis, zaxis), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False));
    c = c + 1
    activeObject = bpy.context.active_object
    mat = bpy.data.materials.new(name="MaterialName")
    activeObject.data.materials.append(mat) 
    if only_even(c):
        bpy.context.object.active_material.diffuse_color = (even_color_1, even_color_2, even_color_3)
    else:
        bpy.context.object.active_material.diffuse_color = (odd_color_1, odd_color_2, odd_color_3) 
        
    bpy.context.scene.update();


def only_even(e):
    if (e % 2 == 1):
        return False
    return True


bpy.app.driver_namespace['add_image'] = add_image;

print("first")
for i in range(4):
    if i == 0:
        xaxis = 1
        yaxis = 7
        zaxis = 1
        print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
        add_image()
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()


    if i == 1:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()
    
    if i == 2:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()

    if i == 3:
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()


print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
for i in range(4):
    print("second")
    odd_color_1 = 0
    odd_color_2 = 0
    old_color_2 = 255
    if i == 0:
        xasis = 1
        yaxis = -7
        zaxis = 1
        print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
        add_image()
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()

    if i == 1:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()
    
    if i == 2:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()

    if i == 3:
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()
        

print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
for i in range(4):
    print("Third")
    odd_color_1 = 0
    odd_color_2 = 255
    old_color_2 = 0
    if i == 0:
        xaxis = -7
        yaxis = 1
        zaxis = 1
        print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
        add_image()
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()

    if i == 1:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()
    
    if i == 2:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()

    if i == 3:
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()


print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
for i in range(4):
    print("fourth")
    odd_color_1 = 255
    odd_color_2 = 0
    old_color_2 = 0
    if i == 0:
        xaxis = 7
        yaxis = -1
        zaxis = 1
        print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
        add_image()
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()

    if i == 1:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis - .5
            zaxis = zaxis + .5
            add_image()
    
    if i == 2:
        for j in range(14):
            xaxis = xaxis + .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()

    if i == 3:
        for j in range(14):
            xaxis = xaxis - .5
            yaxis = yaxis + .5
            zaxis = zaxis + .5
            add_image()


print(" xaxis " + str(xaxis) + " yaxis " + str(yaxis) + " zaxis " + str(zaxis))
# exec(compile(open('d:/blender/test.py').read(), 'd:/blender/test.py', 'exec'))

