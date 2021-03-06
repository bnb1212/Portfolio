<%@page import="pack.guest.GuestDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="func" uri="http://java.sun.com/jsp/jstl/functions"%>

<jsp:useBean id="memberProcess" class="pack.guest.MemberProcess" />
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
<title>KICF 관리자 페이지 - 회원</title>
<script type="text/javascript">
	
<%--
	window.onload = function() {
		document.getElementById("admin_logout").onclick = funcAdminLogOut;
	}

	function funcAdminLogOut() {
		location.href="adminlogout.jsp";
	}
	--%>
	
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
					<a href="adminlogout.jsp"><img src="../images/logout.gif"
						alt="" width="80px"></a>
				</div>
			</div>
			<div class="currentPage">
				<div class="incurrentPage">
					<div class="headline">
						<b>Member Management</b>
					</div>
				</div>
			</div>
		</header>
		<div id="body_wrap">
			<nav id="menu">
				<ul>
					<li><a href="admin_index.jsp">메인 화면</a></li>
					<li class="active"><a href="#">회원 관리</a></li>
					<li><a href="admin_equiplist.jsp">장비 관리</a></li>
				</ul>
			</nav>
			<main>
				<div class="guest_table">
					<table>
						<tr>
							<th class="check">&nbsp;</th>
							<th class="guest_no">회원 번호</th>
							<th class="guest_name">회원 이름</th>
							<th class="guest_id">회원 ID</th>
							<th class="guest_grade">회원 등급</th>
							<th class="guest_tel">회원 전화번호</th>
							<th class="guest_gen">회원 성별</th>
							<th class="guest_addr">회원 주소</th>
							<th class="guest_birth">회원 생일</th>

						</tr>
						<%
							ArrayList<GuestDto> list = (ArrayList<GuestDto>) memberProcess.selectDataAll();
						%>
						<c:set var="list" value="<%=list%>" />
						<c:if test="${empty list}">
							<tr>
								<td colspan="회원 없음"></td>
							</tr>
						</c:if>
						<c:forEach var="m" items="<%=list%>">
							<tr class="create_row">
								<td style="text-align: center;"><input type="checkbox"></td>
								<td>${m.guest_no}</td>
								<td>${m.guest_name}</td>
								<td>${m.guest_id}</td>
								<td>${m.guest_grade}</td>
								<td class='tel'>${m.guest_tel}</td>
								<td>${m.guest_gen}</td>
								<td>${m.guest_addr}</td>
								<td>${m.guest_birth}</td>

							</tr>
						</c:forEach>
						<tr>
							<td class="buttons" colspan="9">
								<ul>
									<li><a href="#" id="btn_guest_delete">-</a></li>

								</ul>
							</td>
						</tr>
					</table>
				</div>
			</main>
		</div>
	</div>
</body>
</html>