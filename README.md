## list of experiments
### popout_exp0
* popout_exp0 is one version of the popout psychophysics experiment. It is a git submoudule for [Behavior-popout-attention](https://github.com/emeyers/Behavior-popout-attention)
* why submodule instead of a regular folder? to run an exp on pavlovia (a gitlab servera), the html folder has to be on the top level. Therefore, each exp has be in an individual repo on gitlab. 
* It's hosted on github at https://github.com/Xinzhu-Fang/popout_exp0/ and on pavlovia at https://gitlab.pavlovia.org/xfang/popout_exp0/
* The online experiment is at https://run.pavlovia.org/xfang/popout_exp0/html/
### popout_diamond_circle_red_green 
* popout_diamond_circle_red_green is one version of the popout psychophysics experiment. It is a git submoudule for [Behavior-popout-attention](https://github.com/emeyers/Behavior-popout-attention)
* why submodule instead of a regular folder? to run an exp on pavlovia (a gitlab servera), the html folder has to be on the top level. Therefore, each exp has be in an individual repo on gitlab. 
* It's hosted on github at https://github.com/Xinzhu-Fang/popout_diamond_circle_red_green/ and on pavlovia at https://gitlab.pavlovia.org/xfang/popout_diamond_circle_red_green/
* The online experiment is at https://run.pavlovia.org/xfang/popout_diamond_circle_red_green/html/

## workflow
* code on your own branch of your local repo and of the github remote. Cindy is responsible for pulling your branch into master on github and updating the master of pavlovia.
* everyone can change the README on master and should only edit the master one.

## data
* Psychopy stores behavioral data in a csv file named after the subject number, the exp_id, and the date and time of collection, and save these files in `data/`
* In the csv file, each row corresponds to a trial. Reaction times and correctness are under columns kTrial.rt and kTrial.corr respectively. The rest columns record session info.

## To run the experiment on desktops
* download the latestest version of psychopy from https://github.com/psychopy/psychopy/releases
* run it, the Coder window shall pop up
* click "View >> Go" to builder view, the builder view shall pop up
* load `popout_Cindy.psyexp` and click "Run experiment" 


## To create a new experiment 
* create a github repo called [new exp name] with a README or .gitignore (something doesn't matter)
* in `Behavior-popout-attention`, do `git submodule add [github repo url of new exp]`
* Add sections for the new exp in `create_*.py` in `popout_exp0` conditioning on the expNames. Specify experiment parameters in `create_exp.py`. They will get stored in `tExp.csv` and read by `popout_Cindy.psyexp`. `create_exp.py` calls `create_stimuli.py` to create all the image files stored in the folder `stimuli` and condition files in the root dir. 
* add the new exp to `dests` in `copy_cindy_exp_file_in.py` and run it (also use this file to update README, etc., go in there and change accordingly)
* change in to dir [new exp name], run `create_exp.py`, run `popout_Cindy.psyexp` in psychopy 
* cycle through the above 3 steps until you are satisfied with the new exp
* once you decide to put it on pavlovia, create an empty repo on pavlovia, do `git remote add pav [pavlovia repo url]`
* run `copy_cindy_exp_file_in.py`, then push to both github and pavlovia
* click "Run the study online (with pavlovia) in the builder view.
* Notes:
    * Do not tamper with the csv files!
    * All "create_*.py" are meant to be the same across exps, so that you don't change the wrong file of the same name.

## to do now
* Temporary US residents are not allowed to work on MTurk. I have a requester account now, someone creates a worker acct.
* there is this nomodule.js file file explorer or some other browser. have being ignoring and using chrome. other main browswers need to be tested

## to polish later
* the cross drawn in psychopy in not supported in psychojs yet. Write a function called `create_fixation()` called by `createt_stimuli()` to create a white cross of the same color background and same size of the stimuli image.
* the current workflow is kind of slow with all the file copying


