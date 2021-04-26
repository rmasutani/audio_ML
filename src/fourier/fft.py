import numpy as np 

PI = np.pi

def fft(x):
    N = x.shape[0]
    hatx = np.zeros(N, dtype="complex")
    k = np.arange(0, N//2)
    W = np.exp(-1j * 2 * PI * k/N)

    if N == 2:
        # 1st butterfly op
        hatx[0] = x[0] + x[1]
        hatx[1] = x[0] - x[1]
        return hatx
    
    if N >= 4:
        # butterfly op
        L = fft(x[0:N:2])
        R = fft(x[1:N:2])

        hatx[0:N//2] =  L + W*R
        hatx[N//2:N] = L - W*R
        return hatx

if __name__ == '__main__':
    print("")
    

