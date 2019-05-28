# dash-merge
Combines many minute-long Tesla dash cam videos into one unified video stream.

## Installation

1. Install Python 3.7 or greater from https://python.org
	* Python 2.7 will not work. Be sure to download python 3.7 or higher.
2. Extract files into an empty directory.
3. You'll want a USB3.0 Drive with >30mbit write speeds. Higher is better.
4. Linux users: install `ffmpeg` using your favorite package manager.

## Usage

1. Delete all video files from the directory you extracted this into earlier.
2. Copy all videos you want to merge into one directory. This program will automatically keep each camera's output separate.
	* Do not rename any of the videos! They should look like `2019-05-28_14-33-left_repeater.mp4`
3. Double click `Merge OSX + Linux` or `Merge Windows`.
4. Check the new output folder for the merged files.

This tool does not take into consideration the time between clips, so where one minute of dash cam footage ends, the
next one will immediately start.

## Troubleshooting

If a terminal or command prompt opens then quickly closes:
1. Check if there's a series of text files named after each camera. i.e. `front.mp4.txt`.
	* If one or more exists, there was an issue running ffmpeg. Verify that its in the local directory or installed globally on your machine.
2. If none of those files exist, check if there's a folder called `output`.
	* If that exists, then there was a problem reading your video files, and some may be corrupted.
	* If the output folder does not exist, check if python3 is installed. From a terminal, run `python3 --version`.

## Licensing

This software is distributed under the GPL v3.0 license and includes ffmpeg, a library which is also distributed under
GPL v3.0. Both licenses can be found in the `LICENSE` file.
