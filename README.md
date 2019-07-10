# popout_exp0
* popout_exp0 is a git submoudule for [Behavior-popout-attention](https://github.com/emeyers/Behavior-popout-attention)
* why submodule instead of a regular folder? to run an exp on pavlovia, the html folder has to be on the top leve
* It's hosted on github at https://github.com/Xinzhu-Fang/popout_exp0/ and on pavlovia at https://gitlab.pavlovia.org/xfang/popout_exp0/
* The online experiment is at https://run.pavlovia.org/xfang/popout_exp0/html/

## workflow
* code on your own branch of your local repo and of the github remote. Cindy is responsible for pulling your branch into master on github and updating the master of pavlovia.
* everyone can change the README on master and should only edit the master one.

## data
* Psychopy stores behavioral data in a csv file named after the subject number, the exp_id, and the date and time of collection, and save these files in `data/`
* In the csv file, each row corresponds to a trial. Reaction times and correctness are under columns kTrial.rt and kTrial.corr respectively. The rest columns record session info.

## To run the experiment on desktops
* download the latestest version of psychopy from https://github.com/psychopy/psychopy/releases
* run it, the Coder window shall pop up
* click View >> Go to builder view, the builder view shall pop up
* load `popout_Cindy.psyexp` and run it by clicking the green triangle 


## To modify/create an experiment
* Specify experiment parameters in `create_tExp.m`. They will get stored in `tExp.csv` and read by `popout_Cindy.psyexp` to create the experiment. `create_tExp.m` calls `create_Stimuli.m` to create all the image files stored in the folder `stimuli` and condition files in the root dir. 


## to do
* the cross drawn in psychopy in not supported in psychojs yet. Write a function called `create_fixation()` called by `createt_stimuli()` to create a white cross of the same color background and same size of the stimuli image. 
* Temporary US residents are not allowed to work on MTurk. I have a requester account now, someone creates a worker acct.


