<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id"); // id값 받음
	String password = request.getParameter("password"); // id값 받음
%>
<script src="https://code.jquery.com/jquery-latest.js"></script>
<jsp:useBean id="admin" class="pack.admin.AdminDto" />
<jsp:useBean id="adminProc" class="pack.admin.AdminProc" />



<%
	boolean b = adminProc.adminLogin(id, password);

	if (b) {
		session.setAttribute("adminKey", id);
		response.sendRedirect("admin_index.jsp");
	} else {
		response.sendRedirect("fail.jsp");
	}
%>
