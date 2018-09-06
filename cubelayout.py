# 4 cubes starting at the same point but going in opposite directions
import bpy

xaxis_1 = -1;
yaxis_1 = 1;
zaxis_1 = 1;

xaxis_2 = 1;
yaxis_2 = -1;
zaxis_2 = 1;
xaxis_3 = -1;
yaxis_3 = -1;
zaxis_3 = -1;
xaxis_4 = 1;
yaxis_4 = 1;
zaxis_4 = -1;
c = 0;
d = 0;
e = 0;
f = 0;

def add_image():
    global zaxis_1;
    global xaxis_1;
    global yaxis_1;
    global zaxis_2;
    global xaxis_2;
    global yaxis_2;
    global zaxis_3;
    global xaxis_3;
    global yaxis_3;
    global zaxis_4;
    global xaxis_4;
    global yaxis_4;
    global c;
    global d;
    global e;
    global f;

    for i in range(5):
        if i == 2:
            bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(xaxis_1, yaxis_1, zaxis_1), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False));
            c = c + 1
            activeObject = bpy.context.active_object
            mat = bpy.data.materials.new(name="MaterialName")
            activeObject.data.materials.append(mat) 
            if only_even(c):
                bpy.context.object.active_material.diffuse_color = (0, 0, 0)
            else:
                bpy.context.object.active_material.diffuse_color = (250, 0, 0) 
        
        if i == 1:
            bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(xaxis_2, yaxis_2, zaxis_2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            d = d + 1
            activeObject = bpy.context.active_object
            mat = bpy.data.materials.new(name="MaterialName")
            activeObject.data.materials.append(mat)
            if only_even(d):
                bpy.context.object.active_material.diffuse_color = (0, 0, 0) #
            else:
                bpy.context.object.active_material.diffuse_color = (0, 255, 0) # 
        
        if i == 3:
            bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(xaxis_3, yaxis_3, zaxis_3), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False));
            e = e + 1
            activeObject = bpy.context.active_object
            mat = bpy.data.materials.new(name="MaterialName")
            activeObject.data.materials.append(mat)
            if only_even(c):
                bpy.context.object.active_material.diffuse_color = (0, 0, 0) 
            else:
                bpy.context.object.active_material.diffuse_color = (0, 0, 255) 

        if i == 4:
            bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(xaxis_4, yaxis_4, zaxis_4), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False));
            f = f + 1
            activeObject = bpy.context.active_object
            mat = bpy.data.materials.new(name="MaterialName")
            activeObject.data.materials.append(mat)
            if only_even(c):
                bpy.context.object.active_material.diffuse_color = (0, 0, 0) #
            else:
                bpy.context.object.active_material.diffuse_color = (255, 230, 220) # 

    bpy.context.scene.update();
    xaxis_1 = xaxis_1 - .5;
    yaxis_1 = yaxis_1 + .5;
    zaxis_1 = zaxis_1 + .5;
    xaxis_2 = xaxis_2 + .5;
    yaxis_2 = yaxis_2 - .5;
    zaxis_2 = zaxis_2 + .5;
    xaxis_3 = xaxis_3 - .5;
    yaxis_3 = yaxis_3 - .5;
    zaxis_3 = zaxis_3 - .5;
    xaxis_4 = xaxis_4 + .5;
    yaxis_4 = yaxis_4 + .5;
    zaxis_4 = zaxis_4 - .5;


def only_even(e):
    if (e % 2 == 1):
        return False
    return True


bpy.app.driver_namespace['add_image'] = add_image;
list_open = open('D:/namesForObject.txt', "rt");
read_list = list_open.read();
line_in_list = read_list.split('\n');
for x in range(15):
    add_image();



# exec(compile(open('d:/blender/cubelayout.py').read(), 'd:/blender/cubelayoput.py', 'exec'))

