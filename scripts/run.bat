set PATH=c:\python35\;c:\python35\scripts\;%PATH%
set RENDER_DEVICE=%1
set FILE_FILTER=%2
set TESTS_FILTER="%3"

python ..\jobs_launcher\executeTests.py %4 %5 --test_filter %TESTS_FILTER% --file_filter %FILE_FILTER% --tests_root ..\jobs --work_root ..\Work\Results --work_dir Blender --cmd_variables Tool "C:\Program Files\Blender Foundation\Blender\blender.exe" RenderDevice %RENDER_DEVICE% ResPath "C:\TestResources\BlenderAssets\scenes" PassLimit 50 rx 0 ry 0
