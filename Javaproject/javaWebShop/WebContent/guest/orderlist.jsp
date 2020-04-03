<%@page import="pack.product.ProductDto"%>
<%@page import="pack.order.OrderDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="orderMgr" class="pack.order.OrderMgr" />
<jsp:useBean id="productMgr" class="pack.product.ProductMgr" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>주문 목록</title>
<script type="text/javascript" src="../js/script.js"></script>
<script type="text/javascript" src="../js/script2.js"></script>
<link href="../css/board.css" rel="stylesheet" type="text/css">
</head>
<body>
	<%@ include file="guest_top.jsp"%>
	<br>


	<table style="width: 80%">
		<tr>
			<td colspan="5" style='text-align: center'>** 주문 상품 목록 **</td>
		</tr>
		<tr>
			<th>주문번호</th>
			<th>상품명</th>
			<th>주문 수</th>
			<th>주문 일자</th>
			<th>주문 상태</th>
		</tr>

		<%
			String id = (String) session.getAttribute("idKey");
			System.out.println(id);
			ArrayList<OrderDto> list = orderMgr.getOrder(id);
			if (list.size() == 0) {
		%>
		<tr>
			<td colspan="5">주문한 상품이 없습니다</td>
		</tr>
		<%
			} else {
				for (OrderDto ord : list) {
					ProductDto product = productMgr.getProduct(ord.getProduct_no());
		%>
		<tr style='text-align: center'>
			<td><%=ord.getNo()%></td>
			<td><%=product.getName()%></td>
			<td><%=ord.getQuantity()%></td>
			<td><%=ord.getSdate()%></td>
			<td>
				<%
					switch (ord.getState()) {
							case "1":
								out.println("접수");
								break;
							case "2":
								out.println("입금 확인");
								break;
							case "3":
								out.println("배송 준비");
								break;
							case "4":
								out.println("배송중");
								break;
							case "5":
								out.println("처리 완료");
								break;
							default:
								out.println("접수중");
								break;
							}
				%>
			</td>
		</tr>



		<%
			}
			}
		%>
	</table>
	<%@ include file="guest_bottom.jsp"%>
</body>
</html>