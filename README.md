# AudioConverter-to-MP3

A dummy audio converter to MP3 file format. 

I used it to convert my lossless albums, in order to put them in my old mp3 player.

The script walks through your target path folders and converts every audio file it finds, preserving the original bitrate up to 320kbps.
Every subfolder of the original folder path will be recursively recreated into a new `converted` folder.

Example:
```
.
└── dir
    ├── subdir1
    |   └── file1.ext
    ├── subdir2
    |   ├── file2.ext
    |   └── file3.ext
    └── file4.ext
.
└── converted
    └── dir
        ├── subdir1
        |   └── file1.mp3
        ├── subdir2
        |   ├── file2.mp3
        |   └── file3.mp3
        └── file4.mp3
```

## Requirements and running
* Python==3.9
* pydub==0.25.1

### Cloning the repo:

```
git clone https://github.com/EnrcDamn/AudioConverter-to-MP3.git
cd AudioConverter-to-MP3
```
### Installing requirements:
```
pip install -r requirements.txt
```

Now you just need to move your target folder (with any subfolder) in `./path/to/AudioConverter-to-MP3/`, and then run the script:

```
python convert_to_mp3.py
```