import cv2
import time
import os
import sys

def main(mode, save_path, people):

    number_of_pose = 5

    arr_a = ['pose_%02d' % i for i in range(number_of_pose)]
    arr_b = ['pattern_0', 'pattern_1', 'pattern_2', 'pattern_3', 'pattern_4']

    # mkdirs
    if not os.path.exists(save_path + '/' + people):

        os.mkdir(save_path + '/' + people)

        for i in arr_a:
            for j in arr_b:
                os.makedirs(save_path + '/' + people + '/' + i + '/' + j)

        print("mkdir success: ", save_path + '/' + people)
    else:
        print("mkdir failed: ", save_path + '/' + people)
        return 0

    # 连接外接webcamera
    cap_0 = cv2.VideoCapture(0)
    # 设置视频参数
    cap_0.set(3, 1024)
    cap_0.set(4, 768)
    cap_0.set(5, 30)

    if mode == 'experiment':
        cap_1 = cv2.VideoCapture(1)
        # 设置视频参数
        cap_1.set(3, 1024)
        cap_1.set(4, 768)
        cap_1.set(5, 30)

        cap_2 = cv2.VideoCapture(2)
        # 设置视频参数
        cap_2.set(3, 1024)
        cap_2.set(4, 768)
        cap_2.set(5, 30)

    i = 0
    j = 0

    print('Step: ' + arr_a[i] + ' ' + arr_b[j])

    # 读取视频
    # 读取视频帧
    while True:

        ret, frame_0 = cap_0.read()
        cv2.imshow("camera_0", frame_0)

        if mode == 'experiment':
            ret, frame_1 = cap_1.read()
            cv2.imshow("camera_1", frame_1)

            ret, frame_2 = cap_2.read()
            cv2.imshow("camera_2", frame_2)


        # 按下A之后拍摄照片，并保存。图片的名为时间
        if cv2.waitKey(1) & 0xFF == ord('a'):
            time_now = time.strftime("%Y-%m%d-%H%M%S", time.localtime())

            cv2.imwrite(save_path + '/' + people + '/' + arr_a[i] + '/' + arr_b[j] + '/' + time_now + '_0.jpg', frame_0)

            if mode == 'experiment':
                cv2.imwrite(save_path + '/' + people + '/' + arr_a[i] + '/' + arr_b[j] + '/' + time_now + '_1.jpg', frame_1)
                cv2.imwrite(save_path + '/' + people + '/' + arr_a[i] + '/' + arr_b[j] + '/' + time_now + '_2.jpg', frame_2)

            j += 1

            if j == 5:
                j = 0
                i += 1

            if i == 5:
                break


            print("save success")
            print('Step: ' + arr_a[i] + ' ' + arr_b[j])


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # 保存视频
        # cv2.imwrite("test.jpg", frame)
        # 释放资源

    cap_0.release()
    if mode == 'experiment':
        cap_1.release()
        cap_2.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    save_path = '/Users/songminglun/Library/Mobile Documents/com~apple~CloudDocs/01_Documents/ILCS_2023/10-30/img'

    if len(sys.argv) != 2:
        print("Usage: python camera.py <people>")
        sys.exit(1)

    people = sys.argv[1]

    main(mode='test', save_path=save_path, people=people)