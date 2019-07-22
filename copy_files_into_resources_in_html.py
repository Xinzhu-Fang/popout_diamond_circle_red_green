# protection, remember to seal after you are done
if 1 == 1:
    import os
    import shutil
    import glob
    src = '.'
    dest = os.path.join('html', 'resources')

    # ideally we want to clean the resources folder before copying new files over, but
    # because I am having trouble deleting it on pc https://stackoverflow.com/questions/2656322/shutil-rmtree-fails-on-windows-with-access-is-denied
    # let's skip this step for now. psychopy makes resources read-only
    # it was fine when I created exp2,

    print(os.path.isdir(dest))
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    ##

    shutil.copytree('stimuli', os.path.join(dest, 'stimuli'))
    src_files = glob.glob(os.path.join('*.csv'))
    src_files.append('fixation.png')
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        print(full_file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
