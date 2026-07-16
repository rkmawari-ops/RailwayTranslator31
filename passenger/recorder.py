import os
from datetime import datetime

import numpy as np
import sounddevice as sd
import soundfile as sf


class AudioRecorder:
    def __init__(self, sample_rate=16000, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels

        self.recording = []
        self.stream = None

        os.makedirs("assets/recordings", exist_ok=True)

    def _callback(self, indata, frames, time, status):
        if status:
            print(status)

        self.recording.append(indata.copy())

    def start(self):
        self.recording = []

        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            callback=self._callback,
        )

        self.stream.start()

        print("\n🎤 Recording Started...")

    def stop(self):
        self.stream.stop()
        self.stream.close()

        audio = np.concatenate(self.recording, axis=0)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S.wav")

        filepath = os.path.join(
            "assets",
            "recordings",
            filename,
        )

        sf.write(filepath, audio, self.sample_rate)

        print(f"\n✅ Recording Saved:\n{filepath}")

        return filepath