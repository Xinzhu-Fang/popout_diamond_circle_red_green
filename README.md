# Behavior-popout-attention
A repository for the MTurk studies on popout attention

## list of experiments
### popout_exp0
* popout_exp0 is one version of the popout psychophysics experiment. It is a git submoudule for [Behavior-popout-attention](https://github.com/emeyers/Behavior-popout-attention)
* why submodule instead of a regular folder? to run an exp on pavlovia (a gitlab servera), the html folder has to be on the top level. Therefore, each exp has be in an individual repo on gitlab.
* It's hosted on github at https://github.com/Xinzhu-Fang/popout_exp0/ and on pavlovia at https://gitlab.pavlovia.org/xfang/popout_exp0/
* The online experiment is at https://run.pavlovia.org/xfang/popout_exp0/html/
### popout_diamond_circle_red_green
* popout_diamond_circle_red_green is one version of the popout psychophysics experiment. It is a git submoudule for [Behavior-popout-attention](https://github.com/emeyers/Behavior-popout-attention)
* why submodule instead of a regular folder? to run an exp on pavlovia (a gitlab server), the html folder has to be on the top level. Therefore, each exp has be in an individual repo on gitlab.
* It's hosted on github at https://github.com/Xinzhu-Fang/popout_diamond_circle_red_green/ and on pavlovia at https://gitlab.pavlovia.org/xfang/popout_diamond_circle_red_green/
* The online experiment is at https://run.pavlovia.org/xfang/popout_diamond_circle_red_green/html/

## workflow
* everyone can edit and should only edit the README of Behavior-popout-attention. The REAME of the rest shall me updated regularly calling the function `update_README.py`

## data
* Psychopy stores behavioral data in a csv file named after the participant id, the exp_id, and the date and time of collection with minute precision. If you don't provide a participant id, there will be no participant id in the file.
* Pavlovia stores behavioral data in a csv file named after the participant id, the exp_id, and the date and time of collection with millisecond precision. If you don't provide a participant id, the participant will be called "PARTICIPANT".
* These csv files are stored in `data/`.
* In the csv file, each row corresponds to a trial. Reaction times and correctness are under columns kTrial.rt and kTrial.corr respectively. The rest columns record session info.

## To run the experiment on MTurk
* about mturk
   * the minimum reward for a hit is $0.01
   * the fee collected by mturk is $0.01 per hit.
   * the minimum purchase is $1
   * In one word, testing a new change cost $1

* Title: A simple experiment on the study of vision / DO NOT ACCEPT THIS HIT. STILL PATCHING THE EXPERIMENT
* Description: Take about 6 min. You can take a break around every 2 min. Simple but repetitive.
* Keywords: experiment
* Instructions:
  * We are not asking you to fill a survey but to participate in a simple visual experiment.
  * Run the link below in your browser to initiate the experiment.
  * Put your worker id in the box under participant so that we can pay you.
  * You drop out the experiment but in that case you won't get paid.



## To run the experiment on desktops
* download the latest version of Psychopy from https://github.com/psychopy/psychopy/releases
* run it, the Coder window shall pop up
* click "View >> Go" to builder view, the builder view shall pop up
* load `popout_Cindy.psyexp` and click "Run experiment"


## To create a new experiment
* create a github repo called [new exp name] with a README or .gitignore (something doesn't matter)
* in `Behavior-popout-attention`, do `git submodule add [github repo url of new exp]`
* Add sections for the new exp in `create_*.py` in `popout_exp0` conditioning on the expNames. Specify experiment parameters in `create_exp.py`. They will get stored in `tExp.csv` and read by `popout_Cindy.psyexp`. `create_exp.py` calls `create_stimuli.py` to create all the image files stored in the folder `stimuli` and condition files in the root dir.
* add the new exp to `dests` in `copy_cindy_exp_file_in.py` and run it.
* change into dir `[new exp name]/`, run `create_exp.py`, run `popout_Cindy.psyexp` in psychopy
* cycle through the above 3 steps until you are satisfied with the new exp
* once you decide to put it on pavlovia, create an empty repo on pavlovia, do `git remote add pav [pavlovia repo url]`
* run `copy_files_into_resources_in_html.py`, then push to both github and pavlovia
* click "Run the study online (with pavlovia) in the builder view.
* Notes:
    * Do not tamper with the csv files!
    * All "create_*.py" are meant to be the same across exps, so that you don't change the wrong file of the same name.

## to do now
* there is this nomodule.js for file explorer or some other browser. have being ignoring it and using chrome. other main browsers need to be tested
* issue: https://discourse.psychopy.org/t/completely-different-scales-in-online-study/6603

## to polish later
* the cross drawn in Psychopy in not supported in Psychojs yet. Write a function called `create_fixation()` called by `createt_stimuli()` to create a white cross of the same color background and same size of the stimuli image.
* the current workflow is kind of slow with all the file copying
* .js are no longer exported from my .psyexp. Something, maybe tiny, must have gone wrong. https://discourse.psychopy.org/t/psychopy-does-not-output-js-files/7660



## Ethan's note
https://docs.google.com/document/d/1IKP6N28dwQcn_nixmHb1ZAVyQHVueh-bLpo2Gh9hDBA/edit
