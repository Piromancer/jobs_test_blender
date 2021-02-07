def core_Render(case):
    RPR_TOOL = os.path.abspath("run.bat").rsplit("\\", 2)[0] + "\\RadeonProRenderSDK\\RadeonProRender\\"

    if (platform.system() == 'Windows'):
        RPR_TOOL += "binWin64\\RprsRender64.exe"
    elif (platform.system() == 'Darwin'):
        RPR_TOOL += "binUbuntu18\\RprsRender64"
    else:   
        RPR_TOOL += "binMacOS\\RprsRender64"

    case_rpr = RPR_EXPORT_DIR + case['case'] + ".rpr"
    case_json = RPR_EXPORT_DIR + case['case'] + ".json"
    if os.path.exists(case_rpr) and os.path.exists(case_json):
        logging("Run command: " + RPR_TOOL + " " + case_rpr + " " + case_json)
        process = subprocess.Popen(RPR_TOOL + " " + case_rpr + " " + case_json, stdout=subprocess.PIPE, shell=True)
        output = process.communicate()
        replace_results(case, RPR_EXPORT_DIR + case['case'] + ".png")
    else:
        logging("Case: " + case['case'] + ". There is no .json or .rpr file for rendering" )

def replace_results(case, result_def):
    output = WORK_DIR + "\\Color\\" + case['case'] + ".png"
    if os.path.exists(result_def):
        os.replace(result_def,output)
    else:
        logging("Case: " + case['case'] + ". There is no result .png file" )