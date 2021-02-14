Required Python libraries for people counting  
This peoject is combination of object detection and object tracking.  Check other banches 
- [Centroid](https://github.com/yeasin50/Social_Distance/tree/Centroid)
- [People Counter](https://github.com/yeasin50/Social_Distance/tree/peopleCounter) 
- [Main](https://github.com/yeasin50/Social_Distance/tree/main)


In order to build our people counting applications, we’ll need a number of different Python libraries, including:

- NumPy
- OpenCV
- dlib
- imutils
 
----
For dlib you need to install cmake 

Im using windows 10  >>   
  if you are facing problem with dlib install 

* Download the CMake installer and install it: https://cmake.org/download/
- Add CMake executable path to the Enviroment Variables:

- set PATH="%PATH%;C:\Program Files\CMake\bin"  
note: The path of the executable could be different from C:\Program Files\CMake\bin, just set the PATH accordingly.

note: The path will be set temporarily, to make the change permanent you have to set it in the “Advanced system settings” → “Environment Variables” tab.

Restart The Cmd or PowerShell window for changes to take effect.  

----
### Easy way to get this 
- Step 1:
Install windows cmake.msi and configure environment variable
- Step 2:
Create a conda environment, and install cmake using the below command.
pip install cmake
- Step 3:
conda install -c conda-forge dlib

also install conda install -c conda-forge imutils 

### Feel free to use pip

-----
We’ll then use dlib for its implementation of correlation filters. We could use OpenCV here as well; however, the dlib object tracking implementation was a bit easier to work with for this project.

THanks https://www.pyimagesearch.com/ & The Sparks Foundation