import cv2
import time

def main(mode, save_path):

    # 连接外接webcamera
    cap_0 = cv2.VideoCapture(0)

    if mode == 'experiment':
        cap_1 = cv2.VideoCapture(1)
        cap_2 = cv2.VideoCapture(2)

    # 设置视频参数
    cap_0.set(3, 640)
    cap_0.set(4, 480)
    cap_0.set(5, 30)
    # 读取视频
    # 读取视频帧
    while True:
        ret, frame = cap_0.read()
        cv2.imshow("frame", frame)

        # 按下A之后拍摄照片，并保存。图片的名为时间
        if cv2.waitKey(1) & 0xFF == ord('a'):
            time_now = time.strftime("%Y-%m%d-%H%M%S", time.localtime())
            cv2.imwrite(save_path + '/' + time_now + ".jpg", frame)
            print("save success")

            

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # 保存视频
        # cv2.imwrite("test.jpg", frame)
        # 释放资源
    cap_0.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(mode='test', save_path='/Users/songminglun/Library/Mobile Documents/com~apple~CloudDocs/01_Documents/ILCS_2023/10-30/img')