Required Python libraries for people counting
this works by Combining object detection and object tracking
In order to build our people counting applications, we’ll need a number of different Python libraries, including:


NumPy
OpenCV
dlib
imutils

for dlib you need to install cmake 

Im using windows 10
if you are facing problem with dlib install 

Windows Dlib > 19.7.0
Download the CMake installer and install it: https://cmake.org/download/
Add CMake executable path to the Enviroment Variables:

set PATH="%PATH%;C:\Program Files\CMake\bin"
note: The path of the executable could be different from C:\Program Files\CMake\bin, just set the PATH accordingly.

note: The path will be set temporarily, to make the change permanent you have to set it in the “Advanced system settings” → “Environment Variables” tab.

Restart The Cmd or PowerShell window for changes to take effect.

Step 1:
Install windows cmake.msi and configure environment variable
Step 2:
Create a conda environment, and install cmake using the below command.
pip install cmake
Step 3:
conda install -c conda-forge dlib

also install conda install -c conda-forge imutils 


We’ll then use dlib for its implementation of correlation filters. We could use OpenCV here as well; however, the dlib object tracking implementation was a bit easier to work with for this project.