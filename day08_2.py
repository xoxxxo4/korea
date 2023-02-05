import cv2


def ShowImage(img_path): 

    # 이미지 읽어줘
    img = cv2.imread('person.jpg')

    # 이미지 보여줘
    cv2.imshow('title', img)

    # 무한 대기 
    cv2.waitKey(0)

def ShowVideo(video_path):

    # 비다오 읽어줘
    vc = cv2.VideoCapture(video_path)

    # 화면 조정
    vc.set(3, 640)       # 3 : 가로
    vc.set(4, 480)       # 4 : 세로

    # 무한 반복 (동영상 = 빠르게 여러 이미지를 출력)
    while True:
        success, img = vc.read()
        
        # 동영상을 성공적으로 읽었으면
        if success:
            cv2.imshow('title', img)
        if cv2.waitKey(20) & 0xFF == 27:
            # ESC키를 눌러 종료
            break


# ShowImage('person.jpg')
# ShowVideo('person.mp4')
# ShowCam() (ShowVideo 대신 ShowCam으로 입력)