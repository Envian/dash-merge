# dash-merge
Combines many minute-long Tesla dash cam videos into one unified video stream.

## Installation

1. Install Python 3 from https://python.org
	* Python 2.7 will not work. Be sure to download Python 3.6 or higher.
2. Extract files into an empty directory.
3. You'll want a USB3.0 Drive with >30mbit write speeds. Higher is better.
4. Linux users: install `ffmpeg` using your favorite package manager.

Note: Only `ffmpeg` (Win/OSX), `dash-merge.py`, and `merge.sh` (If needed) are required to run this program.

## Usage

1. If this is not your first time running this program, delete or move all previous videos out of the directory, or move the executables.
2. Copy all videos you want to merge into one directory. This program will automatically keep each camera's output separate.
	* Do not rename any of the videos! They should look like `2019-05-28_14-33-left_repeater.mp4`
	* Do not run this from your flash drive. It may work, but it will not work well.
3. Run `dash-merge.py` by double clicking it. If it does not seem to do anything, see Troubleshooting below.
4. Check the new output folder for the merged files.

This tool does not take into consideration the time between clips, so where one minute of dash cam footage ends, the
next one will immediately start.

## Troubleshooting

If a terminal or command prompt opens then quickly closes:
1. Check if there's a series of text files named after each camera. i.e. `front.mp4.txt`.
	* If one or more exists, there was an issue running *ffmpeg*. Verify that its in the local directory or installed globally on your machine.
2. If none of those files exist, check if there's a folder called `output`.
	* If that exists, then there was a problem reading your video files, and some may be corrupted. See below.
3. If the output folder does not exist verify you are running Python 3.
	* Windows Users: Right click `dash-merge.py`, open with, and select Python 3. You may need to find the executable. Select `python.exe`.
	* OSX & Linux users: try running `merge.sh` instead. If that does not work, ensure Python 3 is installed.

If you get errors while processing the files, have no videos, or the output videos are corrupted, one of your input videos
may be corrupted. Videos can often be repaired with tools such as VLC, but no guarantees. The best course of action is
to figure out which Videos have been corrupted and remove them.

## Licensing

This software is distributed under the GPL v3.0 license and includes *ffmpeg*, a library which is also distributed under
GPL v3.0. Both licenses can be found in the `LICENSE` file.
