<%@page import="pack.business.DataDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="bean" class="pack.business.DataDto"/>
<jsp:useBean id="buserProcess" class="pack.business.BuserProcess"/>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"  %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h3>부서정보</h3>
	<table border="1">
		<tr>
			<th>번호</th>
			<th>부서명</th>
			<th>전화</th>
		</tr>
		<%
			ArrayList<DataDto> list = (ArrayList<DataDto>) buserProcess.selectDataAll();
		%>
		<c:set var="list" value="<%=list%>" />
		<c:if test="${empty list}">
			<tr>
				<td colspan="자료 없음"></td>
			</tr>
		</c:if>
		<c:forEach var="m" items="<%=list%>">
			<tr>
				<td>${m.buser_no}</td>
				<td>${m.buser_name}</td>
				<td>${m.buser_tel}</td>
			</tr>
		</c:forEach>
		<tr>
			<td colspan="3">건수 : <%=list.size() %></td>
		</tr>
	</table>
</body>
</html>