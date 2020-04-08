<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h3>* 회원 자료 (@MVC - JdbcDaoSupport) *</h3>
	<%--
	<table border="1">
		<tr>
			<td colspan="2"><a href="insert">추가</a></td>
		</tr>
		<tr>
			<th width="70">id</th>
			<th width="100">name</th>
		</tr>
		<c:forEach var="m" items="${list }">
			<tr>
				<td>${m.id }</td>
				<td>${m.name }</td>
			</tr>
		</c:forEach>

	</table>
	--%>

	<c:if test="${count == 0}">
	출력자료가 업서요 흑흑 기부해주새요 흑흑
	<a href="insert">추가</a>
	</c:if>

	<c:if test="${count > 0}">
		<table border="1">
			<tr>
				<td colspan="2"><a href="insert">추가</a></td>
			</tr>
			<tr>
				<th width="70">id</th>
				<th width="100">name</th>
			</tr>
			<c:forEach var="m" items="${list }">
				<tr>
					<td>${m.id }</td>
					<td><a href="detail?id=${m.id}">${m.name }</td>
				</tr>
			</c:forEach>
			<!-- pagelink -->
			<tr>
				<td colspan="2" style="text-align: center; height: 30px"><c:set
						var="pageCount" value="${(count-1) / pageSize + 1}"></c:set> <c:forEach
						var="p" begin="1" end="${pageCount }">
						<c:if test="${currentPage == p }">${p }</c:if>
						<c:if test="${currentPage != p }">
							<a href="list?pageNum=${p}"> ${p }</a>
						</c:if>
					</c:forEach></td>
			</tr>
		</table>
	</c:if>
</body>
</html>