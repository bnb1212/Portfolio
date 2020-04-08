<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	** 상세보기 **
	<br>
	<table>
		<tr>
			<td>id</td>
			<td>${member.id }</td>
		</tr>
		<tr>
			<td>passwd</td>
			<td>${member.passwd }</td>
		</tr>
		<tr>
			<td>name</td>
			<td>${member.name }</td>
		</tr>
		<tr>
			<td>regdate</td>
			<td>${member.regdate }</td>
		</tr>
		<tr>
			<td colspan="2"><a href="list">목록</a>&nbsp;&nbsp; <a
				href="update?id=${member.id }">수정</a>&nbsp;&nbsp; <a
				href="delete?id=${member.id }">삭제</a></td>
		</tr>
	</table>
</body>
</html>