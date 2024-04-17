import wave
import array

def wav_to_raw_pcm(file_path):
    with wave.open(file_path, 'rb') as wf:
        # Read WAV file parameters
        sample_width = wf.getsampwidth()
        num_frames = wf.getnframes()

        # Read audio data
        frames = wf.readframes(num_frames)

        # Convert audio data to raw PCM
        if sample_width == 2:  # 16-bit PCM
            audio_data = array.array('h', frames)
        else:
            raise ValueError("Unsupported sample width")

    return audio_data

# Example usage
raw_pcm_data = wav_to_raw_pcm("meow.wav")
print(raw_pcm_data)
