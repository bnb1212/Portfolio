<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>jsp가 넘겨준 자료</h2>
<%
// redirect 
//String data = request.getParameter("data");
//out.println("data : "+ data);



// forward
String data = (String)request.getAttribute("data");
out.println("data : " + data);

ArrayList<String> mylist = (ArrayList<String>)request.getAttribute("friend");
out.println("<br>친구들 : ");
for(String my:mylist){
	out.println(my + " ");
}
%>
</body>
</html>