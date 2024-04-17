from machine import PWM

class Speaker:
    def __init__(self, pin):
        self.pin = pin
        self.speaker_pwm = PWM(pin)

    def play_audio(self, file_path):
        with open(file_path, 'rb') as f:
            wf = wavfile.WavFile(f)
            for sample in wf.samples():
                self.speaker_pwm.duty(sample)
                time.sleep_us(int(1000000 / wf.rate))
                
    def stop_audio(self):
        self.speaker_pwm.duty(0)

# Utilisation dans un autre fichier :
# from speaker import Speaker

# Instancier un objet Speaker avec la broche GPIO appropriée
# speaker = Speaker(18)

# Jouer un fichier audio
# speaker.play_audio("chat.wav")
