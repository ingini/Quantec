import ftplib
import os


#업로드
filename = "보낼 파일이름"
ftp=ftplib.FTP()
ftp.connect("연결할 IP주소",21)
ftp.login("로그인 아이디","로그인 비밀번호")
ftp.cwd("./")
os.chdir(r"보낼 파일의 위치")
myfile = open(filename,'rb')
ftp.storbinary('STOR ' +filename, myfile )
myfile.close()
ftp.close

#다운로드
filename = "Daily_SecurityReference_2020-01-28.zip"
ftp=ftplib.FTP()
ftp.connect("연결할 IP주소",포트번호)
ftp.login("연결할 아이디","연결할 비밀번호")
ftp.cwd("받아올  파일 위치")
fd = open("./" + filename,'wb')
ftp.retrbinary("RETR " + filename, fd.write)
fd.close()
