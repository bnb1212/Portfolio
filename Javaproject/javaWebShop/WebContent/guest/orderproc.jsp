<%@page import="pack.order.OrderBean"%>
<%@page import="java.util.Enumeration"%>
<%@page import="java.util.Hashtable"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="cartMgr" class="pack.order.CartMgr" scope="session" />
<jsp:useBean id="orderMgr" class="pack.order.OrderMgr" />
<jsp:useBean id="productMgr" class="pack.product.ProductMgr"></jsp:useBean>
<%
	Hashtable hCart = cartMgr.getCartList();

	Enumeration enu = hCart.keys();
	if(hCart.size() == 0){
%>
<script>
	alert("주문 내역 없습니다.");
	location.href="orderlist.jsp";
	
</script>
<%
	}else{
		while(enu.hasMoreElements()){
			OrderBean order = (OrderBean)hCart.get(enu.nextElement());
			orderMgr.insertOrder(order);// shop_order에 주문 정보를 저장
			productMgr.reduceProduct(order); // 주문 수량 만큼 shop_product의 재고량 빼기
			cartMgr.deleteCart(order);			
		}
%>
	<script>
	alert("주문 처리 성공");
	location.href="orderlist.jsp";
	
	</script>
	<%
	}
	
	%>


