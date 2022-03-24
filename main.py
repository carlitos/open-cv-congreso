"""
Author: Rodolfo Ferro @ Datlacuache
Twitter: @rodo_ferro

Script: Main script.
"""

from tools.dataset import extract_frames_from_folder


def main():
    """Main function."""

    # Input directory
    input_dir = 'assets'

    # Output directory
    output_dir = 'frames'

    # Extract frames
    extract_frames_from_folder(
        input_dir,
        output_dir,
        prefix_name='img',
        starting_id=1,
        frame_step=30,  # Used for fps
        extension='png')


if __name__ == '__main__':
    main()
