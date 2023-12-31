from moviepy.editor import ImageClip, ColorClip, CompositeVideoClip

class DynamicPositionClip:
    def __init__(self, framerate, bg_width, bg_height):
        self.framerate = framerate
        self.frame_width = bg_width
        self.frame_height = bg_height
    
    def linearTimeGraph(total_time, image_size, current_time, initial_x):
        return (image_size / total_time) * current_time + initial_x
    
    def exponentialTimeGraph(self, total_time, travel_distance, current_time, initial_x):
        return (travel_distance / total_time**3) * (current_time**3) + initial_x
    def dynamicPosition(self, t, clip_duration, image_width, image_height):
        x = self.exponentialTimeGraph(clip_duration, image_width - self.frame_width, t, 0)
        y = self.exponentialTimeGraph(clip_duration, image_height - self.frame_height, t, 0)
        return (-x, 0)

    def generate_video(self, image_path, clip_duration, output_path):
        clip = ImageClip(image_path).set_duration(clip_duration)
        image_width, image_height = clip.size
        bg_clip = ColorClip(size=(self.frame_width, self.frame_height), color=(0, 0, 0)).set_duration(clip_duration)
        
        #clip = clip.set_position(self.positionTest)
        clip = clip.set_position(lambda t: self.dynamicPosition(t, clip_duration, image_width, image_height))
        composite = CompositeVideoClip([bg_clip, clip])
        composite.write_videofile(output_path, fps=self.framerate)

if __name__ == '__main__':
    FRAMERATE = 24
    BG_WIDTH = 1080
    BG_HEIGHT = 1920
    clip_duration = 5
    image_path = "/home/kevin/Desktop/PARSE/VMAC/ImageQuerry/1367px-Fawn_and_white_Welsh_Corgi_puppy_standing_on_rear_legs_and_sticking_out_the_tongue.jpg"
    output_path = "RtL_mid_expo.mp4"
    all_possibilities = ['LtR_TtB_E', 'LtR_TtB_L', 'LtR_BtT_E', 'LtR_BtT_L', 'LtR_T_E', 'LtR_T_L', 'LtR_M_E', 'LtR_M_L', 'LtR_B_E', 'LtR_B_L', 'RtL_TtB_E', 'RtL_TtB_L', 'RtL_BtT_E', 'RtL_BtT_L', 'RtL_T_E', 'RtL_T_L', 'RtL_M_E', 'RtL_M_L', 'RtL_B_E', 'RtL_B_L', 'L_TtB_E', 'L_TtB_L', 'L_BtT_E', 'L_BtT_L', 'L_T_E', 'L_T_L', 'L_M_E', 'L_M_L', 'L_B_E', 'L_B_L', 'C_TtB_E', 'C_TtB_L', 'C_BtT_E', 'C_BtT_L', 'C_T_E', 'C_T_L', 'C_M_E', 'C_M_L', 'C_B_E', 'C_B_L', 'R_TtB_E', 'R_TtB_L', 'R_BtT_E', 'R_BtT_L', 'R_T_E', 'R_T_L', 'R_M_E', 'R_M_L', 'R_B_E', 'R_B_L']
    
    dynamic_clip = DynamicPositionClip(FRAMERATE, BG_WIDTH, BG_HEIGHT)
    dynamic_clip.generate_video(image_path, clip_duration, output_path)
