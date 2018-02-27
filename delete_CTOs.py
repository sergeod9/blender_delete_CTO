''' This Script Deletes all Cutom Transform Orientations'''
import bpy

orient = bpy.context.scene.orientations.items()#A list containing Custom Orientations Objects, item [0] is the name
views = [area.spaces.active for area in bpy.context.screen.areas if area.type == 'VIEW_3D']
areas = [area for area in bpy.context.window.screen.areas if area.type == 'VIEW_3D']
for o in orient:
    if views and areas:
        views[0].transform_orientation = o[0]
        override = bpy.context.copy()
        override['area'] = areas[0]
        bpy.ops.transform.delete_orientation( override )
