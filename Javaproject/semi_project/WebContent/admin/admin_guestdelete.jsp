<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="bean" class="pack.guest.GuestBean" />
<jsp:setProperty property="*" name="bean" />
<jsp:useBean id="memberProcess" class="pack.guest.MemberProcess" />
<%
	request.setCharacterEncoding("utf-8");
	String guest_no = request.getParameter("no");
%>
<%
	boolean b = memberProcess.deleteGuest(guest_no);

	if (b) {
		response.sendRedirect("admin_guestlist.jsp");
	} else {
		response.sendRedirect("fail.jsp");
	}
%>