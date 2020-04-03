<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="orderMgr" class="pack.order.OrderMgr" />
<%
	String flag = request.getParameter("flag");
	String no = request.getParameter("no");
	String state = request.getParameter("state");

	boolean b = false;

	if (flag.equals("update")) {
		b = orderMgr.updateOrder(no, state);
	} else if (flag.equals("delete")) {
		b = orderMgr.deleteOrder(no);
	} else {
		response.sendRedirect("ordermanager.jsp");
	}

	if (b) {
%>
<script>
	alert("정상 처리됨");
	location.href = "ordermanager.jsp";
</script>
<%
	} else {
%>
<script>
	alert("오류 발생");
	location.href = "ordermanager.jsp";
</script>
<%
	}
%>