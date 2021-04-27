import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
from scipy.fftpack.pseudo_diffs import shift 

N = 2 ** 5
wave = signal.boxcar(N)
amp = 2.0 * fft(wave, 2048) / N 
freq = np.linspace(-0.5, 0.5, len(amp))
magnitude = 20 * np.log10(np.abs(fftshift(amp / abs(amp).max())))

# x = fftshift(amp)
# print(x)
# plt.plot(x)
# plt.show()

# print(wave.shape, wave)
# plt.plot(wave)
# plt.show()


# print(amp.shape)
# plt.plot(amp)
# plt.show()

# plt.plot(freq, magnitude)
# plt.axis([-0.5, 0.5, -60, 0])
# plt.ylabel("magnitude [db]")
# plt.xlabel("normalized frequency [per sample]")
# plt.show()

# やってみる
xs = np.linspace(0, 2*np.pi, 100)
ys = np.sin(xs)
wave = fft(ys, 2048)
wave_shift = fftshift(wave)
freq = np.linspace(-0.5, 0.5, len(wave))
plt.plot(freq, wave_shift)
plt.show()