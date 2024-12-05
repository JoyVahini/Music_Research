from pydub import AudioSegment
import os

input_folder_path = "E:/MSc Research/MSc project/minor_corrections/Thodi/Thodi.wav"
output_folder = 'E:/MSc Research/MSc project/minor_corrections/Thodi/1min'

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




def split_wav(file_path, output_folder, clip_length=60):
    audio = AudioSegment.from_wav(file_path)

    total_length = len(audio) // 1000 
    num_clips = total_length // clip_length
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(num_clips):
        start_time = i * clip_length * 1000
        end_time = start_time + clip_length * 1000
        clip = audio[start_time:end_time]
        clip_name = os.path.join(output_folder, f'Thodi_{i+1}.wav')
        clip.export(clip_name, format='wav')
        print(f'Exported {clip_name}')

    if total_length % clip_length != 0:
        start_time = num_clips * clip_length * 1000
        clip = audio[start_time:]
        clip_name = os.path.join(output_folder, f'Thodi_{num_clips+1}.wav')
        clip.export(clip_name, format='wav')
        print(f'Exported {clip_name}')


concatenate_splitted_files(input_folder_path)
split_wav(input_folder_path, output_folder)
