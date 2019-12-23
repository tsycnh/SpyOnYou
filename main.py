import cv2
import time
class Spy:
    def __init__(self,vlen):
        self.vlen = vlen
        self.fps = 30
        self.video_len = self.vlen*60*self.fps #10min 60s 20frame
        self.cap = cv2.VideoCapture(0)  # 从摄像头中取得视频
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
    def one_video(self,name):
        out = cv2.VideoWriter(name,self.fourcc, self.fps, (self.width, self.height))
        i =0

        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret == True:
                out.write(frame)
                i=i+1
            if i == self.video_len:
                break

        out.release()
        print(name," saved")
    def release(self):
        self.cap.release()
        print('over')
    def start(self):
        while True:
            now = time.localtime()
            path = "{}{:0>2d}{:0>2d}_{:0>2d}{:0>2d}{:0>2d}.mp4".format(now.tm_year,now.tm_mon,now.tm_mday,now.tm_hour,now.tm_min,now.tm_sec)
            path = "./"+path
            self.one_video(path)

s = Spy(10)
s.start()