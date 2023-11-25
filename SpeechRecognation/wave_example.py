import wave

obj = wave.open('sample-9s.wav', 'rb')

print("Numbe of channels ", obj.getnchannels())
print("Sample width ", obj.getsampwidth())
print("Frame rate ", obj.getframerate())
print("Number of Frames ", obj.getnframes())
print("Parameters ", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)