RPR_TOOL_DIR = os.path.join(WORK_DIR, '..', '..', '..', '..', 'RadeonProRenderSDK', 'RadeonProRender')

if platform.system() == 'Windows':
    RPR_TOOL_DIR = os.path.join(RPR_TOOL_DIR, "binWin64")
    RPR_TOOL = os.path.join(RPR_TOOL_DIR, "RprsRender64.exe")
elif platform.system() == 'Darwin':
    RPR_TOOL_DIR = os.path.join(RPR_TOOL_DIR, "binMacOS")
    RPR_TOOL = os.path.join(RPR_TOOL_DIR, "RprsRender64")
else:
    RPR_TOOL_DIR = os.path.join(RPR_TOOL_DIR, "binUbuntu18")
    RPR_TOOL = os.path.join(RPR_TOOL_DIR, "RprsRender64")


def core_render(case):     
    rpr_scene = os.path.join(RPR_TOOL_DIR, case['case'] + ".rpr")
    rpr_json = os.path.join(RPR_TOOL_DIR, case['case'] + ".json")
    
    if os.path.exists(rpr_scene) and os.path.exists(rpr_json):
        event('Prerender', False, case['case'])

        with open(os.path.abspath(rpr_json), 'r') as case_json:
            rpr_json_content = json.load(case_json)

        rpr_json_content['output'] = os.path.abspath(os.path.join(WORK_DIR, "Color", case['case'] + ".png"))

        with open(os.path.abspath(rpr_json), 'w') as case_json:
            json.dump(rpr_json_content, case_json)

        logging('Render image with RprsRenderer')

        command = ""
        if platform.system() != 'Windows':
            command = "LD_LIBRARY_PATH=" + os.path.abspath(os.path.join(RPR_TOOL_DIR))
            os.system('chmod +x ' + RPR_TOOL)
        command += " " + os.path.abspath(RPR_TOOL) + " " + os.path.abspath(rpr_scene) + " " + os.path.abspath(rpr_json)

        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE)
        
        try:
            stdout, stderr = p.communicate(timeout=600)
        except (subprocess.TimeoutExpired):
            logging("Render has been aborted by timeout")
            for child in reversed(p.children(recursive=True)):
                child.terminate()
            p.terminate()
        finally:
            stdout = stdout.decode("utf-8")
            stderr = stderr.decode("utf-8")
            logging("Core render logs:\n" + stdout + "\n ----STEDERR---- \n" + stderr)

        event('Postrender', True, case['case'])

        if os.path.exists(os.path.join(RPR_TOOL_DIR, case['case'] + "output.json")):
            with open(os.path.join(RPR_TOOL_DIR, case['case'] + "output.json"), 'r') as output_json:
                rpr_json_output = json.loads(output_json.read().replace("\\", "\\\\"))
                render_time = rpr_json_output["render.time.ms"] / 1000
                reportToJSON(case, render_time)
        else:
            logging("Case: " + case['case'] + ". There is no output.json file" )
    else:
        logging("Case: " + case['case'] + ". There is no .json or .rpr file for rendering" )
