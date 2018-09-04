# try an outside script
import bpy

zaxis = -5;

def add_image(x):
    global zaxis;
    zaxis = zaxis + .25;
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, zaxis), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False));
    bpy.context.active_object.name = x;
    bpy.context.scene.update();


bpy.app.driver_namespace['add_image'] = add_image;
list_open = open('D:/namesForObject.txt', "rt");
read_list = list_open.read();
line_in_list = read_list.split('\n');
for x in line_in_list:
    print(x);
    print(zaxis);
    add_image(x);
    zaxis = zaxis + .25;


list_open.close();
list_open = None;


# exec(compile(open('d:/blender/cubes.py').read(), 'd:/blender/cubes.py', 'exec'))

