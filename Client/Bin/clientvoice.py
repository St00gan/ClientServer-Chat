import socket
import pyaudio
import wave
import _thread

p = pyaudio.PyAudio()

# record
CHUNK = 1024 # 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 20000
ip = str(socket.gethostbyname(socket.gethostname()))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 48989))

receive_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
send_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Voice chat running (DO NOT EXPECT IT TO WORK FLAWLESSLY RIGHT NOW)")

def receive_data():
    while True:
        try:
            data = s.recv(1024)
            receive_stream.write(data)
        except:
            pass


def send_data():
    while True:
        try:
            data = send_stream.read(CHUNK)
            s.sendall(data)
        except:
            pass

_thread.start_new_thread(receive_data, ())
_thread.start_new_thread(send_data, ())

while True:
    pass
