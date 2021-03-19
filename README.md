# tokenAnalysis
This python program (tokenAnalysis) analyses tokens from text files in a given dataset.

==========DESCRIPTION=============

This python program (tokenAnalysis) analyses tokens from text files in a given dataset.

Inputs to the token analysis program: 
1. Path to the dataset directory containing text files. (e.g "C:\Dataset")

Output of the token analysis program:
1. A text file containing the token analysis, which is "out_tokenAnalysis.txt". This file is output in the same directory as the input dataset.

==========ENVIRONMENT SET-UP=============
1. Download this indexing package (tokenAnalysis) from GitHub (easy as a zip file). Save and unzip it in a preferred directory in your machine (e.g "C:\Test\tokenAnalysis")
Note: An example dataset is available in the package as "ExampleDataset.zip" for use.
2. Install Python 3.8.0 or above from https://www.python.org/downloads/.


==========HOW TO RUN THE PROGRAM=============
1. Launch the command line. 
E.g For Windows, press Window Key + R on keyboard and then type 'cmd'

2. Locate the path of python executable in your machine. 
E.g. For Windows, it's usually located at "C:\Users\YourUserId\AppData\Local\Programs\Python\Python38-32". Replace "YourUserId" with your actual Windows user Id.

3. Change current directory in the command line to the python path above.
E.g For Windows, "cd C:\Users\YourUserId\AppData\Local\Programs\Python\Python38-32"

4. Get the path of the token analysis program (tokenAnalyser.py) in your machine.
E.g "C:\Test\tokenAnalysis\tokenAnalyser.py"

5. Excecute the token analysis program in the command line using data from 4.
E.g "python C:\Test\tokenAnalysis\tokenAnalyser.py"

6. The the program will prompt for the path to input dataset directory. Key in the path and press Enter.
E.g "C:\Test\tokenAnalysis\HillaryEmails"

7. Wait for some time until the program ends. The program will respond on the command line when it ends. It could take up to a few seconds.

8. Find the program output file which contains the analysis data and is under the same directory as the input dataset.
E.g "C:\Test\tokenAnalysis\HillaryEmails\out_tokenAnalysis.txt"
