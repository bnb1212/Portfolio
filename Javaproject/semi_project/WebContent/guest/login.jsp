<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
String id = (String)session.getAttribute("idkey");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<script type="text/javascript">
window.onload = function(){
	document.getElementById("btnLogin").addEventListener("click", funcLogin);
	document.getElementById("btnNewMember").addEventListener("click", funcNew);
}

function funcLogin(){
	if(loginForm.guest_id.value === ""){
		alert("로그인 아이디 입력");
		loginForm.guest_id.focus();
	}else if(loginForm.guest_passwd.value === ""){
		alert("비밀번호 입력");
		loginForm.guest_passwd.focus();
	}else{
			loginForm.action="loginproc.jsp";
			loginForm.method="post";
			loginForm.submit();
		}
}

function funcNew(){
	location.href="../member/register.jsp";	
}
</script>
<title>Insert title here</title>
</head>
<body>
<%
if( id != null){
%>
	<b><%=id %>님 환영합니다</b>
	<br>이미 로그인중입니다.<br>
	<a href="../main.jsp">홈으로</a><br>
	<a href="logout.jsp">로그아웃</a>
<%}else { %>
<table style="width: 5%">
	<tr style="text-align: center;">
		<td>
			
			<a href="../main.jsp"><img src="../images/kic.png"></a>
		</td>
	</tr>
</table>
	<form name="loginForm">
	<table border="1" style="background-image: url(../images/B20161117012606368.jpg); background-size: 100%">
		<tr>
			<td colspan="2">*로그인*</td>
		</tr>
		<tr>
			<td>id :</td>
			<td><input type="text" name ="guest_id"></td>
		</tr>
		<tr>
			<td>pwd :</td>
			<td><input type="text" name ="guest_passwd"></td>
		</tr>
		<tr>
			<td colspan="2">
				<input type="button" value="로 그 인" id = "btnLogin">
				<input type="button" value="회원가입" id = "btnNewMember">
			</td>
		</tr>
	</table>
	</form>

<%
}
%>
</body>
</html>