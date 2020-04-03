<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<script src="http://code.jquery.com/jquery-latest.js"></script>
<script type="text/javascript">
	$(document).ready(function() {
		$("#btnOk").bind("click", function() {
			//alert("버튼 이벤트 발생");
			if(frm.name.value==""){
				alert("이름을 입력하세요");
				frm.name.focus();
			}else if(frm.pass.value ==""){
				alert("비밀번호를 입력하세요");
				frm.pass.focus();
			}else if(frm.mail.value ==""){
				alert("이메일을 입력하세요");
				frm.mail.focus();
			}else if(frm.review_title.value ==""){
				alert("제목을 입력하세요");
				frm.review_title.focus();
			}else if(frm.review_cont.value ==""){
				alert("내용을 입력하세요");
				frm.review_cont.focus();
			}else
				frm.submit();
		});
	});
</script>
</head>
<body>
<%@ include file="../index_top.jsp" %>
<%@ include file="bb_top.jsp"%>
<br>
	<form name="frm" method="post" action="reviewboardsave.jsp">
		<table border="1" width="530">
			<tr>
				<td colspan='2'><h2>*** 글쓰기 ***</h2></td>
			</tr>
			<tr>
				<td align="center" width="100">이 름</td>
				<td width="430"><input name="name" size="15"></td>
			</tr>
			<tr>
				<td align="center">암 호</td>
				<td><input type="password" name="pass" size="15"></td>
			</tr>
			<tr>
				<td align="center">메 일</td>
				<td><input name="mail" size="25"></td>
			</tr>
			<tr>
				<td align="center">제 목</td>
				<td><input name="review_title" size="50"></td>
			</tr>
			<tr>
				<td align="center">내 용</td>
				<td><textarea name="review_cont" cols="50" rows="10"></textarea></td>
			</tr>
			<tr>
				<td colspan="2" align="center" height="30"><input type="button"
					value="메  인" onClick="location.href='../main.jsp'">&nbsp;
					<input type="button" value="작  성" id="btnOk">&nbsp; <input
					type="button" value="목  록"
					onClick="location.href='reviewboardlist.jsp'"></td>
			</tr>
		</table>
	</form>
<%@ include file="../guest/guest_bottom.jsp" %> 
</body>
</html>