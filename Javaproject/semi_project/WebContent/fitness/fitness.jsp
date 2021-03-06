<%@page import="pack.equip.EquipDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
	
<jsp:useBean id="equip" class="pack.equip.EquipDto" />
<jsp:useBean id="equipProc" class="pack.equip.EquipProc" />

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="func" uri="http://java.sun.com/jsp/jstl/functions"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
<link href="../css/imsi.css" rel="stylesheet" type="text/css">
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
	<br>
	<br>
	<div class="fitness_info">
	<div style="width:150px">
	<table style="width: 140px" border="1">
		<tr style="background-color: #aabbcc; text-align: center;">
			<td><a href="fitness.jsp"> <img src="../images/equipment.png">
			</a></td>
		</tr>
		<tr style="text-align: center;">
			<td><a href="location.jsp"> <img src="../images/location.png">
			</a></td>
		</tr>
	</table>
	</div>
	
	<section>
		<%
		ArrayList<EquipDto> list = (ArrayList<EquipDto>) equipProc.selectEquip();
	%>
		<c:set var="list" value="<%=list%>" />
		<c:forEach var="e" items="<%=list%>">
			<figure>
				<a href="equipdetail.jsp?no=${e.equip_no}"><img src="../upload/${e.equip_image}" width="250" height="250">
				</a>
				<figcaption><a href="equipdetail.jsp?no=${e.equip_no}">${e.equip_name}</a></figcaption>
			</figure>
		</c:forEach>
		</section>
	
	
	</div>
	<%@ include file="../guest/guest_bottom.jsp"%>
</body>
</html>