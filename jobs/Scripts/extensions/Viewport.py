def save_viewport(case):
    for area in bpy.context.window_manager.windows[0].screen.areas:
        if area.type == 'VIEW_3D':
            mycontext = bpy.context.copy()
            mycontext["area"] = area
            for space in area.spaces:
                if space.type == 'VIEW_3D': 
                    space.shading.type = 'RENDERED'
                    #context = dict([('area', area), ('region', None)])
                    bpy.ops.screen.screenshot(  'EXEC_SCREEN', filepath=os.path.join(WORK_DIR, 'Color', case['case']))
                    
                    #bpy.ops.render.opengl(bpy.context, write_still=True)
                    break 
    
            

                    
