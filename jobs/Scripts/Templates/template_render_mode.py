
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if current_scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

	scene = bpy.context.scene
	enable_rpr_render(scene)

	bpy.context.scene.rpr.render.render_mode = test_list[3]

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [

		["BL28_RS_RM_001", ["Render mode: Wireframe"], "ComplexTestUber.blend", 'WIREFRAME'], 
		["BL28_RS_RM_002", ["Render mode: Texcoord"], "ComplexTestUber.blend", 'TEXCOORD'],
		["BL28_RS_RM_003", ["Render mode: Position"], "ComplexTestUber.blend", 'POSITION'], 
		["BL28_RS_RM_004", ["Render mode: Normal"], "ComplexTestUber.blend", 'NORMAL'], 
		["BL28_RS_RM_005", ["Render mode: Material index"], "ComplexTestUber.blend", 'MATERIAL_INDEX'], 
		["BL28_RS_RM_006", ["Render mode: Global illumination"], "ComplexTestUber.blend", 'GLOBAL_ILLUMINATION'],
		["BL28_RS_RM_007", ["Render mode: Direct illumination no shadow"], "ComplexTestUber.blend", 'DIRECT_ILLUMINATION_NO_SHADOW'],
		["BL28_RS_RM_008", ["Render mode: Direct illumination"], "ComplexTestUber.blend", 'DIRECT_ILLUMINATION'], 
		["BL28_RS_RM_009", ["Render mode: Diffuse"], "ComplexTestUber.blend", 'DIFFUSE'],
		["BL28_RS_RM_010", ["Render mode: Ambient occlusion"], "ComplexTestUber.blend", 'AMBIENT_OCCLUSION']
		
	]
	
	launch_tests()

