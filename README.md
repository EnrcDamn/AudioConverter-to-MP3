# AudioConverter-to-MP3

A dummy audio converter to MP3 file format. 

I used it to convert my lossless albums, in order to put them into my old and dusty MP3 player.

The script:
* walks through your target path folders;
* creates a new `converted` path;
* converts every audio it finds, preserving the original bitrate up to 320kbps;
* ignores any other file format.

Every subfolder of the original folder path will be recursively recreated in the new `converted` folder.

For example, launching the script on top of a `./dir` path:
```
.
└── dir
    ├── subdir1
    |   └── file1.audio
    ├── subdir2
    |   ├── file2.audio
    |   └── file3.audio
    ├── file4.audio
    └── file5.notaudio
```
Will result in a new `./converted` path looking like this:
```
.
├── converted
|   └── dir
|       ├── subdir1
|       |   └── file1.mp3
|       ├── subdir2
|       |   ├── file2.mp3
|       |   └── file3.mp3
|       └── file4.mp3
└── dir
    ├── ...
    ...
```

## Requirements and running
* Python 3
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

Now you just need to <u>move your target folder</u> (with any subfolder) in `path/to/AudioConverter-to-MP3`, and then run the script:

```
python convert_to_mp3.py
```