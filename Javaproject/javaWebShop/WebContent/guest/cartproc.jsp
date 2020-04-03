<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="order" class="pack.order.OrderBean" />
<jsp:setProperty property="*" name="order" />
<%--이 객체는 scope속성으로 섹션이 살아있는 동안 유효함 --%>
<jsp:useBean id="cartMgr" class="pack.order.CartMgr" scope="session" />

<%
	String flag = request.getParameter("flag"); // 구매목록 보기, 수정, 삭제 판단
	String id = (String) session.getAttribute("idKey");
	// out.print("주문 수 : " + order.getProduct_no() + " " + order.getQuantity());

	if (id == null) { // 고객 로그인 안한 경우 로그인으로 이동
		response.sendRedirect("login.jsp");
	} else {
		if (flag == null) {
			order.setId(id);
			cartMgr.addCart(order); // cart에 주문 상품 담기
%>
<script>
	alert("장바구니에 담기 성공");
	location.href = "cartlist.jsp"; //잘 담겼는지 확인
	//location.href="productlist.jsp"; // 바로 계속 쇼핑
</script>

<%
	} else if (flag.equals("update")) {
			// cartMgr.updateCart(order);
			order.setId(id);
			cartMgr.updateCart(order);
%>
<script>
	alert("장바구니에 내용 수정 성공");
	location.href = "cartlist.jsp";
</script>
<%
	} else if (flag.equals("delete")) {
			cartMgr.deleteCart(order);
%>
<script>
	alert("해당 상품의 주문을 삭제했습니다.");
	location.href = "cartlist.jsp";
</script>
<%
	}
	}
%>