from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip

class DynamicPositionClip:
    def __init__(self, framerate, bg_width, bg_height):
        self.framerate = framerate
        self.frame_width = bg_width
        self.frame_height = bg_height
    
    def linearTimeGraph(self, total_time, image_size, current_time, initial_x):
        return (image_size / total_time) * current_time + initial_x
    
    def exponentialTimeGraph(self, total_time, travel_distance, current_time, initial_x):
        return (travel_distance / total_time**3) * (current_time**3) + initial_x
    
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
    
    def generate_video(self, image_path, clip_duration, movement_function, output_path=None):
        clip = ImageClip(image_path).set_duration(clip_duration)
        image_width, image_height = clip.size
        bg_clip = ColorClip(size=(self.frame_width, self.frame_height), color=(0, 0, 0)).set_duration(clip_duration)
        
        # Use the passed-in movement_function to set the clip's position
        clip = clip.set_position(lambda t: movement_function(t, clip_duration, image_width, image_height))
        composite = CompositeVideoClip([bg_clip, clip])
        return composite
        #composite.write_videofile(output_path, fps=self.framerate)

if __name__ == '__main__':
    FRAMERATE = 24
    BG_WIDTH = 1080
    BG_HEIGHT = 1920
    clip_duration = 5
    image_path = "/home/kevin/Desktop/PARSE/VMAC/ImageQuerry/1367px-Fawn_and_white_Welsh_Corgi_puppy_standing_on_rear_legs_and_sticking_out_the_tongue.jpg"
    output_path = "RtL_mid_expo.mp4"
    all_possibilities = ['LtR_TtB_E', 'LtR_TtB_L', 'LtR_BtT_E', 'LtR_BtT_L', 'LtR_T_E', 'LtR_T_L', 'LtR_M_E', 'LtR_M_L', 'LtR_B_E', 'LtR_B_L', 'RtL_TtB_E', 'RtL_TtB_L', 'RtL_BtT_E', 'RtL_BtT_L', 'RtL_T_E', 'RtL_T_L', 'RtL_M_E', 'RtL_M_L', 'RtL_B_E', 'RtL_B_L', 'L_TtB_E', 'L_TtB_L', 'L_BtT_E', 'L_BtT_L', 'L_T_E', 'L_T_L', 'L_M_E', 'L_M_L', 'L_B_E', 'L_B_L', 'C_TtB_E', 'C_TtB_L', 'C_BtT_E', 'C_BtT_L', 'C_T_E', 'C_T_L', 'C_M_E', 'C_M_L', 'C_B_E', 'C_B_L', 'R_TtB_E', 'R_TtB_L', 'R_BtT_E', 'R_BtT_L', 'R_T_E', 'R_T_L', 'R_M_E', 'R_M_L', 'R_B_E', 'R_B_L']
    
    dynamic_clip = DynamicPositionClip(FRAMERATE, BG_WIDTH, BG_HEIGHT)
    movement_function = dynamic_clip.LtR_T_E  # You can dynamically set this to any other function like dynamic_clip.RtL_M_E
    dynamic_clip.generate_video(image_path, clip_duration, movement_function)