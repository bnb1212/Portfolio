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
	<h3>직원 자료 출력</h3>
	<table border='1'>
		<tr>
			<th>사번</th>
			<th>이름</th>
			<th>부서명</th>
			<th>직급</th>
			<th>입사년</th>
			
		</tr>
		<c:forEach var="s" items="${datas }">
			<tr>
				<td>${s.jikwon_no }</td>
				<td><a href="gogeklist?no=${s.jikwon_no}" target="gogeklist_view">${s.jikwon_name }</a></td>
				<td>${s.buser_name }</td>
				<td>${s.jikwon_jik }</td>
				<td>${s.jikwon_ibsail }</td> <!-- getJikwon_ibsail -->
			</tr>
		</c:forEach>
	</table>
	<iframe name="gogeklist_view" style="width:40%; height:300px" frameBorder="0">
	</iframe>
</body>
</html>