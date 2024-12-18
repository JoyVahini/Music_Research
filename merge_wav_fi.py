from pydub import AudioSegment
import os

input_folder_path = "E:/MSc Research/MSc project/minor_corrections/Thodi/Thodi.wav"

def concatenate_splitted_files(folder_path):
    combined = AudioSegment.empty()
    wav_files = [f for f in sorted(os.listdir(folder_path)) if f.endswith(".wav")]
    chunk_size = 10 
    for i in range(0, len(wav_files), chunk_size):
        chunk = wav_files[i:i + chunk_size]
        chunk_audio = AudioSegment.empty()
        
        for filename in chunk:
            file_path = os.path.join(folder_path, filename)
            audio = AudioSegment.from_wav(file_path)
            chunk_audio += audio
        combined += chunk_audio
    output_path = os.path.join(folder_path, "Thodi.wav")
    combined.export(output_path, format="wav")

    print(f"WAV files have been merged and saved as {output_path}")

concatenate_splitted_files(input_folder_path)
