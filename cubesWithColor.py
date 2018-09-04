# Gren for 'nonsubscriber' and red for cubes with names
import bpy
from random import randint

zaxis = -35;
myArrayNames = [];
alreadyUsedName = [];

def add_image(x):
    global zaxis;
    zaxis = zaxis + .25;
    bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, zaxis), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False));
    bpy.context.active_object.name = 'nonsubscriber_'+str(x);
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0, 255, 0) #change color
    bpy.context.scene.update();
    # print(x);


def rename_image(ob,a,x):
    global myArrayNames;
    while True:
        if (hasattr(ob, "select")):
            ob.select = True;
            bpy.context.scene.objects.active = ob;
            bpy.context.active_object.name = myArrayNames[x];
            activeObject = bpy.context.active_object #Set active object to variable
            mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
            activeObject.data.materials.append(mat) #add the material to the object
            bpy.context.object.active_material.diffuse_color = (255, 0, 0) #change color
            bpy.context.scene.update();
            break;
        else:
            # print("could not select");
            a = randint(1, 250);
            # print('nonsubscriber_'+str(a));
            #  print(myArrayNames[x] + " " + str(x));
            ob = bpy.data.objects.get('nonsubscriber_'+str(a));

bpy.app.driver_namespace['add_image'] = add_image;
list_open = open('D:/namesForObject.txt', "rt");
read_list = list_open.read();
line_in_list = read_list.split('\n');
for x in line_in_list:
    myArrayNames.append(x);

# print(myArrayNames);

for i in range(250):
    add_image(i);

for x in range(30):
    a = randint(1, 250);
    b = randint(1,30);
    while True:
        if b in alreadyUsedName:
            # print(str(b) + " name has already been used " + myArrayNames[b]);
            b = randint(1,30);
        else:
            # print(str(b) + " has not been used " + myArrayNames[b]);
            alreadyUsedName.append(b);
            break;

    # print('nonsubscriber_'+str(a));
    # print(myArrayNames[x] + " " + str(x));
    ob = bpy.data.objects.get('nonsubscriber_'+str(a));
    rename_image(ob,a,b);

list_open.close();
list_open = None;


#  exec(compile(open('d:/blender/cubesWithColor.py').read(), 'd:/blender/cubesWithColor.py', 'exec'))