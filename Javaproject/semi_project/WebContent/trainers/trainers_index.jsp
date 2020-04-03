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
			<td><a class="menu_1" href="../fitness/fitness.jsp"><img
					src="../images/fitness.png"></a></td>
			<td style="background-color: #aabbcc; text-align: center;"><a
				href="../trainers/trainers_index.jsp"><img
					src="../images/trainers.png"></a></td>
			<td><a href="../programs/program_index.jsp"><img
					src="../images/programs.png"></a></td>
			<td><a href="../qnaboard/qnaboardlist.jsp"><img src="../images/community.png"></a></td>
		</tr>
	</table>
	<br>
	<br>
	<table style="width: 50" border="1">
		<tr style="background-color: #aabbcc; text-align: center;">
			<td><a href="ceo.jsp"> <img src="../images/ceo.png">
			</a></td>
		</tr>
		<tr style="text-align: center;">
			<td><a href="trainers.jsp"> <img src="../images/trainer.png">
			</a></td>
		</tr>
	</table>
	<br>
	<table style="width: 50; margin: auto; text-align: center;">
		<tr>
			<td><img src="../images/asd.jpg"></td>
		</tr>
	</table>
	<%@ include file="../guest/guest_bottom.jsp"%>
</body>
</html>