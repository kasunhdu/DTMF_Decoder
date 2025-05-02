
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

tone1 = wavfile.read('tone01.wav')
tone2 = wavfile.read('tone02.wav')
tone3 = wavfile.read('tone03.wav')

samp_rate1 = tone1[0]
samp_rate2 = tone1[0]
samp_rate3 = tone1[0]

tone_data1 = np.array(tone1[1])
tone_data2 = np.array(tone2[1])
tone_data3 = np.array(tone3[1])






time = np.linspace(0, len(tone_data1) / samp_rate1, num=len(tone_data1))


plt.subplot(2,2,1)
plt.plot(time,tone_data1)



sd.play(tone_data1,samp_rate1)
sd.play(tone_data2,samp_rate2)
sd.play(tone_data3,samp_rate3)
        

for i in range (1,11,1):
    audio_i = tone_data1[1300*(i-1):1300*i]
    fft_data_i = np.fft.fft(audio_i)
    shift_fft_data_i = np.fft.fftshift(fft_data_i)


    ff = np.arange(-samp_rate1/2 , samp_rate1/2 , samp_rate1/1300)

    plt.subplot(2,2,2)
    plt.plot(ff,abs(shift_fft_data_i))
    

plt.show()


