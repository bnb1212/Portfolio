<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h3>** 글쓰기 **</h3>
<form action="insert" method="post">
	글제목 : <input type="text" name="title"><br>
	작성자 : <input type="text" name="author"><br>
	글내용 : <textarea rows="5" cols="30" name="content"></textarea><br>
<br><br>
<input type="submit" value="등록">
</form>
</body>
</html>