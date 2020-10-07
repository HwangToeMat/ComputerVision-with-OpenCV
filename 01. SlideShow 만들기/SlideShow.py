import sys
import glob
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--img_dir', default='image', type=str)
parser.add_argument('--screen', default='full', type=str)
parser.add_argument('--delay', default=2, type=int)
args = parser.parse_args()


def run(img_dir='image', screen='full', delay=2):

    img_lst = glob.glob('.\\{}\\*.jpg'.format(img_dir))

    if not img_lst:
        print("There are no jpg files in 'image' folder")
        sys.exit()

    if screen == 'full':
        # 전체 화면
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(
            'image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    elif screen == 'window':
        # 창 화면
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    cnt = len(img_lst)
    idx = 0
    delay *= 1000

    while True:
        img = cv2.imread(img_lst[idx])

        if img is None:
            print('Image load failed!')
            break

        cv2.imshow('image', img)
        if cv2.waitKey(delay) >= 0:
            break

        idx += 1
        if idx >= cnt:
            idx = 0

    cv2.destroyAllWindows()


if __name__ == '__main__':
    run(args.img_dir, args.screen, args.delay)
