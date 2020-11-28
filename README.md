# reorganize-google-photos-takeout-for-just-media
When you use Google Takeout to export your Google Photos, it will divide them into many folders, and include many .json files that you may not want.  This program consolidates all of your media files into a single folder together.

Combs through a 1-subdirectory deep hierarchy for non-.json files.  Copies all non-.json files to a separate
destination.

Assumes that all non-.json files have unique names.

## Requirement
This project has been successfully tested for Python >= 3.8.

## Install dependencies
>pip install tqdm
