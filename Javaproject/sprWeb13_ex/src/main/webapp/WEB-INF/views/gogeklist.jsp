<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="f" uri="http://java.sun.com/jsp/jstl/functions"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h3>고객 정보 출력</h3>
	<table border='1'>
		<tr>
			<th>고객번호</th>
			<th>고객명</th>
			<th>성별</th>
			<th>전화</th>
		</tr>
		<c:forEach var="s" items="${gogeks }">
			<tr>
				<td>${s.gogek_no }</td>
				<td>${s.gogek_name }</td>
				<td>${s.gogek_jumin }</td>
				<td>${s.gogek_tel }</td>
			</tr>
		</c:forEach>
		<tr>
			<td colspan="4">인원수 : ${f:length(gogeks) }</td>
		</tr>
	</table>
</body>
</html>