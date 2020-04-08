<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
** 자료 수정 ** <br>
<form action="update" method="post">
	아이디  : ${updata.id }
	<input type="hidden" name="id" value="${updata.id}">
	<br>
	회원명 : <input type="hidden" name="name" value="${updata.id}">
	비밀번호 : <input type="text" name="passwd" value="${updata.passwd }">
	<br>
	<input type="submit" value="수정완료">
	<br>
</form>
</body>
</html>