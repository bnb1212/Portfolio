<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id");
	session.setAttribute("idkey", id); 
	// 이 클라이언트는 어느 JSP나 서블릿을 가도 이 세션을 공유한다
	// 세션보다 더 큰 어플리케이션(application)도 있으나 너무 전역적(global)이어서 잘 쓰지 않는다.
	session.setMaxInactiveInterval(10);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2> 세션 연습중 이에오 ( '-' ) </h2>
	<form action="j6session2.jsp" method="post">
	* 좋아하는 영화는 ?<br>
	<input type="radio" name="movie" value="기생충" checked="checked">기생충&nbsp;&nbsp;
	<input type="radio" name="movie" value="JOKER">JOKER&nbsp;&nbsp;
	<input type="radio" name="movie" value="코노스바">코노스바&nbsp;&nbsp;
	<input type="radio" name="movie" value="모던타임즈">모던타임즈&nbsp;&nbsp;
	<input type="submit" value="확인">
	</form>
</body>
</html>