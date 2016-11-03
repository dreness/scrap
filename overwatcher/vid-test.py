# import numpy
# import sys
import argparse
import cv2
from os.path import abspath
from skimage.measure import structural_similarity as ssim

frameInterval = 1
startFrame = 1
blitTime = 16

# short
# v = "D:\shadowplay\Overwatch\Overwatch 10.22.2016 - 23.15.35.07.mp4"
# long
# v = "D:\shadowplay\Overwatch\Overwatch 10.23.2016 - 00.14.27.08.mp4"
# fire @ 14:30
# v = 'D:\\shadowplay\\Overwatch\\Overwatch 10.23.2016 - 05.07.32.15.mp4'

parser = argparse.ArgumentParser(description='Analyze Overwatch game recordings')
parser.add_argument('--video', dest='video', help='video file to process',
                    required=True)

args = parser.parse_args()

if args.video:
    v = args.video
else:
    v = "test.mp4"

p = abspath(v)
print "trying to open {}\n".format(p)
cap = cv2.VideoCapture(p)
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    count = count + 1
    if frame is None:
        print "Got empty frame, bailing... (processed {} frames)".format(count)
        exit(0)
    if count < startFrame:
        continue
    if count % frameInterval != 0:
        continue
    # grab just the player health bar
    roi = frame[1020:1125, 240:500] #  [Y1:Y2, X1:X2]

    # set all green and red pixels in roi to zero
    # roi[:,:,(1,2)] = 0

    # how much blue is there?
    # print "sum of all blue in ROI frame: {}".format(roi.sum())

    cv2.imshow("roi", roi)
    if cv2.waitKey(blitTime) & 0xFF == ord('q'):
        break

print 'closing, processed {} frames'.format(count)
cap.release()
cv2.destroyAllWindows()
