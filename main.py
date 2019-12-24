import cv2
import time
import sys
class Spy:
    def __init__(self,vlen):
        self.vlen = vlen
        self.fps = 30
        self.video_len = self.vlen*60*self.fps #10min 60s 20frame
        self.cap = cv2.VideoCapture(0)  # 从摄像头中取得视频
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    def get_frame(self):
        if self.cap.isOpened():
            ret,frame = self.cap.read()
            return ret,frame

    def release(self):
        self.cap.release()
        print('over')


class Writer:
    def __init__(self,fps,width,height,name):
        self.fps, self.width, self.height= fps,width,height
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
        self.out = cv2.VideoWriter(name,self.fourcc, self.fps, (self.width, self.height))

    def write(self,frame):
        self.out.write(frame)

    def release(self):
        self.out.release()


class Shower:
    def __init__(self):
        pass
    def show(self,frame):
        cv2.imshow('SpyOnYou', frame)
        cv2.waitKey(1)
if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("单个视频长度未指定，以分钟为单位。")
        exit()
    else:
        length_per_video = sys.argv[1]
    print("监控开始")
    s = Spy(length_per_video)
    sh = Shower()
    while True:#开启无尽循环
        now = time.localtime()
        path = "{}{:0>2d}{:0>2d}_{:0>2d}{:0>2d}{:0>2d}.mp4".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour,now.tm_min, now.tm_sec)
        path = "./" + path
        # wr = Writer(s.fps, s.width, s.width,path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
        out = cv2.VideoWriter(path, fourcc, s.fps, (s.width, s.height))
        i = 0
        while True:#开启单个视频循环
            ret,frame = s.get_frame()
            sh.show(frame)
            # if ret == True:
            #     wr.write(frame)
            #     i = i + 1
            # if i == s.video_len:
            #     wr.release()
            #     break
            out.write(frame)
            i = i + 1
            if i == s.video_len:
                out.release()
                break