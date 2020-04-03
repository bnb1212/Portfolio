
<%@page import="pack.company.DataDto2"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<jsp:useBean id="processDao2" class="pack.company.ProcessDao2" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>메인</title>
</head>
<body>
	직원 자료 :
	<br>
	<%
		ArrayList<DataDto2> list = (ArrayList) processDao2.selectJikDataAll();
	%>
	<table border="1">
		<tr>
			<th>사번</th>
			<th>이름</th>
			<th>직급</th>
			<th>성별</th>
			<th>급여</th>
		</tr>
		<c:forEach var="s" items="<%=list%>">
			<tr>
				<td>${s.jikwon_no}</td>
				<td>${s.jikwon_name}</td>
				<td>${s.jikwon_jik}</td>
				<td>${s.jikwon_gen}</td>
				<td>${s.jikwon_pay}</td>
			</tr>
		</c:forEach>
		<tr>
			<td colspan="5">인원수 : <%=list.size()%>명
			</td>
		</tr>
	</table>
	<hr>
	<%
		ArrayList<DataDto2> list2 = (ArrayList) processDao2.selectDataPart();
	%>
	<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
	<table border="1">
		<tr>
			<th>직급별</th>
			<th>인원수</th>
			<th>급여합</th>
			<th>급여평균</th>
		</tr>
		<c:forEach var="s" items="<%=list2%>">
			<tr>
				<td>${s.jikwon_jik}</td>
				<td>${s.jikwon_count}</td>
				<td><fmt:formatNumber value="${s.pay_sum}" type="number" pattern="0"/></td>
				<td><fmt:formatNumber value="${s.pay_avg}" type="number" pattern="#"/></td>
			</tr>
		</c:forEach>
	</table>
</body>
</html>