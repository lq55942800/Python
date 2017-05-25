#coding=utf-8

def make_readable(seconds):
    Max_time = 359999
    MM = 0
    HH = 0
    SS = 0
    if seconds>=0 and seconds<=59:
        SS = seconds
        return ('00:00:%02d'%(SS))
    elif seconds>59 and seconds<=3599:
        SS = seconds%60
        MM = (seconds-SS)/60
        return ('00:%02d:%02d'%(MM,SS))
    elif seconds<=359999:
        SS = seconds%60
        MM = (seconds-SS)%3600/60
        HH = (seconds-SS-MM*60)/3600
        return ('%02d:%02d:%02d'%(HH,MM,SS))
    else:
        return ("Wrong second.")

#
# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)