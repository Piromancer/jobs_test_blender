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
        logging('Render image')
        logging("Run command: " + RPR_TOOL + " " + case_rpr + " " + case_json)
        event('Prerender', False, case['case'])
        event('Postrender', True, case['case'])
        start_time = datetime.datetime.now()
        process = subprocess.Popen(RPR_TOOL + " " + case_rpr + " " + case_json, stdout=subprocess.PIPE, shell=True)
        render_time = (datetime.datetime.now() - start_time).total_seconds()

        case['status'] = 'done'
        event('Postrender', True, case['case'])
        reportToJSON(case, render_time)
    else:
        logging("Case: " + case['case'] + ". There is no .json or .rpr file for rendering" )

