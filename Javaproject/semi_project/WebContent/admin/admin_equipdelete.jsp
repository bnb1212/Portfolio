<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<jsp:useBean id="bean" class="pack.equip.EquipFormBean" />
<jsp:setProperty property="*" name="bean" />
<jsp:useBean id="equipProc" class="pack.equip.EquipProc" />
<%
	request.setCharacterEncoding("utf-8");
	String equip_no = request.getParameter("no");
%>
<%
	boolean b = equipProc.deleteEquip(equip_no);

	if (b) {
		response.sendRedirect("admin_equiplist.jsp");
	} else {
		response.sendRedirect("fail.jsp");
	}
%>