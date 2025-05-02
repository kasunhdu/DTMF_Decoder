# DTMF_Decoder
Dual tone multi frequency (DTMF)

Dual tone multi frequency (DTMF) is a technology used with touch tone phones, best known to users as the sound made when pressing a number key. It signals the phone company that you want to make a call and sends a command to the switch.
![ns-dtmf_frequencies-h_half_column_mobile](https://github.com/user-attachments/assets/7678c488-a7e9-435d-a225-6147c871f438)

We can use python's scipy.io library to read WAV file as array and converted it into numpy array. After that used numpy's FFT (Fourier Transform) to convert this time domain signal into frequency domain. After that identified its relevant frequencies.
![1712428623763](https://github.com/user-attachments/assets/0f77e58d-59c6-42ff-92f3-299e2d67f451)


