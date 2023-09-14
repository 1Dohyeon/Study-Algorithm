import datetime #datatime모듈을 이용해 현재 시간을 가져옴
print(str(datetime.datetime.now())[:10]) 
# now() 함수를 사용해 지금의 날짜, 시간을 출력
# str() 함수를 사용해 출력하려는 내용을 string 형태로 출력
# [:10]를 사용해 10글자만 출력하도록 하여 년, 월, 일만 출력하도록  함