import os
import librosa
from pydub import AudioSegment
from pydub.utils import mediainfo
import soundfile
import time

start_time = time.time()

DATASETH_PATH = "audio"
CONVERTED_PATH = "converted"
SAMPLE_RATE = 44100
MAX_BITRATE = 0


def convert_audio_files(dataset_path, converted_path, sample_rate):

    # go through all the files in the dataset
    for path, subdirs, files in os.walk(dataset_path):
        for file in files:
            if file[-3:] == "mp3":

                # extract filenames from mp3 and rename output path/files
                original_file = os.path.join(path, file)
                original_bitrate = mediainfo(original_file)['bit_rate']
                new_filename = os.path.splitext(os.path.basename(original_file))[0] + ".mp3"

                # write wav files
                converted_audio = AudioSegment.from_file(original_file)
                if not os.path.exists(converted_path):
                    os.makedirs(converted_path)
                converted_audio.export(os.path.join(converted_path, new_filename), format="mp3", bitrate=original_bitrate)

if __name__ == "__main__":
    convert_audio_files(DATASETH_PATH, CONVERTED_PATH, SAMPLE_RATE)