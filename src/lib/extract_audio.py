import tempfile
import numpy as np
import subprocess
from scipy.io import wavfile


def extract(file):
    with tempfile.NamedTemporaryFile(mode='w+b', suffix='.mp4') as fp_v:
        with tempfile.NamedTemporaryFile(mode='w+b', suffix='.wav') as fp_a:
            fp_v.write(np.frombuffer(file, dtype=np.uint8))
            command = "ffmpeg -y -i " + fp_v.name + " -ab 160k -ac 1 -ar 16000 -vn " + fp_a.name

            subprocess.call(command, shell=True)

            # fs, data = wavfile.read(fp_a.name) Audio não era executado quando o retorno era data
            #                                    talvez seja necessário realizar adaptações

            f = open(fp_a.name, "rb")
            fileData = f.read()
            f.close()

            return bytes(fileData)