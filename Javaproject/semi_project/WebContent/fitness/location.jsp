<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
</head>
<body>
<%
		String memid = (String) session.getAttribute("idkey");
		String log = "";

		if (memid == null) // 로그인 안함
			log = "<a href='../guest/login.jsp'><img src='../images/loginin.png'></a>";
		else
			log = "<a href='../guest/logout.jsp'><img src='../images/logout.png'></a>";

		String mem = "";
		if (memid == null)
			mem = "<a href='../member/register.jsp'><img src='../images/signup.png'></a>";
		else
			mem = "<a href='../reviewboard/reviewboardlist.jsp'><img src='../images/review.png'></a>";
	%>
	<%@ include file="../index_top.jsp"%>
	<table style="width: 80%" border="1">
		<tr style="background-color: white; text-align: center;">


			<td><a href="../main.jsp"><img src="../images/home.png"></a></td>
			<td><%=log%></td>
			<td><%=mem%></td>
			<td style="background-color: #aabbcc; text-align: center;">
			<a class="menu_1" href="../fitness/fitness.jsp"><img
					src="../images/fitness.png"></a></td>
			<td><a href="../trainers/trainers_index.jsp"><img
					src="../images/trainers.png"></a></td>
			<td><a href="../programs/program_index.jsp"><img
					src="../images/programs.png"></a></td>
			<td><a href="../qnaboard/qnaboardlist.jsp"><img src="../images/community.png"></a></td>
		</tr>
	</table>
<br><br>
<table style="width: 50" border="1">
	<tr style="text-align: center;">
		<td><a href="fitness.jsp"> <img src="../images/equipment.png">
		</a></td>
	</tr>
	<tr style="background-color: #aabbcc; text-align: center;">
		<td><a href="location.jsp"> <img src="../images/location.png">
		</a></td>
	</tr>
</table>
<table style="width: 50; margin: auto; text-align: center;">
		<tr>
			<td><img src="../images/loca.png" style="border: 3px solid #A6243C"></td>
		</tr>
	</table>
<%@ include file="../guest/guest_bottom.jsp" %> 
</body>