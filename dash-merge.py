# Combines Tesla dash cam videos.
# Copyright (C) 2019 Russell Small
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import re
import subprocess

files = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".mp4")]
filesByCam = dict()

FFMPEG = "ffmpeg"

if os.path.isfile("ffmpeg") or os.path.isfile("ffmpeg.exe"):
	FFMPEG = "./ffmpeg"

for file in files:
	parts = re.split("[-_]", file, maxsplit=5)
	if len(parts) != 6:
		continue;

	label = parts[-1]
	if not label in filesByCam:
		filesByCam[label] = []

	filesByCam[label].append(file)

if not os.path.isdir("output"):
	os.mkdir("output")

for label, fileList in filesByCam.items():
	fileList.sort()

	with open("videos-" + label + ".txt", "w") as fl:
		fl.writelines(["file '" + f + "'\n" for f in fileList])
		fl.flush()
		fl.close()

	subprocess.run([FFMPEG, "-f", "concat", "-i", "videos-" + label + ".txt", "-c", "copy", "output/" + label])

	os.remove("videos-" + label + ".txt")

print("\n")
print("\n")

input("Press enter to continue...")
