<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
** 요청 파라미터 연습 ** <br>
<a href="kbs/login?type=admin">관리자</a><br>
<a href="kbs/login?type=user">일반인</a><br>
<a href="kbs/login">파라미터 없음</a><br>
<br>
<form action="kbs/login" method="post">
data : <input type="text" name="type">
		<input type="submit" value="전송1">
</form>
<form action="kbs/korea" method="post">
data : <input type="text" name="type">
		<input type="submit" value="전송2">
</form>
<form action="kbs/asia" method="post">
data : <input type="text" name="type">
		<input type="submit" value="전송3">
</form>
<hr>
<form action="ent/sm/singer/redvelvet">
신곡 : <input type="text" name="title" value="빨간맛">
<input type="submit">
</form>
<form action="ent/jyp/singer/twice">
신곡 : <input type="text" name="title" value="노란맛">
<input type="submit">
</form>

</body>
</html>