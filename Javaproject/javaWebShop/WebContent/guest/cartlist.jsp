<%@page import="pack.product.ProductDto"%>
<%@page import="pack.order.OrderBean"%>
<%@page import="java.util.Enumeration"%>
<%@page import="java.util.Hashtable"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<jsp:useBean id="cartMgr" class="pack.order.CartMgr" scope="session" />
<%-- 세션 끝날때까지 CartMgr객체 살아있어야 하기 때문에 scope 빼먹으면 안됨--%>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>상품 주문</title>
<script type="text/javascript" src="../js/script.js"></script>
<script type="text/javascript" src="../js/script2.js"></script>
<link href="../css/board.css" rel="stylesheet" type="text/css">
<script type="text/javascript">
function cartUpdate(form){
	form.flag.value="update";
	form.submit();
}

function cartDelete(form){
	form.flag.value="delete";
	form.submit();
}

function productDetail(no){
	document.detailFrm.no.value = no;
	document.detailFrm.submit();
}
</script>
</head>
<body>
	** 장바구니 목록 **
	<br>
	<%@ include file="guest_top.jsp"%>
	<table style="width: 80%">
		<tr style="background-color: cyan">
			<th>주문 상품</th>
			<th>조회</th>
			<th>수량</th>
			<th>수정/삭제</th>
			<th>조회</th>
		</tr>
		<%
			int totalPrice = 0;
			Hashtable hCart = cartMgr.getCartList();
			if (hCart.size() == 0) {
		%>
		<tr>
			<td colspan="5">주문 건수가 없습니다.</td>
		</tr>
		<%
			} else {
				Enumeration enu = hCart.keys();
				while (enu.hasMoreElements()) {
					OrderBean order = (OrderBean) hCart.get(enu.nextElement());
					ProductDto product = productMgr.getProduct(order.getProduct_no());
					int price = Integer.parseInt(product.getPrice()); // 주문 상품 낱개 가격
					int quantity = Integer.parseInt(order.getQuantity()); // 주문 수량
					int subTotal = price * quantity; // 소계 
					totalPrice += subTotal; // 총계
		%>
		<form action="cartproc.jsp" method="get">
			<input type="hidden" name="flag"> <input type="hidden"
				name="product_no" value="<%=product.getNo()%>">
			<tr>
				<td><%=product.getName()%></td>
				<td><%=subTotal%></td>
				<td><input type="text" style="text-align: center;"
					name="quantity" size="5" value='<%=order.getQuantity()%>'>
				</td>
				<td><input type="button" style="background-color: aqua;" value="수정" onclick="cartUpdate(this.form)"> /
				<input type="button" style="background-color: aqua;" value="삭제" onclick="cartDelete(this.form)"></td>
				<td><a href="javascript:productDetail('<%=product.getNo() %>')">상세보기</a></td>
			</tr>
		</form>
		<%
			}
			}
		%>
		<tr>
			<td colspan="5"><br>
			<br>
			<b>총 결제 금액 : <%=totalPrice%>원&nbsp;&nbsp;&nbsp; <a
					href="orderproc.jsp">[ 주문하기 ]</a>
			</b></td>

		</tr>
	</table>

	<%@ include file="guest_bottom.jsp"%>
	
<form action="productdetail_g.jsp" name="detailFrm">
<input type="hidden" name="no">
</form>
</body>
</html>