from pathlib import Path

ROOT_PATH = Path.cwd()
INPUT_DIR = ROOT_PATH.joinpath('input')
OUTPUT_DIR = ROOT_PATH.joinpath('output')
INPUT_FILE = INPUT_DIR.joinpath('ALL.xlsx')
OUTPUT_FILE = OUTPUT_DIR.joinpath('output.csv')
