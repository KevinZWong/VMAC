from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav
preload_models()
text_prompt = """
     hey there how are you doing, my name is kevin wong.
"""

sentences = [
"nickacado avacado is very very very fat",
]

for i in range(0, 10):
     for j in sentences:
          audio_array = generate_audio(j, history_prompt= "v2/en_speaker_" + str(i))
          write_wav("textAivoices/test.wav", SAMPLE_RATE, audio_array)