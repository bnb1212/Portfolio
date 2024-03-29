<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link
	href="https://fonts.googleapis.com/css?family=Do+Hyeon&display=swap&subset=korean"
	rel="stylesheet">
<link rel="stylesheet" href="../css/admin.css" rel="stylesheet"
	type="text/css">
<title>KICF 관리자 페이지 </title>
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
					<a href="adminlogout.jsp"><img src="../images/logout.gif" alt="" width="80px"></a>
				</div>
			</div>
			<div class="currentPage">
				<div class="incurrentPage">
					<div class="headline"><b>Front Page</b></div>
				</div>
			</div>
		</header>
		<div id="body_wrap">
			<nav id="menu">
				<ul>
					<li class="active"><a href="#">메인 화면</a></li>
					<li><a href="admin_guestlist.jsp">회원 관리</a></li>
					<li><a href="admin_equiplist.jsp">장비 관리</a></li>
				</ul>
			</nav>
			<main>
			<span>
			<a href="admin_guestlist.jsp"><img src="../images/guestbutton.png" style='width:250px'></a>
			<a href="admin_equiplist.jsp"><img src="../images/equipbutton.png" style='width:250px'></a>
			</span>
			</main>
		</div>
	</div>
	<%--
	<a href="admin_equiplist.jsp">장비관리</a><br>
	<a href="../guest/guest_equiplist.jsp">게스트 장비목록보기</a><br>
	<button id="admin_logout" value="로그아웃">로그아웃</button>
	--%>
</body>
</html>