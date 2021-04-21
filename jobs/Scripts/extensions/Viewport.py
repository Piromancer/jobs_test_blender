def save_viewport(case):
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            context = dict([('area', area), ('region', None)])
            bpy.ops.screen.screenshot(context, filepath=os.path.join(WORK_DIR, 'Color', case['case']), full=False)
            break 
                    
