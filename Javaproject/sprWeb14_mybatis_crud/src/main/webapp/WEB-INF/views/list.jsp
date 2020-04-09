<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h3>회원정보(@MVC - MyBatis(CRUD))</h3>
	<a href="insert">회원추가</a>

	<br>
	<table border="1">
		<tr>
			<th>번호</th>
			<th>이름</th>
			<th>주소</th>
			<th>변경</th>
		</tr>
		<c:forEach var="s" items="${list }">
			<tr>
				<td>${s.num }</td>
				<td>${s.name }</td>
				<td>${s.addr }</td>
				<td><a href="update?num=${m.num }">수정</a> /
				<a href="delete?num=${m.num }">삭제</a>
				</td>
			</tr>

		</c:forEach>

	</table>

</body>
</html>