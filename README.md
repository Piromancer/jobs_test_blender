# Autotests for Radeon ProRender plugin for Blender

## Install
 1. Clone this repo
 2. Get `jobs_launcher` as git submodule, using next commands
 `git submodule init`
 `git submodule update`
 3. Check that `BlenderAssets` scenes placed in `C:/TestResources`
 4. Run `scripts/run.bat` with customised `--cmd_variables`. For example:

     > --cmd_variables Tool "C:\Program Files\Blender Foundation\Blender\blender.exe" RenderDevice 'gpu' TestsFilter small
     * Tool define path to Blender
     * RenderDevice define what hardware will be used.
         'gpu' - GPU
         'cpu' - CPU
     * TestsFilter takes only `small` or `full`, and define count of scenes that will be send ot render.

## How to update weights.json
 1. Move to jobs_launcher
 2. Init jobs_launcher submodule by commnad: git submodule update --init
 3. Move to common/scripts/manual
 4. Download from Weekly report session_report.json (Add FULL/summary_report.json or FULL2/summary_report.json to url with report)
 5. Run generation of new weights.json: python3 analyze_summary_report.py --path <path_to_summary_report.json> --results_path <where_to_save_weight.json>
 6. Move new weight.json to jobs_test_blender/jobs/
