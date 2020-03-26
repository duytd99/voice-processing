import sounddevice as sd
import soundfile as sf
import time
import queue

q = queue.Queue()

def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

def record(filename):
        try:
            with sf.SoundFile(filename, mode='x', samplerate=16000, channels=1) as file:
                with sd.InputStream(samplerate=16000, device=sd.default.device, channels=1, callback=callback):
                    print('Press any key to stop ')
                    print('If not working, please interrupt the kernel manually')
                    while True:
                        file.write(q.get())
        except KeyboardInterrupt:
            print('Finished recording ' + filename)

record('testRecord.wav')