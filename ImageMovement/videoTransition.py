from moviepy.editor import * 

def linearTimeGraph(total_time, image_size, current_time, initial_x):
    return (image_size/total_time) * (current_time) + initial_x
def exponentialTimeGraph(total_time, image_size, current_time, initial_x):
    return (image_size/total_time**3) * (current_time**3) + initial_x

def dynamic_position(t, width, height, FRAMERATE, clip_durration):
    x = exponentialTimeGraph(clip_durration, width, t, 0)
    y = exponentialTimeGraph(clip_durration, height, t, 0)
    return (x, 0)
    # (x, 0 ) makes the x value change and keeps they value the same so that the image slides right

image_path = "/home/kevin/Desktop/PARSE/VMAC/ImageQuerry/1367px-Fawn_and_white_Welsh_Corgi_puppy_standing_on_rear_legs_and_sticking_out_the_tongue.jpg"
FRAMERATE = 24
clip_durration = 5
clip = ImageClip(image_path).set_duration(clip_durration)

width, height = clip.size
print(f"Width: {width}, Height: {height}")


bg_clip = ColorClip(size=(1920,1920), color=(0, 0, 0)).set_duration(clip_durration)

clip = clip.set_position(lambda t: dynamic_position(t, width, height, FRAMERATE, clip_durration)) # time is automatically passed in as a parameter
composite = CompositeVideoClip([bg_clip, clip])
composite.write_videofile("imagetest_edge_to_edge.mp4", fps=FRAMERATE)

