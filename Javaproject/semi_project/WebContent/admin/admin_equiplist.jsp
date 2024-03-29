<%@page import="pack.equip.EquipDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="func" uri="http://java.sun.com/jsp/jstl/functions"%>

<jsp:useBean id="equipProc" class="pack.equip.EquipProc" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link
	href="https://fonts.googleapis.com/css?family=Do+Hyeon&display=swap&subset=korean"
	rel="stylesheet">
<link rel="stylesheet" href="../css/admin.css" rel="stylesheet"
	type="text/css">
<script src="https://code.jquery.com/jquery-latest.js"></script>
<script src="../js/myscript2.js"></script>
<title>KICF 관리자 페이지 - 장비</title>
<script type="text/javascript">

</script>
</head>

<body>
	<!-- wrap -->
	<div id="wrap" class="relatuve center clearfix">
		<!-- Common Header -->
		<header>
			<div class="headtop">
				<div class="logo">
					<a href="admin_index.jsp"><img src="../images/logo.png" alt=""></a>
				</div>
				<div class="admin_button">
					<a href="adminlogout.jsp"><img
						src="../images/logout.gif" alt="" width="80px"></a>
				</div>
			</div>
			<div class="currentPage">
				<div class="incurrentPage">
					<div class="headline">
						<b>Equipment Management</b>
					</div>
				</div>
			</div>
		</header>
		<div id="body_wrap">
			<nav id="menu">
				<ul>
					<li><a href="admin_index.jsp">메인 화면</a></li>
					<li><a href="admin_guestlist.jsp">회원 관리</a></li>
					<li class="active"><a href="#">장비 관리</a></li>
				</ul>
			</nav>
			<main>
				<div class="equip_table">
					<table>
						<tr>
							<th class="check">&nbsp;</th>
							<th class="name">장비 명</th>
							<th class="stock">보유 수</th>
							<th class="image">이미지 보기</th>
						</tr>
						<%
							ArrayList<EquipDto> list = (ArrayList<EquipDto>) equipProc.selectEquip();
						%>
						<c:set var="list" value="<%=list%>" />
						<c:if test="${empty list}">
							<tr>
								<td colspan="장비 없음"></td>
							</tr>
						</c:if>
						<c:forEach var="m" items="<%=list%>">
							<tr class="create_row">
								<td style="text-align: center;">${m.equip_no}</td>
								<td>${m.equip_name}</td>
								<td>${m.equip_stock}</td>
								<td>이미지 / 설명 보기</td>
							</tr>
						</c:forEach>
						<tr>
							<td class="buttons" colspan="4">
								<ul>
									<li><a href="#" id="btn_equip_delete">-</a></li>
									<li><a href="#" id="btn_equip_insert">+</a></li>
								</ul>
							</td>
						</tr>
					</table>
					<div class="add_div"></div>
				</div>
			</main>
		</div>
	</div>
</body>
</html>