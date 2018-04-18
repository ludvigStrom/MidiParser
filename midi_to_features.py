# By Ludvig Ström 2018
# The goal of the class is to extract normalized feautures of a midifile to a csv-file.
# the features of the file is file name, length, silence, intensity(no of notes/min), note distrubution, scale distrubution.
# This class is an extension of mxm.MidiEvents

# NOTE ON NOTE/SCALE DISTRUBUTION
# * Note distrubution is the number of notes regardless of octave eg. numbers of C's in the file, C#'s of the file and so forth.
# * Scale distrubtion is the number of notes normalized numbers of midi note 64 on's, no. of midi note 65 on's and so forth. 

# MidiToFeatures
import os, os.path, random
from mxm.midifile.src import constants as c
from mxm.midifile.src.midi_events import MidiEvents

class MidiToFeatures(MidiEvents):
    
    def __init__(self, name, inDir):
        self.inDir = inDir
        self.labels = 'name:drink:intensity:C:C#:D:D#:E:F:F#:G:G#:A:A#:B'
        self.name = name
        self.drink = 'drinkyNamy'
        self.intensity = 0
        self.cNote = 0
        self.cSharpNote = 0 
        self.dNote = 0 
        self.dSharpNote = 0 
        self.eNote = 0
        self.fNote = 0
        self.fSharpNote = 0
        self.gNote = 0
        self.gSharpNote = 0 
        self.aNote = 0
        self.aSharpNote = 0
        self.bNote = 0
        self.noteOns = 0
        self.midiNotes = [0] * 128
        self.highestValueMidiNotes = 0
        self.highestValueScale = 0
        self.intensityLimit = 1024
    
    def _time(self):
        if not hasattr(self, '_old_time'):
            self._old_time = 0

    def _pt(self):
        "prints time"
        st = 'midi_out.update_time(new_time=%s)' % self.rel_time()
        print (st)

    def addMidiToFeatures(self, midi):
        self.midiNotes[midi] += 1

        croot = 0
        csharp = 1
        droot = 2
        dsharp = 3
        eroot = 4
        froot = 5
        fsharp = 6
        groot = 7
        gsharp = 8
        aroot = 9
        asharp = 10
        broot = 11

        if (midi == croot) or (midi == (croot + 12)) or (midi == (croot + 24)) or (midi == (croot + 36)) or (midi == (croot + 48)) or (midi == (croot + 60)) or (midi == (croot + 72)) or (midi == (croot + 84)) or (midi == (croot + 96)) or (midi == (croot + 108)) or (midi == (croot + 120)) or (midi == (croot + 134)):
            #print ('C ')
            self.cNote = self.cNote + 1
        elif (midi == csharp) or (midi == (csharp + 12)) or (midi == (csharp + 24)) or (midi == (csharp + 36)) or (midi == (csharp + 48)) or (midi == (csharp + 60)) or (midi == (csharp + 72)) or (midi == (csharp + 84)) or (midi == (csharp + 96)) or (midi == (csharp + 108)) or (midi == (csharp + 120)):
            #print ('C# ')
            self.cSharpNote = self.cSharpNote + 1
        elif (midi == droot) or (midi == (droot + 12)) or (midi == (droot + 24)) or (midi == (droot + 36)) or (midi == (droot + 48)) or (midi == (droot + 60)) or (midi == (droot + 72)) or (midi == (droot + 84)) or (midi == (droot + 96)) or (midi == (droot + 108)) or (midi == (droot + 120)):
            #print ('D ')
            self.dNote = self.dNote + 1
        elif (midi == dsharp) or (midi == (dsharp + 12)) or (midi == (dsharp + 24)) or (midi == (dsharp + 36)) or (midi == (dsharp + 48)) or (midi == (dsharp + 60)) or (midi == (dsharp + 72)) or (midi == (dsharp + 84)) or (midi == (dsharp + 96)) or (midi == (dsharp + 108)) or (midi == (dsharp + 120)):
            #print ('D# ')
            self.dSharpNote = self.dSharpNote + 1
        elif (midi == eroot) or (midi == (eroot + 12)) or (midi == (eroot + 24)) or (midi == (eroot + 36)) or (midi == (eroot + 48)) or (midi == (eroot + 60)) or (midi == (eroot + 72)) or (midi == (eroot + 84)) or (midi == (eroot + 96)) or (midi == (eroot + 108)) or (midi == (eroot + 120)):
            #print ('E ')
            self.eNote = self.eNote + 1
        elif (midi == froot) or (midi == (froot + 12)) or (midi == (froot + 24)) or (midi == (froot + 36)) or (midi == (froot + 48)) or (midi == (froot + 60)) or (midi == (froot + 72)) or (midi == (froot + 84)) or (midi == (froot + 96)) or (midi == (froot + 108)) or (midi == (froot + 120)):
            #print ('F ')
            self.fNote = self.fNote + 1
        elif (midi == fsharp) or (midi == (fsharp + 12)) or (midi == (fsharp + 24)) or (midi == (fsharp + 36)) or (midi == (fsharp + 48)) or (midi == (fsharp + 60)) or (midi == (fsharp + 72)) or (midi == (fsharp + 84)) or (midi == (fsharp + 96)) or (midi == (fsharp + 108)) or (midi == (fsharp + 120)):
            #print ('F# ')
            self.fSharpNote = self.fSharpNote + 1
        elif (midi == groot) or (midi == (groot + 12)) or (midi == (groot + 24)) or (midi == (groot + 36)) or (midi == (groot + 48)) or (midi == (groot + 60)) or (midi == (groot + 72)) or (midi == (groot + 84)) or (midi == (groot + 96)) or (midi == (groot + 108)) or (midi == (groot + 120)):
            #print ('G ')
            self.gNote = self.gNote + 1
        elif (midi == gsharp) or (midi == (gsharp + 12)) or (midi == (gsharp + 24)) or (midi == (gsharp + 36)) or (midi == (gsharp + 48)) or (midi == (gsharp + 60)) or (midi == (gsharp + 72)) or (midi == (gsharp + 84)) or (midi == (gsharp + 96)) or (midi == (gsharp + 108)) or (midi == (gsharp + 120)):
            #print ('G# ')
            self.gSharpNote = self.gSharpNote + 1
        elif (midi == aroot) or (midi == (aroot + 12)) or (midi == (aroot + 24)) or (midi == (aroot + 36)) or (midi == (aroot + 48)) or (midi == (aroot + 60)) or (midi == (aroot + 72)) or (midi == (aroot + 84)) or (midi == (aroot + 96)) or (midi == (aroot + 108)) or (midi == (aroot + 120)):
            #print ('A ')
            self.aNote = self.aNote + 1
        elif (midi == asharp) or (midi == (asharp + 12)) or (midi == (asharp + 24)) or (midi == (asharp + 36)) or (midi == (asharp + 48)) or (midi == (asharp + 60)) or (midi == (asharp + 72)) or (midi == (asharp + 84)) or (midi == (asharp + 96)) or (midi == (asharp + 108)) or (midi == (asharp + 120)):
            #print ('A# ')
            self.aSharpNote = self.aSharpNote + 1
        elif (midi == broot) or (midi == (broot + 12)) or (midi == (broot + 24)) or (midi == (broot + 36)) or (midi == (broot + 48)) or (midi == (broot + 60)) or (midi == (broot + 72)) or (midi == (broot + 84)) or (midi == (broot + 96)) or (midi == (broot + 108)) or (midi == (broot + 120)):
            #print ('B ')
            self.bNote = self.bNote + 1

        self.noteOns = self.noteOns + 1

    def note_on(self, channel=0, note=0x40, velocity=0x40, use_running_status=False):
        #send note to addMidiToFeatures if note is ON and not belongs to channel 10 (drums)
        if velocity >= 1 and channel is not 10:
            self.addMidiToFeatures(note)                                                                                               

    def normalize_value(self, val, minimum, maximum):
        rtn_val = (val-minimum)/(maximum-minimum)
        return rtn_val

    def findHighestVal(self, pyList):
        highestVal = 0
        for member in pyList:
            if(member > highestVal):
                highestVal = member
        return highestVal

    def normalizeAllValuesInList(self, pylist, minVal, maxVal):
        i = 0
        for member in pylist:
            pylist[i] = self.normalize_value(member, minVal, maxVal)
            i += 1
        return pylist
    
    #This method is called when you reach the end of the midi file
    def eof(self):
        print ('Parsing ' + self.name)

        #Normalize all values in midinotes
        self.midiNotes = self.normalizeAllValuesInList(self.midiNotes, 0, self.findHighestVal(self.midiNotes))

        #Add all values to vector
        scaleNotes = [self.cNote, self.cSharpNote, self.dNote, self.dSharpNote, self.eNote, self.fNote, self.fSharpNote, self.gNote, self.gSharpNote, self.aNote, self.aSharpNote, self.bNote]
        #Normalize values in scale
        scaleNotes = self.normalizeAllValuesInList(scaleNotes, 0, self.findHighestVal(scaleNotes))
        
        #Calculate intensity
        if(self.noteOns > self.intensityLimit):
            self.noteOns = self.intensityLimit;
        self.intensity = self.normalize_value(self.noteOns, 0, self.intensityLimit)

        #WRITE TO FILE!       
        os.chdir(self.inDir) #change to output dir
        
        if not os.path.isfile('midiFeatures.csv'): #if not create file, write labels, and keep it open in append mode
            f = open('midiFeatures.csv', 'a')
            #write label in header
            f.write(self.labels)

            #write all the midi notes in header
            i = 0
            for member in self.midiNotes:
                f.write(':' + str(i))
                i += 1

        else: #else open file in append mode
            f = open('midiFeatures.csv', 'a')

        #write to file
        f.write('\n'
                + self.name
                + ':'
                + self.drink
                + ':'
                + str(self.intensity)
                + ':'
                )
        #write scaleNotes to file
        for member in scaleNotes:
            f.write(str(member) + ':')

        #write all midiNotes to file
        for member in self.midiNotes:
            f.write(str(member) + ':')
        f.close()
        print('done')

if __name__ == '__main__':

    import doctest
    doctest.testmod() # run test on inline examples first

    # # https://www.reddit.com/r/WeAreTheMusicMakers/comments/3ajwe4/the_largest_midi_collection_on_the_internet/
    
    # test_file = '/home/maxm/instances/midienv/mxm.midifile-1.0/mxm/midifile/tests/midifiles/ableton-glissando.mid'
    
    # with open(test_file, 'rb') as f:
    #     # do parsing
    #     from midi_infile import MidiInFile
    #     midiIn = MidiInFile(MidiToCode(), f)
    #     midiIn.read()

