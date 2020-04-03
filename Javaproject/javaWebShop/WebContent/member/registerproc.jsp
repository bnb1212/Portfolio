<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
%>
<jsp:useBean id="mbean" class="pack.member.MemberBean" />
<jsp:setProperty property="*" name="mbean" />
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr" />
<%
	boolean b = memberMgr.memberInsert(mbean);

%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
if(b){
	out.println("<b>회원가입</b>을 축하합니다<br>");
	out.println("<a href='../index.jsp'>로그인</a>");
	
	}else{
		out.println("<b>회원가입</b> 실패! 관리자에게 문의 바람<br>");
		out.println("<a href='register.jsp'>가입 재시도</a>");
	
}
%>
</body>
</html>