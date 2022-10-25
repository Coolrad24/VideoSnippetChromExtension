import video_tool as vt


class VideoEngine:
    def __init__(self):
        pass


    def cut_video(self,st,sp, video_file):
        
        final_video_file = vt.cut_video(video_file=video_file, start=st,
                                        end=sp)
        return final_video_file
