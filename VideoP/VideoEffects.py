from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip
import cv2
import numpy as np


class DynamicPositionClip:
    def __init__(self, framerate, bg_width, bg_height):
        self.framerate = framerate
        self.frame_width = bg_width
        self.frame_height = bg_height
    
    def linearTimeGraph(total_time, image_size, current_time, initial_x):
        return (image_size / total_time) * current_time + initial_x
    
    def exponentialTimeGraph(self, total_time, image_size, current_time, initial_x):
        return (image_size / total_time**3) * (current_time**3) + initial_x
    
    def dynamicPosition(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-x, 0)
    
    # Left to Right movement
    def LtR_T_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        return (-x, 0)
    
    def LtR_M_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        return (-x, -(image_height - self.frame_height)/2)
    
    def LtR_B_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        return (-x, -(image_height - self.frame_height))
    
    # Right to Left movement
    def RtL_T_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, -(image_width - self.frame_width))
        return (x, 0)
        
    def RtL_M_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, -(image_width - self.frame_width))
        return (x, -(image_height - self.frame_height)/2)
        
    def RtL_B_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, -(image_width - self.frame_width))
        return (x, -(image_height - self.frame_height))


    # Top to Bottom movement
    def TtB_L_E(self, t, clip_duration, image_width, image_height):
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (0, -y)
        
    def TtB_C_E(self, t, clip_duration, image_width, image_height):
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-(image_width - self.frame_width) / 2, -y)
        
    def TtB_R_E(self, t, clip_duration, image_width, image_height):
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-(image_width - self.frame_width), -y)
    
    # Top Left to Bottom Right
    def LtR_TtB_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-x, -y)
    
    # Top Right to Bottom Left
    def RtL_TtB_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (x, -y)
    
    #Bottom Left to Top Right
    def LtR_BtT_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-x, y)
    
    # Bottom Right to Top Left
    def RtL_BtT_E(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (x, y)
    
    def positionTest(self, t):
        return (0, 0)
    
    def dynamicMotionX(self, t, clip_duration, travelLength):
        x = self.exponentialTimeGraph(clip_duration, travelLength, t, 0)
        return x
    def motionSelection(t, MovementString, clip_duration, image_width, image_height):





        

class VideoEffects(DynamicPositionClip):
    def __init__(self, framerate, bg_width, bg_height):
        super().__init__(framerate, bg_width, bg_height)

    def apply_opencv_effects(self, img, t, total_duration):
        # Varying contrast for demonstration
        # You can replace this with any other OpenCV effect
        alpha = 1 + 0.5 * (t / total_duration)  # Scale factor [1, 1.5]
        img_contrast = cv2.convertScaleAbs(img, alpha=alpha, beta=0)
        
        return img_contrast

    def generate_videclip(self, image_path, clip_duration, output_path):
        # Create a static ImageClip
        static_img = cv2.imread(image_path)
        static_img_rgb = cv2.cvtColor(static_img, cv2.COLOR_BGR2RGB)
        
        # Create an ImageClip with dynamic position
        clip = ImageClip(np.array(static_img_rgb)).set_duration(clip_duration)
        image_width, image_height = clip.size
        clip = clip.set_position(lambda t: self.RtL_mid_expo(t, clip_duration, image_width, image_height))
        
        # Apply OpenCV effects to each frame of the positioned clip  
        clip = clip.fl(lambda gf, t: self.apply_opencv_effects(gf(t), t, clip_duration))

        # Create background and composite clips
        bg_clip = ColorClip(size=(self.frame_width, self.frame_height), color=(0, 0, 0)).set_duration(clip_duration)
        composite = CompositeVideoClip([bg_clip, clip])
        
        composite.write_videofile(output_path, fps=self.framerate)

if __name__ == '__main__':
    FRAMERATE = 24
    BG_WIDTH = 1080
    BG_HEIGHT = 1920
    clip_duration = 5
    image_path = "/home/kevin/Desktop/PARSE/VMAC/ImageQuerry/1367px-Fawn_and_white_Welsh_Corgi_puppy_standing_on_rear_legs_and_sticking_out_the_tongue.jpg"
    output_path = "RtL_mid_expo.mp4"
    dynamic_clip = VideoEffects(FRAMERATE, BG_WIDTH, BG_HEIGHT)
    dynamic_clip.generate_video(image_path, clip_duration, output_path)
