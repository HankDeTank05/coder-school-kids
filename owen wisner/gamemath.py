import math

def clamp(range_min, range_max, val_to_clamp):
    if val_to_clamp<range_min:
        return range_min
    elif val_to_clamp>range_max:
        return range_max
    else:
        return val_to_clamp

def intersect_circle_rect(circle_x, circle_y, circle_r, rect_x, rect_y, rect_w, rect_h):
    # step 1: clamp center in rect
    clamp_center_x=clamp(rect_x, rect_x+rect_w, circle_x)
    clamp_center_y=clamp(rect_y, rect_y+rect_h, circle_y)
    
    #step 2: get distance between clamped point and circle center
    x_dist=clamp_center_x-circle_x
    y_dist=clamp_center_y-circle_y
    distance=math.sqrt(x_dist**2+y_dist**2)

    #step 3: return true if collision and false if not
    return distance<=circle_r
    
