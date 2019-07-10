#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on July 09, 2019, at 18:57
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'popout_cindy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\GitHub\\Behavior-popout-attention\\popout_diamond_circle_red_green\\popout_cindy_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2048, 1152], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
Cindy_num_blocks_finished = 0

MyExps = data.TrialHandler(nReps=1, method='random', 
                           extraInfo=expInfo, originPath=-1,
                           trialList=data.importConditions('tExp.csv'),
                           seed=None, name='MyExps')
thisExp.addLoop(MyExps)  # add the loop to the experiment
thisMyExp = MyExps.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMyExp.rgb)
if thisMyExp != None:
  for paramName in thisMyExp:
    exec('{} = thisMyExp[paramName]'.format(paramName))
tInstr = visual.TextStim(win=win, name='tInstr',
    text=tInstr_text,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
iTrial = visual.ImageStim(
    win=win,
    name='iTrial', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
tTrial = visual.TextStim(win=win, name='tTrial',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
pTrial = visual.ImageStim(
    win=win,
    name='pTrial', units='height', 
    image='fixation.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
tPause = visual.TextStim(win=win, name='tPause',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
tEnd = visual.TextStim(win=win, name='tEnd',
    text=tEnd_text,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
kInstr = keyboard.Keyboard()
# keep track of which components have finished
instrComponents = [tInstr, kInstr]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tInstr* updates
    if t >= 0.0 and tInstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        tInstr.tStart = t  # not accounting for scr refresh
        tInstr.frameNStart = frameN  # exact frame index
        win.timeOnFlip(tInstr, 'tStartRefresh')  # time at next scr refresh
        tInstr.setAutoDraw(True)
    
    # *kInstr* updates
    if t >= 0.0 and kInstr.status == NOT_STARTED:
        # keep track of start time/frame for later
        kInstr.tStart = t  # not accounting for scr refresh
        kInstr.frameNStart = frameN  # exact frame index
        win.timeOnFlip(kInstr, 'tStartRefresh')  # time at next scr refresh
        kInstr.status = STARTED
        # keyboard checking is just starting
        kInstr.clearEvents(eventType='keyboard')
    if kInstr.status == STARTED:
        theseKeys = kInstr.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tInstr.started', tInstr.tStartRefresh)
thisExp.addData('tInstr.stopped', tInstr.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=blocks_nReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tAll_blocks.csv'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=trials_nReps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(cur_block_file_name),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        kTrial = keyboard.Keyboard()
        iTrial.setSize((iTrial_size, iTrial_size))
        iTrial.setImage(linux_file_name)
        # keep track of which components have finished
        trialComponents = [kTrial, iTrial, tTrial, pTrial]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *kTrial* updates
            if t >= 0 and kTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                kTrial.tStart = t  # not accounting for scr refresh
                kTrial.frameNStart = frameN  # exact frame index
                win.timeOnFlip(kTrial, 'tStartRefresh')  # time at next scr refresh
                kTrial.status = STARTED
                # AllowedKeys looks like a variable named `kTrial_allowed_keys`
                if not type(kTrial_allowed_keys) in [list, tuple, np.ndarray]:
                    if not isinstance(kTrial_allowed_keys, str):
                        logging.error('AllowedKeys variable `kTrial_allowed_keys` is not string- or list-like.')
                        core.quit()
                    elif not ',' in kTrial_allowed_keys:
                        kTrial_allowed_keys = (kTrial_allowed_keys,)
                    else:
                        kTrial_allowed_keys = eval(kTrial_allowed_keys)
                # keyboard checking is just starting
                win.callOnFlip(kTrial.clock.reset)  # t=0 on next screen flip
                kTrial.clearEvents(eventType='keyboard')
            frameRemains = 0 + kTrial_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if kTrial.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                kTrial.tStop = t  # not accounting for scr refresh
                kTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(kTrial, 'tStopRefresh')  # time at next scr refresh
                kTrial.status = FINISHED
            if kTrial.status == STARTED:
                theseKeys = kTrial.getKeys(keyList=list(kTrial_allowed_keys), waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    kTrial.keys = theseKeys.name  # just the last key pressed
                    kTrial.rt = theseKeys.rt
                    # was this 'correct'?
                    if (kTrial.keys == str(correct_response)) or (kTrial.keys == correct_response):
                        kTrial.corr = 1
                    else:
                        kTrial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *iTrial* updates
            if t >= pTrial_duration and iTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                iTrial.tStart = t  # not accounting for scr refresh
                iTrial.frameNStart = frameN  # exact frame index
                win.timeOnFlip(iTrial, 'tStartRefresh')  # time at next scr refresh
                iTrial.setAutoDraw(True)
            frameRemains = pTrial_duration + iTrial_duration + pTrial_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if iTrial.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                iTrial.tStop = t  # not accounting for scr refresh
                iTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iTrial, 'tStopRefresh')  # time at next scr refresh
                iTrial.setAutoDraw(False)
            
            # *tTrial* updates
            if t >= pTrial_duration and tTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                tTrial.tStart = t  # not accounting for scr refresh
                tTrial.frameNStart = frameN  # exact frame index
                win.timeOnFlip(tTrial, 'tStartRefresh')  # time at next scr refresh
                tTrial.setAutoDraw(True)
            frameRemains = pTrial_duration + pTrial_duration + tTrial_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if tTrial.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                tTrial.tStop = t  # not accounting for scr refresh
                tTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tTrial, 'tStopRefresh')  # time at next scr refresh
                tTrial.setAutoDraw(False)
            
            # *pTrial* updates
            if t >= 0.0 and pTrial.status == NOT_STARTED:
                # keep track of start time/frame for later
                pTrial.tStart = t  # not accounting for scr refresh
                pTrial.frameNStart = frameN  # exact frame index
                win.timeOnFlip(pTrial, 'tStartRefresh')  # time at next scr refresh
                pTrial.setAutoDraw(True)
            frameRemains = 0.0 + pTrial_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if pTrial.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                pTrial.tStop = t  # not accounting for scr refresh
                pTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pTrial, 'tStopRefresh')  # time at next scr refresh
                pTrial.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if kTrial.keys in ['', [], None]:  # No response was made
            kTrial.keys = None
            # was no response the correct answer?!
            if str(correct_response).lower() == 'none':
               kTrial.corr = 1;  # correct non-response
            else:
               kTrial.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('kTrial.keys',kTrial.keys)
        trials.addData('kTrial.corr', kTrial.corr)
        if kTrial.keys != None:  # we had a response
            trials.addData('kTrial.rt', kTrial.rt)
        trials.addData('kTrial.started', kTrial.tStartRefresh)
        trials.addData('kTrial.stopped', kTrial.tStopRefresh)
        trials.addData('iTrial.started', iTrial.tStartRefresh)
        trials.addData('iTrial.stopped', iTrial.tStopRefresh)
        trials.addData('tTrial.started', tTrial.tStartRefresh)
        trials.addData('tTrial.stopped', tTrial.tStopRefresh)
        trials.addData('pTrial.started', pTrial.tStartRefresh)
        trials.addData('pTrial.stopped', pTrial.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed trials_nReps repeats of 'trials'
    
    
    # ------Prepare to start Routine "pause"-------
    t = 0
    pauseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Cindy_num_blocks_finished += 1
    tPausse_text_final = tPause_text +'\n Number of blocks completed: ' + str(Cindy_num_blocks_finished) + '\n Number of blocks remaining:  ' + str(int(my_num_of_blocks - Cindy_num_blocks_finished))
    
    
    tPause.setText(tPausse_text_final)
    kPause = keyboard.Keyboard()
    # keep track of which components have finished
    pauseComponents = [tPause, kPause]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pause"-------
    while continueRoutine:
        # get current time
        t = pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tPause* updates
        if t >= 0.0 and tPause.status == NOT_STARTED:
            # keep track of start time/frame for later
            tPause.tStart = t  # not accounting for scr refresh
            tPause.frameNStart = frameN  # exact frame index
            win.timeOnFlip(tPause, 'tStartRefresh')  # time at next scr refresh
            tPause.setAutoDraw(True)
        
        # *kPause* updates
        if t >= 0.0 and kPause.status == NOT_STARTED:
            # keep track of start time/frame for later
            kPause.tStart = t  # not accounting for scr refresh
            kPause.frameNStart = frameN  # exact frame index
            win.timeOnFlip(kPause, 'tStartRefresh')  # time at next scr refresh
            kPause.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(kPause.clock.reset)  # t=0 on next screen flip
            kPause.clearEvents(eventType='keyboard')
        if kPause.status == STARTED:
            theseKeys = kPause.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                kPause.keys = theseKeys.name  # just the last key pressed
                kPause.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('tPause.started', tPause.tStartRefresh)
    blocks.addData('tPause.stopped', tPause.tStopRefresh)
    # check responses
    if kPause.keys in ['', [], None]:  # No response was made
        kPause.keys = None
    blocks.addData('kPause.keys',kPause.keys)
    if kPause.keys != None:  # we had a response
        blocks.addData('kPause.rt', kPause.rt)
    blocks.addData('kPause.started', kPause.tStartRefresh)
    blocks.addData('kPause.stopped', kPause.tStopRefresh)
    # the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed blocks_nReps repeats of 'blocks'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
kEnd = keyboard.Keyboard()
# keep track of which components have finished
endComponents = [tEnd, kEnd]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tEnd* updates
    if t >= 0.0 and tEnd.status == NOT_STARTED:
        # keep track of start time/frame for later
        tEnd.tStart = t  # not accounting for scr refresh
        tEnd.frameNStart = frameN  # exact frame index
        win.timeOnFlip(tEnd, 'tStartRefresh')  # time at next scr refresh
        tEnd.setAutoDraw(True)
    
    # *kEnd* updates
    if t >= 0.0 and kEnd.status == NOT_STARTED:
        # keep track of start time/frame for later
        kEnd.tStart = t  # not accounting for scr refresh
        kEnd.frameNStart = frameN  # exact frame index
        win.timeOnFlip(kEnd, 'tStartRefresh')  # time at next scr refresh
        kEnd.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(kEnd.clock.reset)  # t=0 on next screen flip
        kEnd.clearEvents(eventType='keyboard')
    if kEnd.status == STARTED:
        theseKeys = kEnd.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            kEnd.keys = theseKeys.name  # just the last key pressed
            kEnd.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tEnd.started', tEnd.tStartRefresh)
thisExp.addData('tEnd.stopped', tEnd.tStopRefresh)
# check responses
if kEnd.keys in ['', [], None]:  # No response was made
    kEnd.keys = None
thisExp.addData('kEnd.keys',kEnd.keys)
if kEnd.keys != None:  # we had a response
    thisExp.addData('kEnd.rt', kEnd.rt)
thisExp.addData('kEnd.started', kEnd.tStartRefresh)
thisExp.addData('kEnd.stopped', kEnd.tStopRefresh)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
