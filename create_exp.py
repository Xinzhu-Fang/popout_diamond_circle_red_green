import create_stimuli
import pandas as pd
import os
# naming scheme: all variable names fed to psychopy are prefixed with the component they serve
# (e.g., kTrial_) otherwise 'my_'. all component names are the routine name
# prefixed with the component type name (e.g. kTtrial is the keyboard input
# on routine 'trial'). variables not needed by psychopy are prefixed with
# 'temp_', some of which that are important metainfo and are stored in the table. _2" indicates practice block


temp_grid_type = 1
temp_stimuli_dir = 'stimuli'
# when tweaking exp paradigm, set bCreate_stimuli to 0 so stimuli don't
# get created but existing files will get removed to make sure sound
# files and condition files are consistent.
# when teaking other aspects of exp design such as messages, set to 2 so stimuli don't
# change
bCreate_stimuli = 1

# temp_seed = 2  # sum(100*clock)#
my_num_of_blocks = 3 # divisible by number of cue type of equal weights
temp_num_of_trials = 36  # this number has to be divisible by number of locations
temp_seed = 1 #
temp_expName = os.path.split(os.getcwd())[1] # get the current dir/exp name
kTrial_allowed_keys = create_stimuli.create_stimuli(my_num_of_blocks, temp_num_of_trials,
                                                    temp_stimuli_dir, bCreate_stimuli, temp_seed, temp_expName)

# # must use double quote
# kTrial_break = "q"  # cannot skip block

# tFeedback_duration = 2.2  # 2.5
# tBlank_duration = 0  # 0.2 #

pTrial_size = 0.1 # same height as width by setting unit as height in builder https://www.psychopy.org/general/units.html#units
pTrial_duration = 0.4
# ! users have screens of different sizes and resolutions
# my monitor psychopy can adjust to the actual window size and returns a
# warning if it is not the size given
# my_window_height = 2560
# my_window_width = 1440

iTrial_size = 0.9 # same height as width
iTrial_duration = 0.5

tTrial_duration = 0.2 # blank
my_text_height = 0.05 # not used
# pTrial_address = '0x1FF0'

trials_nReps = 1
blocks_nReps = 1
temp_stimuli_dir = 'stimuli'

# if ispc
#     pathparts = strsplit(pwd, '\')
#     else
#     pathparts = strsplit(pwd, '/')
#
#     end
#     my_expName = pathparts(end)


tEnd_text = 'You finished it!'
# ! should show percentage correct after the first block to make sure they got it.
# tFeedback_noresp = cellstr('You missed it')
# tFeedback_wrresp = cellstr('Wrong')
# tFeedback_coresp = cellstr('Correct')
kPause_key = 'space'
tPause_text = 'Take a break as you needed. Press the ' + kPause_key + ' key when you are ready to resume'

# when tweaking exp paradigm, set bCreate_stimuli to 0 so stimuli don't
# get created but existing files will get removed to make sure sound
# files and condition files are consistent.
# when teaking other aspects of exp design such as messages, set to 2 so stimuli don't
# change

kTrial_duration = 1 + pTrial_duration + iTrial_duration

temp_task_trial_duration = kTrial_duration
temp_block_duration_in_minutes = temp_task_trial_duration * temp_num_of_trials / 60

if temp_expName == 'popout_exp0':
    tInstr_text = 'Welcome to our psychophysics experiment! You will see diamonds display briefly on the screen,' + \
                  'and the task is to respond to which corner (left or right) is cut off of the target diamond.' +\
                  'For displays with several diamonds, the target diamond will be the only one of its color.' +\
                  '(All other diamonds will be a drastically different color, and you should not respond to any of these.)' + \
                  'If the left corner is cut off the target diamond, please press the Z key.If the right corner is cut off, please press the / key.' +\
                  'In some blocks, the target color does not change' +\
                  'There will be ' + str(my_num_of_blocks) + ' in total. ' +\
                  'Each block will be ' + str(temp_block_duration_in_minutes) + ' minutes.'
elif temp_expName == 'popout_diamond_circle_red_green':
    tInstr_text = 'Welcome to our psychophysics experiment! You will see diamonds or circles display briefly on the screen,' + \
                  'and the task is to respond to which shape is of the target diamond.' + \
                  'For displays with several items, the target item will be the only one of its color.' + \
                  '(All other items will be a drastically different color, and you should not respond to any of these.)' + \
                  'If the target is a diamond, please press the Z key (hint: a diamond has corners like the letter z.' + \
                  'If the target is a circle, please press the / key (hint: a circle is smooth like the / key.' + \
                  'In some blocks, the target color does not change' + \
                  'There will be ' + str(my_num_of_blocks) + ' in total. ' + \
                  'Each block will be ' + str(temp_block_duration_in_minutes) + ' minutes.'

col_names =['tInstr_text', 'tPause_text', 'tEnd_text', 'iTrial_duration', 'tTrial_duration', 'iTrial_size', 'pTrial_duration', 'pTrial_size',
            'my_num_of_blocks', 'temp_num_of_trials', 'kTrial_duration',
            'temp_block_duration_in_minutes', 'trials_nReps', 'blocks_nReps', 'kTrial_allowed_keys']

tExp = pd.DataFrame([(tInstr_text, tPause_text, tEnd_text, iTrial_duration, tTrial_duration, iTrial_size, pTrial_duration, pTrial_size,
                      my_num_of_blocks, temp_num_of_trials, kTrial_duration,
                      temp_block_duration_in_minutes, trials_nReps, blocks_nReps, kTrial_allowed_keys)],
                    columns=col_names)
tExp.to_csv('tExp.csv', encoding='utf-8', index=False)
