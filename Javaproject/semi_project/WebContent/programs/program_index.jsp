<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	String id = (String) session.getAttribute("idkey");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>프로그램 등록</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
<script type="text/javascript">
	window.onload = function() {

		document.getElementById("btnSubmit").onclick = regCheck;
	}
</script>
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
			<td><a href="../trainers/trainers_index.jsp"><img
					src="../images/trainers.png"></a></td>
			<td style="background-color: #aabbcc; text-align: center;"><a
				href="../programs/program_index.jsp"><img
					src="../images/programs.png"></a></td>
			<td><a href="../qnaboard/qnaboardlist.jsp"><img src="../images/community.png"></a></td>
		</tr>
	</table>
	<table class="table">
		<tr>
			<td style="background-color: #aabbcc; text-align: center;"
				valign="middle">

				<form name="regForm" method="post" action="programproc.jsp">
					<table border="1"
						style="background-image: url(../images/proimage.jpg); background-size: 80%">
						<tr align="center" style="background-color: #8899aa">

							<td colspan="2"><b style="color: #FFFFFF">프로그램 안내 표 </b></td>
						</tr>
						<tr>
							<td width="13%" colspan="2" align="center"
								style="background-color: yellow">기본(0번) 프로그램</td>
						</tr>

						<tr>
							<td width="16%" colspan="2" align="center">기본 헬스장 이용 price
								= 30000 <br> 회원등급 : bronze
							</td>
						</tr>
						<tr>
							<td width="13%" colspan="2" align="center"
								style="background-color: yellow">1번 프로그램</td>
						</tr>

						<tr>
							<td width="16%" colspan="2" align="center">헬스장 이용권 + 개인
								pt2번 <br>price = 50000 <br> 회원등급 : silver
							</td>
						</tr>
						<tr>
							<td width="13%" colspan="2" align="center"
								style="background-color: yellow">2번 프로그램</td>
						</tr>

						<tr>
							<td width="16%" colspan="2" align="center">헬스장 이용권 + 개인
								pt4번 <br>price = 66000 <br> 회원등급 : gold
							</td>
						</tr>
						<tr>
							<td width="13%" colspan="2" align="center"
								style="background-color: green">회원 등급 별 혜택</td>
						</tr>

						<tr>
							<td width="16%" colspan="2" align="center">bronze = 기본 옷 +
								샤워도구 증정 <br>silver = 기본 옷 + 샤워도구 증정 + 100ml 단백질 보충제 증정 <br>
								gold = 기본 옷 + 샤워도구 증정 + 250ml 단백질 보충제 증정 + 다음달 회원 할인권 (30%) 증정.
								<br> 등급만 올리고 싶으시다면 각 등급 up당 20000원이 추가됩니다.
							</td>

						</tr>
						<tr>
							<td>신청 프로그램 번호 :</td>
							<td><input type="text" name="guest_program_no" size="60"
								value="0"></td>

						</tr>
						<tr>
							<td>신청 회원 등급 :</td>
							<td><input type="text" name="guest_grade" size="60">

							</td>

						</tr>
						<tr>
							<td>신청 회원 번호 :</td>
							<td><input type="text" name="guest_no" size="60"></td>

						</tr>
						<tr>
							<td colspan="2" align="center"><input type="button"
								value="신청하기" id="btnSubmit"> &nbsp;&nbsp;&nbsp;&nbsp; <input
								type="reset" value="다시쓰기"></td>
						</tr>
					</table>
				</form>
			</td>
		</tr>
		<%@ include file="../guest/guest_bottom.jsp"%>
	</table>
</body>
</html>