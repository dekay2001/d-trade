import os
import shutil
import sys

import bolt

import dtrade.about as about

bolt.register_task('default', ['validate'])
bolt.register_task('validate', ['pip', 'ut', 'ft'])

bolt.register_task('ut', [
    'clear-pyc',
    'shell.pytest'
])
bolt.register_task('ct', ['conttest'])
bolt.register_task('clear-pyc', ['delete-pyc', 'delete-pyc.from-tests'])
bolt.register_task('clear-last-build', ['delete-files.last-build'])

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(PROJECT_ROOT, 'dtrade')
TESTS_DIR = os.path.join(PROJECT_ROOT, 'tests')

OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
OUTPUT_UNIT_DIR = os.path.join(OUTPUT_DIR, 'unit')
OUTPUT_UNIT_RESULTS_DIR = os.path.join(OUTPUT_UNIT_DIR, 'results')
OUTPUT_UNIT_COVERAGE_DIR = os.path.join(OUTPUT_UNIT_DIR, 'coverage')

config = {
    'delete-pyc': {
        'sourcedir': SRC_DIR,
        'recursive': True,
        'from-tests': {
            'sourcedir': TESTS_DIR
        }
    },
    'conttest': {
        'task': 'ut',
        'directory': PROJECT_ROOT,
    },
    'shell': {
        'pytest': {
            'command': sys.executable,
            'arguments': [
                '-m', 'pytest',
                # '--durations=50',   # Shows top 50 slowest unit tests
                TESTS_DIR
            ],
            'coverage': {
                'arguments': [
                    '-m', 'pytest',
                    f'--cov={about.package}',
                    '--cov-report',
                    f'html:{OUTPUT_UNIT_COVERAGE_DIR}',
                    TESTS_DIR,
                ]
            }
        }
    },
}