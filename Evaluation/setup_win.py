"""
This script compiles the evaluation interface into an exe file
using py2exe. To run it, call python setup.py py2exe. Note that 
you will need to have Python 2.7 (x32) and PyQt4 (x32 Python 2.7).
"""
from distutils.core import setup
import py2exe, os, sys

root_dir = os.path.dirname(os.path.realpath(__file__))
main_file = os.path.join(root_dir, "evaluation.py")
exe_name = "Evaluation"
images = [os.path.join(root_dir, "minus.png"),
                os.path.join(root_dir, "plus.png")]
incl_files = images
excl_dlls = ["libiomp5md.dll", "MSVCP60.DLL", "MSVCP90.DLL", "MSVCP100.DLL"]
windowsSettings = [{"dest_base": exe_name, "script": main_file}]
incl_packages = ["sip"]


options = {
    'py2exe': {
        "dist_dir": "bin",
        "includes": incl_packages,
        "dll_excludes": excl_dlls,
        'bundle_files': 1,
        'compressed': 2,
        'optimize': 2, 
        'xref': False,
        'skip_archive': False,
        'ascii': False,
    }
}

setup(
    windows = windowsSettings,
    author = "CMPUT 302 - Team 8",
    version = "1.0",
    description = "Sifteos for Dyslexia - EvaluationInterface",
    name = "Evaluation Interface",
    options = options,
    data_files = incl_files,
    zipfile = None
)
