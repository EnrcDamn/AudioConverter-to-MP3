import os
import mimetypes
from pydub import AudioSegment
from pydub.utils import mediainfo

ORIGINAL_FOLDER = "."
CONVERTED_FOLDER = "converted"
SAMPLE_RATE = 44100
MAX_BITRATE = 0

def is_audio_file(filename):
    # get file mediatype
    mediatype = mimetypes.guess_type(filename)[0]
    if mediatype != None:
        mediatype = mediatype.split('/')[0]
        if mediatype == 'audio':
            return True
    return False


def convert_audio_files(original_folder, converted_folder, sample_rate):
    # go through all the files in the folder
    for path, _, files in os.walk(original_folder):
        for file in files:
            if is_audio_file(file):
                # extract filenames and media infos from the original files and rename output files
                original_filename = os.path.join(path, file)
                original_bitrate = mediainfo(original_filename)['bit_rate']
                new_filename = os.path.splitext(os.path.basename(original_filename))[0] + ".mp3"
                converted_path = os.path.join(converted_folder, path)
                os.makedirs(converted_path, exist_ok=True)

                # write output mp3 files
                converted_audio = AudioSegment.from_file(original_filename)
                converted_audio.export(
                    os.path.join(converted_path, new_filename),
                    format="mp3",
                    bitrate=original_bitrate
                    )
    print(f"\n===============================")
    print(f"Process completed successfully!")
    print(f"===============================")

if __name__ == "__main__":
    convert_audio_files(ORIGINAL_FOLDER, CONVERTED_FOLDER, SAMPLE_RATE)