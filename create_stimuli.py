def create_stimuli(num_blocks, num_trials_per_block, stimuli_dir, bCreate_stimuli, temp_seed, expName):

    import PIL.Image as Image
    import PIL.ImageDraw as ImageDraw
    import math
    import numpy as np
    import os
    import shutil
    import pandas as pd
    import glob

    print(bCreate_stimuli)

    # remove condition files suppose less blocks are created, some won't be overwritten
    for iFile in glob.glob('tBlock*'):
        try:
            os.remove(iFile)
        except:
            print("Error while deleting file : ", iFile)

    num_all_trials = num_blocks * num_trials_per_block # need to be dividable by 4 and 3 for now

    if bCreate_stimuli != 2:
        if os.path.isdir(stimuli_dir):
            shutil.rmtree(stimuli_dir)

    def diamond_with_cut(cutVar, size, whatIndex, whatCanvas, whatColor):
        x = x_coordinates[whatIndex]
        y = y_coordinates[whatIndex]
        tpoint = (x, (y + size))
        bpoint = (x, (y - size))
        if cutVar == "R":
            sidept = ((x - size), y)
            tcut = ((x + (size / 2)), (y + (size / 2)))
            bcut = ((x + (size / 2)), (y - (size / 2)))
        else:
            sidept = ((x + size), y)
            tcut = ((x - (size / 2)), (y + (size / 2)))
            bcut = ((x - (size / 2)), (y - (size / 2)))

        whatCanvas.polygon((tpoint, sidept, bpoint, bcut, tcut), fill=tuple(whatColor))

    def shape(whatShape, size, whatIndex, whatCanvas, whatColor):
        if whatShape == 'D':
            x = x_coordinates[whatIndex]
            y = y_coordinates[whatIndex]
            tpoint = (x, (y + size))
            bpoint = (x, (y - size))
            sidept = ((x - size), y)
            sidept_2 = ((x + size), y)
            whatCanvas.polygon((tpoint, sidept, bpoint, sidept_2), fill=tuple(whatColor))

        elif whatShape == 'C':
            x = x_coordinates[whatIndex]
            y = y_coordinates[whatIndex]
            point1 = (x - size * 1.1, y - size * 1.1)
            point2 = (x + size, y + size)

            whatCanvas.ellipse([point1, point2], fill=tuple(whatColor), outline=tuple(whatColor))


    if expName == 'popout_exp0':

        image_height = 600
        image_width = 600
        square_length = 200
        radius = 40
        # this creates a 3X3 grid
        height_grid = math.floor(image_height/square_length)
        width_grid = math.floor(image_width / square_length)

        x_coordinates = np.repeat(np.array(range(width_grid))[np.newaxis, :], height_grid,
                                  axis=0) * square_length + square_length / 2
        x_coordinates = x_coordinates.flatten()
        y_coordinates = np.repeat(np.array(range(height_grid))[:, np.newaxis], width_grid,
                                  axis=1) * square_length + square_length / 2
        y_coordinates = y_coordinates.flatten()
        ## ^ this way, the pos_index for the gird is
        # 0 1 2
        # 3 4 5
        # 6 7 8
        pos_index = list(range(9))

        # 0 is multi, 1 is single
        distract_levels = [0, 1]

        # target, background, distractor
        color_levels = np.array([[[255, 0, 0], [0, 0, 0], [0, 255, 0]],
                                 [[0, 255, 0], [0, 0, 0], [225, 0, 0]]])

        # -1 means mixed in a block, 0 means the first of color levels...
        cue_levels = [-1, 0, 1]

        target_levels = ['L', 'R']
        key_levels = ['z', 'slash'] # https://discourse.psychopy.org/t/trying-to-have-psychopy-take-as-an-input-to-start-the-experiment/1165

        target_pos_index_levels = [1, 3, 5, 7] #list(range(9))

        np.random.seed(temp_seed)
        # by default, all levels haves equal weight, change as needed, like [0, 1, 1] instead of [0, 1]
        distract_levels_indices = np.tile(np.array(list(range(len(distract_levels)))), int(num_all_trials/len(distract_levels)))
        np.random.shuffle(distract_levels_indices)
        distract_condition = [distract_levels[i] for i in distract_levels_indices]

        color_levels_indices = np.tile(np.array(list(range(len(color_levels)))), int(num_all_trials/color_levels.shape[0]))
        np.random.shuffle(color_levels_indices)
        color_condition = [color_levels[i] for i in color_levels_indices] # a list of np arrays

        cue_levels_indices = np.tile(np.array(list(range(-1, len(cue_levels)-1))), int(num_blocks/len(cue_levels)))
        np.random.shuffle(cue_levels_indices)
        cue_condition = np.tile(cue_levels_indices, (num_trials_per_block, 1))
        cue_condition = list(cue_condition.flatten('F'))

        target_levels_indices = np.tile(np.array(list(range(len(target_levels)))),  int(num_all_trials/len(target_levels)))
        np.random.shuffle(target_levels_indices)
        target_condition = [target_levels[i] for i in target_levels_indices]
        key_correlate = [key_levels[i] for i in target_levels_indices]

        target_pos_index_levels_indices = np.tile(np.array(list(range(len(target_pos_index_levels)))),  int(num_all_trials/len(target_pos_index_levels)))
        np.random.shuffle(target_pos_index_levels_indices)
        target_pos_index_condition = [target_pos_index_levels[i] for i in target_pos_index_levels_indices]

        file_name = []
        for iBlock in range(1, num_blocks + 1):
            for iTrial in range((iBlock-1) * num_trials_per_block, iBlock * num_trials_per_block):
                print(iBlock, iTrial)
                iDistract = distract_condition[iTrial]
                iCue = cue_condition[iTrial]
                if iCue != -1:
                    color_condition[iTrial] = color_levels[iCue]
                iColor = color_condition[iTrial]
                iTarget = target_condition[iTrial]
                iTarget_pos_index = target_pos_index_condition[iTrial]
                image = Image.new("RGB", (image_height, image_width))
                draw = ImageDraw.Draw(image)

                # background color
                draw.polygon(((0, 0), (0, image_height), (image_width, image_height), (image_width, 0)), fill=tuple(iColor[1]))
                diamond_with_cut(iTarget, radius, iTarget_pos_index, draw, iColor[0])
                # if iTrial < 10:
                #     image.show()
                # else:
                #     break
                if iDistract == 1:
                    for iPos_index in pos_index:
                        if iPos_index != iTarget_pos_index:
                            iTarget = target_levels[np.random.randint(2)]
                            diamond_with_cut(iTarget, radius, iPos_index, draw, iColor[2])

                iFile_name = 'block_' + '%02d' % iBlock + '_trial_' + '%03d' % iTrial + '.png'
                # iFile_name = os.path.join(stimuli_dir, 'block_' + '%02d' % iBlock + '_trial_' +'%03d' % iTrial + '.png')

                if bCreate_stimuli == 1:
                    if not os.path.isdir(stimuli_dir):
                        os.mkdir(stimuli_dir)
                    image.save(os.path.join(stimuli_dir,iFile_name))

                file_name.append(iFile_name)

        # I could also code in psychopy to do os.path.join but I don't want to translate that into js
        # pavlovia server is linux , see https://gitlab.pavlovia.org/viscoglab/facediscriminationtaskpilot04/blob/master/trialTypes.csv
        linux_file_name = [stimuli_dir + '/' + i for i in file_name]
        pc_file_name = [stimuli_dir + '\\' + i for i in file_name]

        # psychopy calls correct_response
        col_names = ['linux_file_name', 'pc_file_name', 'distract_condition', 'target_color_condition', 'back_color_condition', 'distractor_color_condition',
                     'cue_condition', 'target_condition',
                     'correct_response', 'target_pos_index_condition']

        # so here list get converted to np array, it only works when all the arrays have the same size, color_condition  is the
        # odd one here
        # tAll_trials = pd.DataFrame(np.column_stack([file_name, distract_condition, color_condition, cue_condition, target_condition,
        #                                             key_correlate, target_pos_index_condition]),
        #                            columns=col_names)
        target_color_condition = np.array([i[0] for i in color_condition]) # ntrials * 3 numpy array
        back_color_condition = np.array([i[1] for i in color_condition])
        distractor_color_condition = np.array([i[2] for i in color_condition])

        # the reason we need tolist() here is that when numpy array in pandas written to csv, [0,0,0] becomes [ 0 0 0], cannot be evaled
        tAll_trials = pd.DataFrame(list(zip(linux_file_name, pc_file_name, distract_condition, target_color_condition.tolist(), back_color_condition.tolist(), distractor_color_condition.tolist(),
                                            cue_condition, target_condition,
                                            key_correlate, target_pos_index_condition)),
                                   columns=col_names)

    elif expName == 'popout_diamond_circle_red_green':

        image_height = 600
        image_width = 600
        square_length = 200
        radius = 40
        # this creates a 3X3 grid
        height_grid = math.floor(image_height / square_length)
        width_grid = math.floor(image_width / square_length)

        x_coordinates = np.repeat(np.array(range(width_grid))[np.newaxis, :], height_grid,
                                  axis=0) * square_length + square_length / 2
        x_coordinates = x_coordinates.flatten()
        y_coordinates = np.repeat(np.array(range(height_grid))[:, np.newaxis], width_grid,
                                  axis=1) * square_length + square_length / 2
        y_coordinates = y_coordinates.flatten()
        ## ^ this way, the pos_index for the gird is
        # 0 1 2
        # 3 4 5
        # 6 7 8
        pos_index = list(range(9))

        # 0 is multi, 1 is single
        distract_levels = [0, 1]

        # target, background, distractor
        color_levels = np.array([[[255, 0, 0], [0, 0, 0], [0, 255, 0]],
                                 [[0, 255, 0], [0, 0, 0], [225, 0, 0]]])

        # -1 means mixed in a block, 0 means the first of color levels...
        cue_levels = [-1, 0, 1]

        # target_levels = ['L', 'R']
        target_levels = ['D', 'C']

        key_levels = ['z',
                      'slash']  # https://discourse.psychopy.org/t/trying-to-have-psychopy-take-as-an-input-to-start-the-experiment/1165

        # target_pos_index_levels = [1, 3, 5, 7]  # list(range(9))
        target_pos_index_levels = list(range(9))

        np.random.seed(temp_seed)
        # by default, all levels haves equal weight, change as needed, like [0, 1, 1] instead of [0, 1]
        distract_levels_indices = np.tile(np.array(list(range(len(distract_levels)))),
                                          int(num_all_trials / len(distract_levels)))
        np.random.shuffle(distract_levels_indices)
        distract_condition = [distract_levels[i] for i in distract_levels_indices]

        color_levels_indices = np.tile(np.array(list(range(len(color_levels)))),
                                       int(num_all_trials / color_levels.shape[0]))
        np.random.shuffle(color_levels_indices)
        color_condition = [color_levels[i] for i in color_levels_indices]  # a list of np arrays

        cue_levels_indices = np.tile(np.array(list(range(-1, len(cue_levels) - 1))), int(num_blocks / len(cue_levels)))
        np.random.shuffle(cue_levels_indices)
        cue_condition = np.tile(cue_levels_indices, (num_trials_per_block, 1))
        cue_condition = list(cue_condition.flatten('F'))

        target_levels_indices = np.tile(np.array(list(range(len(target_levels)))), int(num_all_trials / len(target_levels)))
        np.random.shuffle(target_levels_indices)
        target_condition = [target_levels[i] for i in target_levels_indices]
        key_correlate = [key_levels[i] for i in target_levels_indices]

        target_pos_index_levels_indices = np.tile(np.array(list(range(len(target_pos_index_levels)))),
                                                  int(num_all_trials / len(target_pos_index_levels)))
        np.random.shuffle(target_pos_index_levels_indices)
        target_pos_index_condition = [target_pos_index_levels[i] for i in target_pos_index_levels_indices]

        file_name = []
        for iBlock in range(1, num_blocks + 1):
            for iTrial in range((iBlock - 1) * num_trials_per_block, iBlock * num_trials_per_block):
                print(iBlock, iTrial)
                iDistract = distract_condition[iTrial]
                iCue = cue_condition[iTrial]
                if iCue != -1:
                    color_condition[iTrial] = color_levels[iCue]
                iColor = color_condition[iTrial]
                iTarget = target_condition[iTrial]
                iTarget_pos_index = target_pos_index_condition[iTrial]
                image = Image.new("RGB", (image_height, image_width))
                draw = ImageDraw.Draw(image)

                # background color
                draw.polygon(((0, 0), (0, image_height), (image_width, image_height), (image_width, 0)),
                             fill=tuple(iColor[1]))
                shape(iTarget, radius, iTarget_pos_index, draw, iColor[0])
                # if iTrial < 10:
                #     image.show()
                # else:
                #     break
                iShape_levels = target_levels[:]
                iShape_levels.remove(iTarget)
                if iDistract == 1:
                    for iPos_index in pos_index:
                        if iPos_index != iTarget_pos_index:
                            # iTarget = target_levels[np.random.randint(2)]
                            shape(iShape_levels[0], radius, iPos_index, draw, iColor[2])

                iFile_name = 'block_' + '%02d' % iBlock + '_trial_' + '%03d' % iTrial + '.png'
                # iFile_name = os.path.join(stimuli_dir, 'block_' + '%02d' % iBlock + '_trial_' +'%03d' % iTrial + '.png')

                if bCreate_stimuli == 1:
                    if not os.path.isdir(stimuli_dir):
                        os.mkdir(stimuli_dir)
                    image.save(os.path.join(stimuli_dir, iFile_name))

                file_name.append(iFile_name)

        # I could also code in psychopy to do os.path.join but I don't want to translate that into js
        # pavlovia server is linux , see https://gitlab.pavlovia.org/viscoglab/facediscriminationtaskpilot04/blob/master/trialTypes.csv
        linux_file_name = [stimuli_dir + '/' + i for i in file_name]
        pc_file_name = [stimuli_dir + '\\' + i for i in file_name]

        # psychopy calls correct_response
        col_names = ['linux_file_name', 'pc_file_name', 'distract_condition', 'target_color_condition',
                     'back_color_condition', 'distractor_color_condition',
                     'cue_condition', 'target_condition',
                     'correct_response', 'target_pos_index_condition']

        # so here list get converted to np array, it only works when all the arrays have the same size, color_condition  is the
        # odd one here
        # tAll_trials = pd.DataFrame(np.column_stack([file_name, distract_condition, color_condition, cue_condition, target_condition,
        #                                             key_correlate, target_pos_index_condition]),
        #                            columns=col_names)
        target_color_condition = np.array([i[0] for i in color_condition])  # ntrials * 3 numpy array
        back_color_condition = np.array([i[1] for i in color_condition])
        distractor_color_condition = np.array([i[2] for i in color_condition])

        # the reason we need tolist() here is that when numpy array in pandas written to csv, [0,0,0] becomes [ 0 0 0], cannot be evaled
        tAll_trials = pd.DataFrame(list(
            zip(linux_file_name, pc_file_name, distract_condition, target_color_condition.tolist(),
                back_color_condition.tolist(), distractor_color_condition.tolist(),
                cue_condition, target_condition,
                key_correlate, target_pos_index_condition)),
                                   columns=col_names)

    tAll_trials.to_csv('tAll_trials.csv', encoding='utf-8', index=False)

    tAll_blocks = pd.DataFrame(columns=['cur_block_file_name'])
    for iBlock in range(1, num_blocks + 1):
        tCur_block = tAll_trials.iloc[(iBlock-1) * num_trials_per_block: iBlock * num_trials_per_block, ]
        cur_block_file_name = 'tBlock' + '%02d' % iBlock + '.csv'
        tCur_block.to_csv(cur_block_file_name, encoding='utf-8', index=False)
        tAll_blocks = tAll_blocks.append({'cur_block_file_name': cur_block_file_name}, ignore_index=True)

    tAll_blocks.to_csv('tAll_blocks.csv', encoding='utf-8', index=False)

    return key_levels




