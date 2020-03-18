import argparse
import os
import json
import datetime


errors = [
    {'error': 'rprCachingShadersWarningWindow',
     'message': 'Render cache built during cases'},
    {'error': 'Error: Radeon ProRender: IO error',
     'message': 'Some files/textures are missing'}
]


def createArgsParser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--output', required=True, metavar='<dir>')

    return parser


def main(args):
    work_dir = os.path.abspath(args.output)
    files = [f for f in os.listdir(
        work_dir) if os.path.isfile(os.path.join(work_dir, f))if 'renderTool' in f]

    logs = ''

    for f in files:
        logs += '\n\n\n----------LOGS FROM FILE ' + f + '----------\n\n\n'
        with open(os.path.realpath(os.path.join(os.path.abspath(args.output), f))) as log:
            logs += log.read()
        os.remove(os.path.realpath(os.path.join(
            os.path.abspath(args.output), f)))

    log_path = ''
    for line in logs.splitlines():
        if [l for l in ['Save report', 'Create log'] if l in line]:
            log_path = os.path.join(os.path.abspath(
                args.output), 'render_tool_logs', line.split().pop() + '.log')
        if os.path.exists(log_path):  # throw exception while log_path == ''
            with open(log_path, 'a') as log_file:
                log_file.write(line + '\n')

    with open(os.path.realpath(os.path.join(os.path.abspath(args.output), 'renderTool.log')), 'w') as f:
        for error in errors:
            if error['error'] in logs:
                f.write('[Error] {}\n'.format(error['message']))

        f.write('\n\nCases statuses from test_cases.json\n\n')

        cases = json.load(open(os.path.realpath(
            os.path.join(os.path.abspath(args.output), 'test_cases.json'))))

        f.write('Active cases: {}\n'.format(
            len([n for n in cases if n['status'] == 'active'])))
        f.write('Inprogress cases: {}\n'.format(
            len([n for n in cases if n['status'] == 'inprogress'])))
        f.write('Fail cases: {}\n'.format(
            len([n for n in cases if n['status'] == 'fail'])))
        f.write('Error cases: {}\n'.format(
            len([n for n in cases if n['status'] == 'error'])))
        f.write('Done cases: {}\n'.format(
            len([n for n in cases if n['status'] == 'done'])))
        f.write('Skipped cases: {}\n\n'.format(
            len([n for n in cases if n['status'] == 'skipped'])))

        f.write('''\tPossible case statuses:\nActive: Case will be executed.
Inprogress: Case is in progress (if blender was crashed, case will be inprogress).
Fail: Blender was crashed during case. Fail report will be created.
Error: Blender was crashed during case. Fail report is already created.
Done: Case was finished successfully.
Skipped: Case will be skipped. Skip report will be created.\n
Case\t\tStatus\tTime\tTries
\n''')

        total_time = 0

        for case in cases:
            case_time = case_time = '{:.2f}'.format(case.get("time_taken", 0))
            f.write(
                '{}\t{}\t{}\t{}\n'.format(case['case'], case['status'], case_time, case.get('number_of_tries', 1)))
            total_time += float(case.get('time_taken', '0'))

        f.write(
            'Time taken: ' + str(datetime.datetime.utcfromtimestamp(total_time).strftime('%H:%M:%S')))

        f.write(logs)


if __name__ == '__main__':
    args = createArgsParser().parse_args()
    main(args)
