<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	String adminId = (String) session.getAttribute("adminKey");
	if (adminId == null) {
		response.sendRedirect("admin/adminlogin.html");
		return;
	} else
		response.sendRedirect("admin/admin_index.jsp");
%>