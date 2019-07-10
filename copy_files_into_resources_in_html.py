# protection, remember to seal after you are done
if 1 == 0:
    import os
    import shutil
    import glob
    src = '.'
    dest = os.path.join('html', 'resources')
    shutil.rmtree(dest)
    shutil.copytree('stimuli', os.path.join(dest, 'stimuli'))
    src_files = glob.glob(os.path.join('*.csv'))
    src_files.append('fixation.png')
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        print(full_file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)
