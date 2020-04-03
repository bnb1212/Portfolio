<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원가입</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">

<script src="../js/script.js"></script>
<script type="text/javascript">
window.onload = function(){
	regForm.guest_id.focus();
	
	document.getElementById("btnSubmit").onclick = inputCheck;
}
</script>
</head>
<body>
<br>
<table style="width: 5%">
	<tr style="text-align: center;">
		<td>
			
			<a href="../main.jsp"><img src="../images/kic.png"></a>
		</td>
	</tr>
</table>
<table class="table">
<tr>
	<td align="center" valign="middle" style="background-image: url(../images/welcome.jpg); background-size: 100%">
	
		<form name="regForm" method="post" action="registerproc.jsp">
			<table border="1">
				<tr align="center" style="background-color: #8899aa">
				
					<td colspan="2"><b style="color: #FFFFFF">회원 가입</b></td>
				</tr>
				<tr>
					<td width="16%">회원 번호</td>
					<td width="57%"><input type="text" name="guest_no" size="15">
						
				</tr>
				<tr>
					<td>회원 이름</td>
					<td><input type="text" name="guest_name" size="15"></td>
				</tr>
				<tr>
					<td>회원 id</td>
					<td><input type="text" name="guest_id" size="15">
					
				</tr>
				<tr>
					<td>패스워드</td>
					<td><input type="text" name="guest_passwd" size="15"></td>
				</tr>
				<tr>
					<td>회원등급</td>
					<td><input type="hidden" name="guest_grade" size="27" value="bronze"><span style = " font-size:1.0em; font-weight: bold; color: black;">
					처음등록시 bronze로만 등록 가능합니다.
					</span></td>
				</tr>
				<tr>
					<td>참여 프로그램 번호</td>
					<td><input type="hidden" name="guest_program_no" size="7" value="0">
					<span style = " font-size:1.0em;  font-weight: bold; color:	red;">
					프로그램 등록 페이지에서 참조, 신청해주세요
					</span>
					</td>
				</tr> 
				<tr>
					<td>전화번호</td>
					<td>
						<input type="text" name="guest_tel" size="20"> 
						
					</td>
				</tr>
				<tr>
					<td>성별</td>
					<td><input type="text" name="guest_gen" size="60"></td>
				</tr>
				<tr>
					<td>주소</td>
					<td>
						<input type="text" name="guest_addr" size="60">
					</td>
				</tr>
				
				<tr>
					<td>생일</td>
					<td>
						<input type="text" name="guset_birth" size="60">
					</td>
				</tr>
				<tr>
					<td colspan="2" align="center">
						<input type="button" value="회원가입" id="btnSubmit">
						&nbsp;&nbsp;&nbsp;&nbsp; 
						<input type="reset" value="다시쓰기">
					</td>
				</tr>
			</table>
		</form>
	</td>
</tr>
</table>
</body>
</html>