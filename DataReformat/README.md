Sifteos for Dyslexia
====================
CMPUT 302 Project 8: "Sifteo Games for Dyslexia" for Suzanne Sauvé.

Copyright © 2013 Jake Brand, Nick Klose, Richard Leung, 
Andrew Neufeld, and Anthony Sopkow.

The Sifteos for Dyslexia project has the goal of creating games for Sifteo cubes which will help children with dyslexia learn to discern between different audible and visual phonemes.

Required Packages For Use
=================
1. Python 2.7. Python is Copyright © 1990-2013, Python Software Foundation
2. PyQt4. PyQT is Copyright © 2013, Riverbank Computing Limited. Riverbank Computing Limited is a company registered in England and Wales with company number 4314904.

Additionally, to compile the interfaces to an EXE file for Windows, the following is required:

3. Py2exe. Py2exe was developed by Thomas Heller, Jimmy Retzlaff, and Mark Hammond.http://www.py2exe.org/

Details
=======
Course:		CMPUT 302
Semester:	Winter 2013
Institution: 	University of Alberta
Instructor:	Walter Bischof

Compatibility
=============
## Compiling from Source
### evaluation.py
In general, a system with the required packages can run the evaluation interface with the following command while in the Evaluation directory:

`python evaluation.py`

### customization.py
In general, a system with the required packages can run the customization interface with the following command while in the Customization directory:

`python customization.py`

Alternatively, to run the program in debug mode (which prints verbose output to the console), use this command:

`python customization.py debug`

### setup_win.py
This file must be run on a Windows machine with py2exe installed. It may need to be modified to suit the specific system it's being run on. It can be run with:

`python setup_win.py py2exe`

This applies to both the evaluation and customization versions of the setup script.

## Running on Windows
The evaluation interface can be run on Windows by opening `Evaluation/evaluation.exe`.

The customization interface can be run on Windows by opening `Customization/customization.exe`.

License
=======

	CMPUT 302 Project 8: "Sifteo Games for Dyslexia" for Suzanne Sauvé.

	Copyright © 2013 Jake Brand, Nick Klose, Richard Leung, 
					  Andrew Neufeld, and Anthony Sopkow.

	The Sifteos for Dyslexia project has the goal of creating games for 
	Sifteo cubes which will help children with dyslexia learn to discern 
	between different audible and visual phonemes.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	http://www.gnu.org/copyleft/gpl.html