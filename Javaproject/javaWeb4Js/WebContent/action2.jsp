<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
out.print("액션태그2");
<% 
String msg = request.getParameter("msg");
%>
<%= "메세지는" + msg %>
