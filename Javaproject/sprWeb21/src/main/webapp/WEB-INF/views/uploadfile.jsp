<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
* 업로드된 파일 정보 *<br>
파일명 : ${filename } 
<hr>
<form action="download" method="post">
<input type="hidden" name="filename" value="${filename }">
<input type="submit" value="현재파일 다운로드하기">
</form>
</body>
</html>