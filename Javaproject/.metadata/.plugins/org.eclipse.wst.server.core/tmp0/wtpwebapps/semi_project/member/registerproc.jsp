<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
request.setCharacterEncoding("utf-8");
%>
<jsp:useBean id="gbean" class ="pack.guest.GuestBean" />
<jsp:setProperty property="*" name="gbean"/>
<jsp:useBean id="memberProcess" class ="pack.guest.MemberProcess" />
<%
boolean b = memberProcess.memberInsert(gbean);
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
	//out.println("<a href='login.jsp'>로그인</a>");
	out.println("<a href='../main.jsp'>메인으로</a>");
}else{
	out.println("<b>회원가입</b>실패!! 관리자에게 문의하세요<br>");
	out.println("<a href='register.jsp'>가입 재시도하세요.</a>");
}
%>
</body>
</html>