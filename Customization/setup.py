"""
This script compiles the customization interface into an exe file
using py2exe. To run it, call python setup.py py2exe. Note that 
you will need to have Python 2.7 (x32) and PyQt4 (x32 Python 2.7).
"""
from distutils.core import setup
import py2exe, os, sys

root_dir = os.path.dirname(os.path.realpath(__file__))
main_file = os.path.join(ROOT, "customization.py")
exe_name = "Customization"
incl_files = [os.path.join(ROOT_PATH, "plus.png"), os.path.join(ROOT_PATH, "minus.png")]
excl_files = ["_gtkagg", "_tkagg"]
excl_dlls = ["libiomp5md.dll", "MSVCP60.DLL", "MSVCP90.DLL", "MSVCP100.DLL"]
windowsSettings = [{"dest_base": EXE_FILE, "script": MAIN_FILE}]
incl_packages = ["sip"]


options = {
    'py2exe': {
        "dist_dir": "bin",
        "includes": incl_packages,
        "excludes": excl_files,
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
    description = "Sifteos for Dyslexia - Customization Interface",
    name = "Customization Interface",
    options = options,
    data_files = incl_files,
    zipfile = None
)
