     
def linearTimeGraph(total_time, image_size, current_time, initial_x):
    return (image_size / total_time) * current_time + initial_x

def exponentialTimeGraph( total_time, image_size, current_time, initial_x):
    return (image_size / total_time**3) * (current_time**3) + initial_x

def dynamicMotionX( t, motionString, total_time, travel_distance, initial_x):
    #LtR_TtB_E
    # total_time, travel_distance, current_time, initial_x
    motionlist = motionString.split("_")
    print(motionlist)
    motionTestX = False
    motionTestY = False
    motionTest = list(motionlist[0])
    if ("t" in motionTest):
        motionTestX = True
    motionTest = list(motionlist[1])
    if ("t" in motionTest):
        motionTestY = True
    # tested for motion

    # motionlist[0] == R L or C
    if not(motionTestX):
        if (motionlist[0] == "L"):
            travel_distanceX = 0
        elif (motionlist[0] == "R"):
            travel_distanceX = 0

    x = exponentialTimeGraph(total_time, travel_distanceX, current_time, initial_x)




# {Direction}_{Position}_{TimeGraph}
all_possibilities = ['LtR_TtB_E', 'LtR_TtB_L', 'LtR_BtT_E', 'LtR_BtT_L', 'LtR_T_E', 'LtR_T_L',
                     'LtR_M_E', 'LtR_M_L', 'LtR_B_E', 'LtR_B_L', 'RtL_TtB_E', 'RtL_TtB_L', 
                     'RtL_BtT_E', 'RtL_BtT_L', 'RtL_T_E', 'RtL_T_L', 'RtL_M_E', 'RtL_M_L', 
                     'RtL_B_E', 'RtL_B_L', 'L_TtB_E', 'L_TtB_L', 'L_BtT_E', 'L_BtT_L', 
                     'L_T_E', 'L_T_L', 'L_M_E', 'L_M_L', 'L_B_E', 'L_B_L', 'C_TtB_E', 
                     'C_TtB_L', 'C_BtT_E', 'C_BtT_L', 'C_T_E', 'C_T_L', 'C_M_E', 'C_M_L', 
                     'C_B_E', 'C_B_L', 'R_TtB_E', 'R_TtB_L', 'R_BtT_E', 'R_BtT_L', 'R_T_E', 
                     'R_T_L', 'R_M_E', 'R_M_L', 'R_B_E', 'R_B_L']

dynamicMotionX(1.1, all_possibilities[0], 5, 20, 3)

