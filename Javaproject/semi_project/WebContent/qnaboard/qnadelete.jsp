<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%
	String no = request.getParameter("qna_no");
	String spage = request.getParameter("page");
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
function check() {
	/*
	if(frm.pass.value === ""){
		frm.pass.focus();
		alert("비밀번호 입력!");
		return;
	}
	*/
	if(confirm("정말 삭제할까요?")){
		frm.submit();
	}
}
</script>
</head>
<body>
<h2>* 글 삭제 *</h2>
<form action="qnadeleteok.jsp" name='frm' method='post'>
	<input type="hidden" name="qna_no" value="<%=no%>">
	<input type="hidden" name="page" value="<%=spage%>">
	비밀번호 입력 : 
	<input type="password" name='pass'><p/>
	<input type="button" onclick="check()" value="삭제 확인">
	<input type="button" value='목록 보기' onclick="location.href='qnaboardlist.jsp?page=<%=spage%>'">
</form>
</body>
</html>