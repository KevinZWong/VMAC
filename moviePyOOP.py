from DynamicEffectsOOP import DynamicPositionClip
from moviepy.editor import *
from moviepy.video.fx.all import crop, resize
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioArrayClip
from moviepy.video.compositing.transitions import crossfadein
from random import uniform
import concurrent.futures
import os
import subprocess
import ffmpeg
import numpy as np
from queue import Queue
from threading import Thread

class VideoGenerator:

    def __init__(self):
        self.size = (1080,1920)
        self.font="Lane"
        self.color="White"
        self.bg_color=(0, 0, 0, 0)
        self.fontsize=25   
        self.framerate = 24
        self.bg_width = 1080
        self.bg_height = 1920
            
    def getFontsize(self):
        return self.fontsize
    def setFontsize(self, initFontsize): 
        self.fontsize = initFontsize
    def getSize(self):
        return self.size
    def setSize(self, initSize): 
        self.size = initSize
    def getFont(self):
        return self.font
    def setFont(self, initFont): 
        self.font = initFont
    def getColor(self):
        return self.color
    def setColor(self, initColor): 
        self.color = initColor
    def getBg_color(self):
        return self.bg_color
    def setBg_color(self, initBg_color): 
        self.bg_color = initBg_color

    def getLengthAudioFile(self, fname):
        audio = AudioFileClip(fname)
        duration = audio.duration
        return duration



    def add_static_image_to_audio(self, image_path, audio_path, output_path):

        audio_clip = AudioFileClip(audio_path)
        image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
        image_clip = image_clip.set_audio(audio_clip)
        image_clip.write_videofile(output_path, fps=24)

    def cropVideo(self, clip):
        # Get the original dimensions of the clip
        width, height = clip.size

        # Calculate the dimensions of the new clip with a 9:16 aspect ratio
        new_width = int(height * 9 / 16)
        new_height = height

        # Calculate the x-coordinate of the left edge of the crop box
        left = (width - new_width) / 2

        # Crop the clip to the new dimensions
        cropped_clip = clip.crop(x1=left, y1=0, x2=left+new_width, y2=new_height)

        return cropped_clip



    def generateBackgroundFootage(self, final_duration, folder_name):
        def get_video_lengths(folder_path):
            video_lengths = []
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".mp4"):
                    file_path = os.path.join(folder_path, file_name)
                    video = VideoFileClip(file_path)
                    video_lengths.append((file_path, video.duration))
            return video_lengths

        video_files_durations = get_video_lengths(folder_name)
        #random.shuffle(video_files_durations) was i high when i wrote this?

        currentDuration = 0
        index = 0
        clipList = []
        while currentDuration < final_duration and index < len(video_files_durations):
            file_path, duration = video_files_durations[index]
            clipList.append(VideoFileClip(file_path))
            currentDuration += duration
            index += 1

        final_clip = concatenate_videoclips(clipList)
        trimmed_clip = final_clip.subclip(0, final_duration)

        return trimmed_clip

    # generates back ground footage based on the inputed times, diffrent for each image
    '''

    def generateBackgroundFootageImages(self, AudioFileLengthsList, imageFiles, transition_time):
        # Validate inputs
        if not len(AudioFileLengthsList) == len(imageFiles):
            raise ValueError("Input lists must have the same length")

        # Create a list of (image file, duration) tuples
        clips = list(zip(imageFiles, AudioFileLengthsList))

        # Create a sequence of ImageClips
        sequence = [ImageClip(img).set_duration(dur) for img, dur in clips]

        # Add transitions between clips
        videos = []
        for i in range(len(sequence) - 1):
            clip1 = sequence[i]
            clip2 = sequence[i+1].crossfadein(transition_time)
            videos.append(CompositeVideoClip([clip1, clip2.set_start(clip1.duration - transition_time)]))
        videos.append(sequence[-1]) # append last clip without transition

        # Concatenate the clips into a single video
        video = concatenate_videoclips(videos)
        return video
        video.write_videofile("output.mp4")

        return video
        
    '''

    # generates back ground footage based on the inputed times, same for each image
    def generateBackgroundFootageImages(self, imageFiles, total_duration):
        dynamic_clip = DynamicPositionClip(self.framerate, self.bg_width, self.bg_height)

        if not imageFiles:
            raise ValueError("No images to process")

        # Calculate the duration for each image
        image_duration = total_duration / len(imageFiles)
        movement_function = dynamic_clip.LtR_T_E
        clips = []
        for image in imageFiles:
            clip = dynamic_clip.generate_video(image, image_duration, movement_function)
            clips.append(clip.set_duration(image_duration))
        
        # Concatenate all clips to form a sequence
        final_clip = concatenate_videoclips(clips)
        return final_clip
    
    
    def combine_audio_files(self, file_list, output_file):
        # Combine the audio files into a single file
        command = ['ffmpeg', '-y']
        for file in file_list:
            command += ['-i', file]
        command += ['-filter_complex', 'concat=n={}:v=0:a=1'.format(len(file_list)), '-vn', output_file]
        subprocess.run(command)

    def overlay_audio_video(self, video_clip, audio_file_path):
        # Load the audio file
        audio = AudioFileClip(audio_file_path)
        
        # Calculate the duration of silence needed
        silence_duration = video_clip.duration - audio.duration

        # If the audio is longer than the video, we need to cut it
        if audio.duration > video_clip.duration:
            audio = audio.subclip(0, video_clip.duration)
        # If the video is longer than the audio, we need to add silence to the audio
        elif silence_duration > 0:
            # Create a silent audio clip of the required duration
            silence = AudioArrayClip(np.zeros((int(silence_duration * audio.fps), 2)), fps=audio.fps)
            
            # Concatenate the original audio with the silence
            audio = concatenate_audioclips([audio, silence])

        # Set the audio of the video clip
        video_clip = video_clip.set_audio(audio)

        return video_clip

    def add_text_overlay(self, video_clip, text_list):
        clips = []

        for text, start_time, end_time in text_list:
            subclip = video_clip.subclip(start_time, end_time)
            txt_clip = (TextClip(text, fontsize=self.fontsize, color=self.color, transparent=True)
                        .set_position(('center', 'bottom'))
                        .set_start(0)
                        .set_duration(subclip.duration))
            result = CompositeVideoClip([subclip, txt_clip])
            clips.append(result)

        final_clip = concatenate_videoclips(clips)


        return final_clip

    
    def ScriptSplitterV2_times(self, strings , times):
        intervals = []
        current_time = 0
        for i in range(len(strings)):
            interval = [strings[i], current_time, current_time + times[i]]
            intervals.append(interval)
            current_time += times[i]
        return intervals
    


        '''   
    def add_text_overlay(self ,video_path, text_list, output_path):
        # Load the video file
        video = VideoFileClip(video_path)

        # Iterate through the text list and add text to video clip
        for text, start_time, end_time in text_list:
            text_clip = TextClip(text, fontsize=self.fontsize, color=self.color, transparent=True).set_pos('center').set_duration(end_time - start_time).set_start(start_time)
            video = CompositeVideoClip([video, text_clip])

        # Write the new video file with the added text
        video.write_videofile(output_path, codec='libx264')

        # Close the video clip
        video.close()

        return output_path
    '''

'''        
def main():
    video1 = VideoGenerator()
    
    audioFilePath = "VoiceFiles\\"
    imageFilePath = "ImageFiles\\"
    videoFilePath = "VideoFiles\\"
    video1.add_static_image_to_audio( audioFilePath + "script0_0.mp3", imageFilePath + "image0_0.png", videoFilePath + "testvideo1.mp4")
'''
