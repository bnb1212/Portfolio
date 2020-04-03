<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>쇼핑몰</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
</head>
<body style="margin-top: 20">
	<h2>전문 쇼핑몰</h2>
	<%@include file="guest_top.jsp"%>
	<table style="width: 80%">
	<%if (memid != null){%>
		<tr style="text-align: center;">
			<td>
				<%= memid%>님! 방문을 환영합니다.
				<img src="../images/pic2.gif">
			</td>
		</tr>
	<%}else{%>
		<tr style="text-align: center;">
			<td style="font-size: 20px; 
			background-image:url('../images/pic.jpg');
			background-size:100%">
			<br><br><br><br> 리카누님 소ㄴ..아니 방문자가 왔어!
			<br><br><br><br> 만물의 도서관에 온것을 환영하노라!
		</td>
		<%} %>
		<tr>
			<td><pre>
			
			</pre></td>
		</tr>
	</table>

	<%@include file="guest_bottom.jsp"%>
</body>
</html>