<%@page import="pack.business.MemberProcess"%>
<%@page import="pack.business.DataDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="func" uri="http://java.sun.com/jsp/jstl/functions"%>

<jsp:useBean id="memberProcess" class="pack.business.MemberProcess" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h3>* 회원 정보 (MyBatis - Annotation) *</h3>
	<br>
	<a href="ins.jsp">회원 추가</a>
	<table border="1">
		<tr>
			<th>id</th>
			<th>name</th>
			<th>pwd</th>
			<th>date</th>
		</tr>
		<%
			ArrayList<DataDto> list = (ArrayList<DataDto>) memberProcess.selectDataAll();
		%>
		<c:set var="list" value="<%=list%>" />
		<c:if test="${empty list}">
			<tr>
				<td colspan="자료 없음"></td>
			</tr>
		</c:if>
		<c:forEach var="m" items="<%=list%>">
			<tr>
				<td><a href="del.jsp?id=${m.id}">${m.id}</a></td>
				<td><a href="update.jsp?id=${m.id}">${m.name }</a></td>
				<td>${m.passwd }</td>
				<td>${func:substring(m.reg_date,0,10)}</td>
			</tr>
		</c:forEach>
		<tr>
			<td colspan="4">id를 클릭하면 삭제, name을 클릭하면 수정을 진행합니다.</td>
		</tr>
	</table>
</body>
</html>