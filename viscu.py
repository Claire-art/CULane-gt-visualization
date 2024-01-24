import cv2
import numpy as np
import os
import glob

def draw_lane(image, lines):
    # 좌표에 따라 차선 그리기
    for line in lines:
        for i in range(len(line) - 1):
            start_point = (int(line[i][0]), int(line[i][1]))
            end_point = (int(line[i + 1][0]), int(line[i + 1][1]))
            cv2.line(image, start_point, end_point, (0, 255, 0), 2)

    return image

def read_coords(txt_path):
    # .txt 파일에서 차선 좌표 읽기
    lines = []
    with open(txt_path, 'r') as file:
        for line in file:
            coords = line.strip().split()
            line_coords = []
            for i in range(0, len(coords), 2):
                x, y = float(coords[i]), float(coords[i + 1])
                if y > 0:  # 유효한 좌표인 경우에만 추가
                    line_coords.append((x, y))
            lines.append(line_coords)
    return lines

def process_images(input_folder, output_folder):
    # input_folder 내의 모든 .jpg 파일을 검색
    for image_path in glob.glob(os.path.join(input_folder, '*.jpg')):
        base_name = os.path.basename(image_path)
        txt_path = os.path.join(input_folder, base_name.replace('.jpg', '.lines.txt'))

        # .lines.txt 파일이 있는지 확인
        if os.path.exists(txt_path):
            image = cv2.imread(image_path)
            lines = read_coords(txt_path)
            lane_image = draw_lane(image, lines)

            # output 폴더에 결과 저장
            output_path = os.path.join(output_folder, base_name)
            cv2.imwrite(output_path, lane_image)

# 폴더 경로
input_folder = '/home/jua/다운로드/CULane/driver_37_30frame/05191714_0507.MP4/'
output_folder = '/home/jua/cu20/'

# 처리 함수 호출
process_images(input_folder, output_folder)

# 이미지와 좌표 파일 경로
# image_path = '/home/jua/다운로드/CULane/driver_37_30frame/05181432_0203.MP4/02520.jpg'
#txt_path = '/home/jua/다운로드/CULane/driver_37_30frame/05181432_0203.MP4/02520.lines.txt'

