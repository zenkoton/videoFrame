import os
import cv2


source_path = "./source/"

# 将输入视频提取出帧输出到
def frame(inpath,interval=10):
    cam = cv2.VideoCapture(inpath)
    dir_name = os.path.join("output",os.path.basename(inpath))
    try:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
    except:
        print("error make outputdir")   

    n = 0 # n代表技术器
    count = 0

    while(True):
        ret,frame = cam.read()

        if ret:
            if n%interval==0:
                name = os.path.join(dir_name,os.path.basename(inpath)+str(count)+'.jpg')
                cv2.imwrite(name,frame)
                count = count+1
            n = n+1 
        else:
            break
    cam.release()


if __name__=='__main__':
    videos = []
    for root , dirs , names in os.walk(source_path):
        for name in names:
            ext = os.path.splitext(name)[1]
            if ext == '.mp4':
                videos.append(os.path.join(root,name))  # 将mp4存储到list中
    

    for video in videos:
        frame(video)