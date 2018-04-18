"""
This is an example of how to use MidiToFeatures, a script that parse midi files characteristica to a file
for use in machinelearning.

Place midi files in the directory defined in this code and run the script. A .csv file will be generated in that directory
"""

import os
from mxm.midifile import MidiInFile
from mxm.midifile import MidiToFeatures

os.chdir("F:\\midi_programming\\testOutput")

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".mid"):
        midiFeatures = MidiInFile(MidiToFeatures(str(filename), os.getcwd()), filename)
        midiFeatures.read()

print ("")
