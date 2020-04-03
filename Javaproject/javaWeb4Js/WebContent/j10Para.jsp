<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%
    request.setCharacterEncoding("utf-8");
    %>
    
 <jsp:useBean id="bean" class="pack.ExamBean"/>
 <%--
 <jsp:setProperty property="name" id="bean"/>
 ...
 --%>
 <<jsp:setProperty property="*" name="bean"/> 
 <!-- 폼 빈 프로퍼티는 별 -->
 <%
 	System.out.println(bean.getName() + " " + bean.getKor() + " " + bean.getEng());
 %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
성적 자료 출력<br>
이름은 <jsp:getProperty property="name" name="bean"/><br>
국어는 <jsp:getProperty property="kor" name="bean"/><br>
영어는 <jsp:getProperty property="eng" name="bean"/><br>

<jsp:useBean id="examProcess" class="pack.ExamProcess"/>
<jsp:setProperty property="examBean" name="examProcess" value="<%=bean %>"/>
총점 : <jsp:getProperty property="tot" name="examProcess"/>
평균 : <jsp:getProperty property="avg" name="examProcess"/>
</body>
</html>