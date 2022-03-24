"""
Author: Rodolfo Ferro @ Datlacuache
Twitter: @rodo_ferro

Script: Main script.
"""

from tools.dataset import extract_frames_from_video


def main():
    """Main function."""

    # Input video
    input_video = 'assets/test.mp4'

    # Output directory
    output_dir = 'assets/frames'

    # Extract frames
    _ = extract_frames_from_video(input_video,
                                  output_dir,
                                  prefix_name='img',
                                  starting_id=1,
                                  frame_step=30,
                                  extension='png')


if __name__ == '__main__':
    main()
