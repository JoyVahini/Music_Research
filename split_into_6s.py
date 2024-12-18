from pydub import AudioSegment
import os

input_folder_path = "E:/MSc Research/MSc project/github_repo/datasets/Sarasangi/Sarasangi.wav"
output_folder = 'E:/MSc Research/MSc project/github_repo/datasets/Sarasangi/6s'

def split_wav(file_path, output_folder, clip_length=6):
    audio = AudioSegment.from_wav(file_path)

    total_length = len(audio) // 1000 
    num_clips = total_length // int(clip_length)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(num_clips):
        start_time = i * int(clip_length) * 1000
        end_time = start_time + int(clip_length) * 1000
        clip = audio[start_time:end_time]
        clip_name = os.path.join(output_folder, f'Sarasangi_{i+1}.wav')
        clip.export(clip_name, format='wav')
        print(f'Exported {clip_name}')

    if total_length % int(clip_length) != 0:
        start_time = num_clips * int(clip_length) * 1000
        clip = audio[start_time:]
        clip_name = os.path.join(output_folder, f'Sarasangi_{num_clips+1}.wav')
        clip.export(clip_name, format='wav')
        print(f'Exported {clip_name}')

split_wav(input_folder_path, output_folder)
