<%@page import="pack.member.MemberBean"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr" />
<%
	request.setCharacterEncoding("utf-8");
	String id = (String) session.getAttribute("idKey");

	MemberBean bean = memberMgr.getMember(id);

	if (bean == null) {
		response.sendRedirect("../guest/guest_index.jsp");
		return;
	}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원수정</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<script src="../js/script.js"></script>
<script type="text/javascript">
	window.onload = function() {

	}
</script>
</head>
<body>
	<form action="memberupdateproc.jsp" name="updateForm" method="post">
		<table border="1" style="width: 80%">
			<tr>
				<td colspan="2"><b><%=bean.getName()%></b> 회원님의 정보를 수정합니다.</td>
			</tr>
			<tr>
				<td>아이디</td>
				<td><%=bean.getId()%></td>
			</tr>
			<tr>
				<td>비밀번호</td>
				<td><input type="text" name="passwd"
					value="<%=bean.getPasswd()%>" /></td>
			</tr>
			<tr>
				<td>이름</td>
				<td><input type="text" name="name" value="<%=bean.getName() %>" /></td>
			</tr>
			<tr>
				<td>E-mail</td>
				<td><input type="text" name="email"
					value="<%=bean.getEmail()%>" /></td>
			</tr>
			<tr>
				<td>전화번호</td>
				<td><input type="text" name="phone"
					value="<%=bean.getPhone()%>" /></td>
			</tr>
			<tr>
				<td>우편번호</td>
				<td><input type="text" name="zipcode"
					value="<%=bean.getZipcode()%>" /></td>
			</tr>
			<tr>
				<td>주소</td>
				<td><input type="text" name="address"
					value="<%=bean.getAddress()%>" /></td>
			</tr>
			<tr>
				<td>직업</td>
				<td><select name=job>
						<option value="<%=bean.getJob() %>">선택하세요
						<option value="회사원">회사원
						<option value="학생">학생
						<option value="자영업">자영업
						<option value="주부">주부
						<option value="기타">기타
				</select></td>
			</tr>
			<tr>
				<td colspan="2" style="text-align: center;">
					<input type="submit" value="수정완료">
					<input type="button" value="수정취소" onclick="javascript:history.back()">
					<input type="button" value="회원 탈퇴">
				</td>
			</tr>
		</table>
	</form>
</body>
</html>