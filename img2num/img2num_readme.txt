#Pillow 모듈 필요

# 모듈 없을 시 설치 방법
pip install Pillow

#사용법
> python Img2num.py 파일명

출력: 파일명_output.txt

#예

만약 sample.jpg 파일(가로 4, 세로 3)을 숫자로 변환하면 아래와 같이 실행.

 > python Img2num.py sample.jpg

출력 결과는  
sample_output.txt
에 저장되며, 아래와 같이 배열의 형태로 저장 됨.

[[[r,g,b],[r,g,b],[r,g,b],[r,g,b]],
 [[r,g,b],[r,g,b],[r,g,b],[r,g,b]],
 [[r,g,b],[r,g,b],[r,g,b],[r,g,b]]]
 
# jpg 파일만 적용 가능함.