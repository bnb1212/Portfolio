<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% 
session.removeAttribute("idkey"); // session.invalidate();
%>

<script>
alert("로그아웃 성공");
//location.href="login.jsp";
location.href="../main.jsp";
</script>