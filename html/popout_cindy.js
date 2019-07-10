/*********************
 * Popout_Cindy Test *
 *********************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'popout_cindy';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp

var Cindy_num_blocks_finished = 0;

const MyExpLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(MyExpLoopBegin, MyExpLoopScheduler);
flowScheduler.add(MyExpLoopScheduler);
flowScheduler.add(MyExpLoopEnd);

flowScheduler.add(experimentInit);
flowScheduler.add(instrRoutineBegin);
flowScheduler.add(instrRoutineEachFrame);
flowScheduler.add(instrRoutineEnd);
const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin, blocksLoopScheduler);
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);
flowScheduler.add(endRoutineBegin);
flowScheduler.add(endRoutineEachFrame);
flowScheduler.add(endRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var MyExp;
var currentLoop;
function MyExpLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  MyExp = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'tExp.csv',
    seed: undefined, name: 'MyExp'
  });
  psychoJS.experiment.addLoop(MyExp); // add the loop to the experiment
  currentLoop = MyExp;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisMyExp of MyExp) {
    thisScheduler.add(importConditions(MyExp));
  }

  return Scheduler.Event.NEXT;
}


function MyExpLoopEnd() {
  psychoJS.experiment.removeLoop(MyExp);

  return Scheduler.Event.NEXT;
}


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.1.2';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);

  return Scheduler.Event.NEXT;
}

var instrClock;
var tInstr;
var trialClock;
var iTrial;
var tTrial;
var pTrial;
var pauseClock;
var tPause;
var endClock;
var tEnd;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  tInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'tInstr',
    text: tInstr_text,
    font: 'Arial',
    units : undefined,
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0
  });

  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  iTrial = new visual.ImageStim({
    win : psychoJS.window,
    name : 'iTrial', units : 'height',
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0
  });
  tTrial = new visual.TextStim({
    win: psychoJS.window,
    name: 'tTrial',
    text: '',
    font: 'Arial',
    units : undefined,
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0
  });

  pTrial = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pTrial', units : 'height',
    image : 'fixation.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0
  });
  // Initialize components for Routine "pause"
  pauseClock = new util.Clock();
  tPause = new visual.TextStim({
    win: psychoJS.window,
    name: 'tPause',
    text: 'default text',
    font: 'Arial',
    units : undefined,
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0
  });

  // Initialize components for Routine "end"
  endClock = new util.Clock();
  tEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'tEnd',
    text: tEnd_text,
    font: 'Arial',
    units : undefined,
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0
  });

  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine

  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var kInstr;
var instrComponents;
function instrRoutineBegin() {
  //------Prepare to start Routine 'instr'-------
  t = 0;
  instrClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  kInstr = new core.BuilderKeyResponse(psychoJS);

  // keep track of which components have finished
  instrComponents = [];
  instrComponents.push(tInstr);
  instrComponents.push(kInstr);

  for (const thisComponent of instrComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;

  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instrRoutineEachFrame() {
  //------Loop for each frame of Routine 'instr'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instrClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame

  // *tInstr* updates
  if (t >= 0.0 && tInstr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    tInstr.tStart = t;  // (not accounting for frame time here)
    tInstr.frameNStart = frameN;  // exact frame index
    tInstr.setAutoDraw(true);
  }


  // *kInstr* updates
  if (t >= 0.0 && kInstr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    kInstr.tStart = t;  // (not accounting for frame time here)
    kInstr.frameNStart = frameN;  // exact frame index
    kInstr.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (kInstr.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys();

    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }

    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }

  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }

  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instrComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }

  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEnd() {
  //------Ending Routine 'instr'-------
  for (const thisComponent of instrComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instr" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();

  return Scheduler.Event.NEXT;
}

var blocks;
var currentLoop;
function blocksLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blocks = new TrialHandler({
    psychoJS: psychoJS,
    nReps: blocks_nReps, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'tAll_blocks.csv',
    seed: undefined, name: 'blocks'});
  psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
  currentLoop = blocks;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock of blocks) {
    thisScheduler.add(importConditions(blocks));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(pauseRoutineBegin);
    thisScheduler.add(pauseRoutineEachFrame);
    thisScheduler.add(pauseRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisBlock));
  }

  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: trials_nReps, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: cur_block_file_name,
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisTrial));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function blocksLoopEnd() {
  psychoJS.experiment.removeLoop(blocks);

  return Scheduler.Event.NEXT;
}

var kTrial;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  kTrial = new core.BuilderKeyResponse(psychoJS);

  iTrial.setSize([iTrial_size, iTrial_size]);
  iTrial.setImage(linux_file_name);
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(kTrial);
  trialComponents.push(iTrial);
  trialComponents.push(tTrial);
  trialComponents.push(pTrial);

  for (const thisComponent of trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;

  return Scheduler.Event.NEXT;
}

var frameRemains;
function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame

  // *kTrial* updates
  if (t >= 0 && kTrial.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    kTrial.tStart = t;  // (not accounting for frame time here)
    kTrial.frameNStart = frameN;  // exact frame index
    kTrial.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { kTrial.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0 + kTrial_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (kTrial.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    kTrial.status = PsychoJS.Status.FINISHED;
  }

  if (kTrial.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys();

    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }

    if (theseKeys.length > 0) {  // at least one key was pressed
      kTrial.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      kTrial.rt = kTrial.clock.getTime();
      // was this 'correct'?
      if (kTrial.keys == correct_response) {
          kTrial.corr = 1;
      } else {
          kTrial.corr = 0;
      }
      // a response ends the routine
      continueRoutine = false;
    }
  }


  // *iTrial* updates
  if (t >= pTrial_duration && iTrial.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    iTrial.tStart = t;  // (not accounting for frame time here)
    iTrial.frameNStart = frameN;  // exact frame index
    iTrial.setAutoDraw(true);
  }

  frameRemains = pTrial_duration + (iTrial_duration + pTrial_duration) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (iTrial.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    iTrial.setAutoDraw(false);
  }

  // *tTrial* updates
  if (t >= pTrial_duration && tTrial.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    tTrial.tStart = t;  // (not accounting for frame time here)
    tTrial.frameNStart = frameN;  // exact frame index
    tTrial.setAutoDraw(true);
  }

  frameRemains = pTrial_duration + (pTrial_duration + tTrial_duration) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (tTrial.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    tTrial.setAutoDraw(false);
  }

  // *pTrial* updates
  if (t >= 0.0 && pTrial.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pTrial.tStart = t;  // (not accounting for frame time here)
    pTrial.frameNStart = frameN;  // exact frame index
    pTrial.setAutoDraw(true);
  }

  frameRemains = 0.0 + pTrial_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (pTrial.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    pTrial.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }

  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }

  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }

  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  for (const thisComponent of trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }

  // check responses
  if (kTrial.keys === undefined || kTrial.keys.length === 0) {    // No response was made
      kTrial.keys = undefined;
  }

  // was no response the correct answer?!
  if (kTrial.keys === undefined) {
    if (['None','none',undefined].includes(correct_response)) {
       kTrial.corr = 1  // correct non-response
    } else {
       kTrial.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('kTrial.keys', kTrial.keys);
  psychoJS.experiment.addData('kTrial.corr', kTrial.corr);
  if (typeof kTrial.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('kTrial.rt', kTrial.rt);
      routineTimer.reset();
      }

  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();

  return Scheduler.Event.NEXT;
}

var kPause;
var pauseComponents;
var tPausse_text_final;
function pauseRoutineBegin() {
  //------Prepare to start Routine 'pause'-------
  t = 0;
  pauseClock.reset(); // clock
  frameN = -1;

  Cindy_num_blocks_finished += 1
  tPausse_text_final = tPause_text.concat('\n Number of blocks completed: ', Cindy_num_blocks_finished, '\n Number of blocks remaining:  ' + parseInt(my_num_of_blocks - Cindy_num_blocks_finished))
  // update component parameters for each repeat
  tPause.setText(tPausse_text_final);
  kPause = new core.BuilderKeyResponse(psychoJS);

  // keep track of which components have finished
  pauseComponents = [];
  pauseComponents.push(tPause);
  pauseComponents.push(kPause);

  for (const thisComponent of pauseComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;

  return Scheduler.Event.NEXT;
}


function pauseRoutineEachFrame() {
  //------Loop for each frame of Routine 'pause'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = pauseClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame

  // *tPause* updates
  if (t >= 0.0 && tPause.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    tPause.tStart = t;  // (not accounting for frame time here)
    tPause.frameNStart = frameN;  // exact frame index
    tPause.setAutoDraw(true);
  }


  // *kPause* updates
  if (t >= 0.0 && kPause.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    kPause.tStart = t;  // (not accounting for frame time here)
    kPause.frameNStart = frameN;  // exact frame index
    kPause.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { kPause.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (kPause.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});

    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }

    if (theseKeys.length > 0) {  // at least one key was pressed
      kPause.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      kPause.rt = kPause.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }

  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }

  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of pauseComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }

  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function pauseRoutineEnd() {
  //------Ending Routine 'pause'-------
  for (const thisComponent of pauseComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }

  // check responses
  if (kPause.keys === undefined || kPause.keys.length === 0) {    // No response was made
      kPause.keys = undefined;
  }

  psychoJS.experiment.addData('kPause.keys', kPause.keys);
  if (typeof kPause.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('kPause.rt', kPause.rt);
      routineTimer.reset();
      }

  // the Routine "pause" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();

  return Scheduler.Event.NEXT;
}

var kEnd;
var endComponents;
function endRoutineBegin() {
  //------Prepare to start Routine 'end'-------
  t = 0;
  endClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  kEnd = new core.BuilderKeyResponse(psychoJS);

  // keep track of which components have finished
  endComponents = [];
  endComponents.push(tEnd);
  endComponents.push(kEnd);

  for (const thisComponent of endComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;

  return Scheduler.Event.NEXT;
}


function endRoutineEachFrame() {
  //------Loop for each frame of Routine 'end'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = endClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame

  // *tEnd* updates
  if (t >= 0.0 && tEnd.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    tEnd.tStart = t;  // (not accounting for frame time here)
    tEnd.frameNStart = frameN;  // exact frame index
    tEnd.setAutoDraw(true);
  }


  // *kEnd* updates
  if (t >= 0.0 && kEnd.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    kEnd.tStart = t;  // (not accounting for frame time here)
    kEnd.frameNStart = frameN;  // exact frame index
    kEnd.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { kEnd.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (kEnd.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys();

    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }

    if (theseKeys.length > 0) {  // at least one key was pressed
      kEnd.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      kEnd.rt = kEnd.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }

  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }

  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of endComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }

  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEnd() {
  //------Ending Routine 'end'-------
  for (const thisComponent of endComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }

  // check responses
  if (kEnd.keys === undefined || kEnd.keys.length === 0) {    // No response was made
      kEnd.keys = undefined;
  }

  psychoJS.experiment.addData('kEnd.keys', kEnd.keys);
  if (typeof kEnd.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('kEnd.rt', kEnd.rt);
      routineTimer.reset();
      }

  // the Routine "end" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();

  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisScheduler, thisTrial) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      thisScheduler.stop();
    } else if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
