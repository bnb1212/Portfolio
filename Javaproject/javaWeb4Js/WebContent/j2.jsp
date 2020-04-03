<!-- 얘네들이 지시어 -->
<!-- 상단 지시어의 import는 여러번 사용 가능 -->
<%@ page language="java" 
	contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"
    import="java.util.*"
    import="java.sql.Connection"
    session = "true"
    buffer="8kb"
    autoFlush="true"
    isThreadSafe ="true"
    info="jsp 문서 정보"
    errorPage="err.jsp"
    %>
 <!-- 기본값으로 서술시 안적어도 된다  -->
 <!-- 액션 태그 <jsp:어쩌구> -->
 <!-- 지시어와 액션태그는 실행결과는 같아도 과정이 다르다. -->
 
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>지시어</title>
</head>
<body>
날짜 출력 :
<%
	Calendar calendar = Calendar.getInstance();
	int year=calendar.get(Calendar.YEAR);
	int month=calendar.get(Calendar.MONTH)+1;
	out.println(year + "년" + month + "월");
%>
<br>
<%= this.getServletInfo() %>
<hr>
<%out.println(10/0); // 에러가 발생해서 err.jsp를 부르지만 포워딩이 발생해 주소는 j2.jsp 
					// 스프링은 forward가 기본. 리다이렉트와 포워드를 잘 이해해야함
					//리다이렉트 포워드 Model1까지는 포워드. 
					%> 

</body>
</html>