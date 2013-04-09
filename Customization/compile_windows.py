"""
This script compiles the customization interface into an EXE.

Code adapted from:
http://arstechnica.com/information-technology/2009/03/
	how-to-deploying-pyqt-applications-on-windows-and-mac-os-x/

Copyright (c) 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.
"""

from distutils.core import setup
import py2exe

setup(name="customization",
      version="0.1",
      author="Jake Brand, Nick Klose, Richard Leung, Andrew Neufeld, and Anthony Sopkow",
      author_email="nick.klose@ualberta.ca",
      url="https://github.com/nklose/CMPUT302",
      license="GNU General Public License (GPL)",
      packages=['liftr'],
      package_data={"liftr": ["ui/*"]},
      scripts=["bin/liftr"],
      windows=[{"script": "bin/liftr"}],
      options={"py2exe": {"skip_archive": True, "includes": ["sip"]}})