https://phpschool.com/gnuboard4/bbs/board.php?bo_table=qna_db&wr_id=225663&sca=&sfl=mb_id&stx=bihon&sop=and


전체 데이터베이스 백업

C:\>mysqldump -uroot -p비밀번호 -A > D:\backup\all_db.sql

다른 db에 호환되게 백업하기

C:\>C:\>mysqldump -u아이디 -p비밀번호 dbname --compatible=mysql40 > dbname.sql

ps.--compatible 옵션은 mysql 4.1 버전부터 사용할 수 있습니다. 위의 명령을 이전버전인
4.0 버전으로 다운그레이드할 때 사용할 수 있는 옵션입니다. 
실행해본 결과 auto_increment 속성이 없어져 버리므로 나중에 스크립트파일에 직접 추가해야 합니다.