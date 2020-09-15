set PATH=c:\python35\;c:\python35\scripts\;%PATH%
set PYTHONPATH=..\jobs_launcher\;%PYTHONPATH%

set DELETE_BASELINES=%1
if not defined DELETE_BASELINES set DELETE_BASELINES=False

python ..\jobs_launcher\common\scripts\generate_baselines.py --results_root ..\Work\Results\Blender28 --baseline_root ..\Work\Baseline --remove_old %DELETE_BASELINES%