from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip

class DynamicPositionClip:
    def __init__(self, framerate, bg_width, bg_height):
        self.framerate = framerate
        self.frame_width = bg_width
        self.frame_height = bg_height

    def linearTimeGraph(self, total_time, image_size, current_time, initial_x):
        return (image_size / total_time) * current_time + initial_x
    
    def exponentialTimeGraph(self, total_time, image_size, current_time, initial_x):
        return (image_size / total_time**3) * (current_time**3) + initial_x
    
    def dynamicPosition(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-x, 0)
    
    # Left to Right movement
    def LtR_top_expo(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        return (-x, 0)
    
    def LtR_mid_expo(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        return (-x, -(image_height - self.frame_height)/2)
    
    def LtR_bot_expo(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        return (-x, -(image_height - self.frame_height))
    
    # Right to Left movement
    def RtL_top_expo(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, -(image_width - self.frame_width))
        return (x, 0)
        
    def RtL_mid_expo(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, -(image_width - self.frame_width))
        return (x, -(image_height - self.frame_height)/2)
        
    def RtL_bot_expo(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, -(image_width - self.frame_width))
        return (x, -(image_height - self.frame_height))


    # Top to Bottom movement
    def TtB_left_expo(self, t, clip_duration, image_width, image_height):
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (0, -y)
        
    def TtB_center_expo(self, t, clip_duration, image_width, image_height):
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-(image_width - self.frame_width) / 2, -y)
        
    def TtB_right_expo(self, t, clip_duration, image_width, image_height):
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-(image_width - self.frame_width), -y)
    
    # Top Left to Bottom Right
    def LtR_TtB(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-x, -y)
    
    # Top Right to Bottom Left
    def RtL_TtB(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (x, -y)
    
    #Bottom Left to Top Right
    def LtR_BtT(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-x, y)
    
    # Bottom Right to Top Left
    def RtL_BtT(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (x, y)
    
    def positionTest(self, t):
        return (0, 0)
    
    def generate_video(self, image_path, clip_duration, output_path):
        clip = ImageClip(image_path).set_duration(clip_duration)
        image_width, image_height = clip.size
        bg_clip = ColorClip(size=(self.frame_width, self.frame_height), color=(0, 0, 0)).set_duration(clip_duration)
        
        #clip = clip.set_position(self.positionTest)
        clip = clip.set_position(lambda t: self.RtL_mid_expo(t, clip_duration, image_width, image_height))
        composite = CompositeVideoClip([bg_clip, clip])
        composite.write_videofile(output_path, fps=self.framerate)

if __name__ == '__main__':
    FRAMERATE = 24
    BG_WIDTH = 1080
    BG_HEIGHT = 1920
    clip_duration = 5
    image_path = "/home/kevin/Desktop/PARSE/VMAC/ImageQuerry/1367px-Fawn_and_white_Welsh_Corgi_puppy_standing_on_rear_legs_and_sticking_out_the_tongue.jpg"
    output_path = "RtL_mid_expo.mp4"

    dynamic_clip = DynamicPositionClip(FRAMERATE, BG_WIDTH, BG_HEIGHT)
    dynamic_clip.generate_video(image_path, clip_duration, output_path)
