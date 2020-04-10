<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="update" method="post">
	글번호 : ${dto.num }<br>
	<input type="hidden" name="num" value="${dto.num }">
	글제목 : <input type="text" name="title" value="${dto.title }"><br>
	작성자 : <input type="text" name="author" value="${dto.author}"><br>
	글내용 : <textarea rows="5" cols="30" name="content">${dto.content }</textarea><br>
<br><br>
<input type="submit" value="등록">
</form>
</body>
</html>