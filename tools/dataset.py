"""
Author: Rodolfo Ferro @ Datlacuache
Twitter: @rodo_ferro

Script: Tools module.
"""

from glob import glob
import os

from tqdm import tqdm
import cv2


def extract_frames_from_video(input_video,
                              output_dir,
                              prefix_name='img',
                              starting_id=1,
                              frame_step=30,
                              extension='jpg'):
    """Extracts frames from input video.

    Parameters
    ----------
    input_video : str
        The path to the input video file. Must be a mp4 video.
    output_dir : str
        The path to the output directory.
    prefix_name : str
        The prefix name for the output frames.
    starting_id : int, optional
        The start id for the output frames.
    frame_step : int, optional
        The frame step for the output frames (used for fps).
    extension : str, optional
        The extension for the output frames.

    Returns
    -------
    frame_id : int
        The following (starting) id for file names.
    """

    # If output folder does not exist, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize frame IDs and video capture
    iter_id = 0
    frame_id = starting_id
    vid = cv2.VideoCapture(input_video)
    total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f'[INFO] {total_frames} frames will be processed')

    pbar = tqdm(total=total_frames - 1)
    while True:
        ret, frame = vid.read()

        if ret:
            if iter_id % frame_step == 0:
                frame_name = prefix_name + f'_{frame_id:0>10}.{extension}'
                out_file = os.path.join(output_dir, frame_name)
                cv2.imwrite(out_file, frame)
                frame_id += 1

            pbar.update(1)
            iter_id += 1
        else:
            break

    vid.release()
    cv2.destroyAllWindows()

    print(f'[INFO] {frame_id - starting_id} frames extracted')

    return frame_id


def extract_frames_from_folder(input_dir,
                               output_dir,
                               prefix_name='img',
                               starting_id=1,
                               frame_step=30,
                               extension='jpg'):
    """Extracts frames from folder."""

    # List sorted videos from folder
    videos = glob(os.path.join(input_dir, '*.mp4'))
    videos = sorted(videos)

    # Initialize frame IDs and video capture
    next_id = starting_id

    # Iterate over videos
    for video in videos:
        next_id = extract_frames_from_video(video,
                                            output_dir,
                                            prefix_name=prefix_name,
                                            starting_id=next_id,
                                            frame_step=frame_step,
                                            extension=extension)

    print(f'[INFO] {next_id - starting_id} frames extracted')
