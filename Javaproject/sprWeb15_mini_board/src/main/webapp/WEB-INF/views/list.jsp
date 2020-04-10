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
	<h3>미니 게시판 ('-')</h3>
	<br>
	<a href="insert">글쓰기</a>
	<table border="1">
		<tr>
			<th>번호</th>
			<th>제목</th>
			<th>작성자</th>
			<th>조회수</th>
		</tr>
		<c:forEach var="s" items="${datas }">
			<tr>
				<td>${s.num }</td>
				<td><a href="detail?num=${s.num}">${s.title }</a></td>
				<td>${s.author }</td>
				<td>${s.readcnt }</td>
			</tr>
		</c:forEach>
		<!-- 검색 -->
		<tr>
			<td colspan="4">
				<form action="search" method="post">
					<select name="searchName">
						<option value="author">작성자</option>
						<option value="title">제목</option>
					</select> <input type="text" name="searchValue"> <input
						type="submit" value="검색">
				</form>
			</td>
	</table>
</body>
</html>