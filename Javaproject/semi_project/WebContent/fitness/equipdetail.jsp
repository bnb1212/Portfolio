<%@page import="pack.equip.EquipDto"%>
<%@page import="pack.equip.EquipProc"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<jsp:useBean id="equipProc" class="pack.equip.EquipProc" />
<%
	String no = request.getParameter("no");
	EquipDto dto = equipProc.selectEquipOne(no);
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>장비 세부 안내</title>
<link href="../css/imsi.css" rel="stylesheet" type="text/css">
<link
	href="https://fonts.googleapis.com/css?family=Do+Hyeon&display=swap&subset=korean"
	rel="stylesheet">
</head>
<body>
	<h3>== 장비 안내 ==</h3>
	<p />
	<main>
		<table>
			<tr>
				<td rowspan="3"><img src="../upload/<%=dto.getEquip_image()%>"
					width="250" height="250"></td>
				<td>장비 이름 : <%=dto.getEquip_name()%></td>
			</tr>
			<tr>
				<td>보유수 : <%=dto.getEquip_stock()%></td>
			</tr>
			<tr>
				<td>소개 : <%=dto.getEquip_info()%></td>
			</tr>

		</table>
	</main>
</body>
</html>