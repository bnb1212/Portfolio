<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	String id = (String) session.getAttribute("idKey");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
<script type="text/javascript">
	window.onload = function() {
		document.getElementById("btnLogin").addEventListener("click", funcLogin);
		document.getElementById("btnNewMember").addEventListener("click", funcNew);
	}

	function funcLogin() {
		if(loginForm.id.value === ""){
			alert("로그인 아이디 입력");
			loginForm.id.focus();
		}else if(loginForm.passwd.value === ""){
			alert("비밀번호 입력");
			loginForm.passwd.focus();
		}else{
			loginForm.action ="loginproc.jsp";
			loginForm.method="post";
			loginForm.submit();
		}	
	}
	
	function funcNew() {
		location.href = "register.jsp";
	}
</script>
</head>
<body>
	<%
		if (id != null) {
	%>
	<b><%=id%>님 환영 합니다</b>
	<br>준비된 기능을 사용할 수 있습니다.
	<br>
	<a href="logout.jsp">로그아웃</a>
	<%
		} else {
	%>
	<form name="loginForm">
		<table>
			<tr>
				<td>* 로그인 *</td>
			</tr>
			<tr>
				<td>id :</td>
				<td><input type="text" name="id"></td>
			</tr>
			<tr>
				<td>pwd :</td>
				<td><input type="text" name="passwd"></td>
			</tr>
			<tr>
				<td colspan="2">
				<td><input type="button" value="로그인" id="btnLogin"></td>
				<td><input type="button" value="회원가입" id="btnNewMember"></td>
			</tr>
		</table>
	</form>

	<%
		}
	%>

</body>
</html>