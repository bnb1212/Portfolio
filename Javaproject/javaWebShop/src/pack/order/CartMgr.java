package pack.order;

import java.util.Hashtable;

public class CartMgr {
	private Hashtable hCart = new Hashtable();
	
	public void addCart(OrderBean obean) {
		String product_no = obean.getProduct_no();
		int quantity = Integer.parseInt(obean.getQuantity());
		
		if(quantity > 0) {
			// 동일 상품 주문 시 주문 수량만 증가
			if(hCart.containsKey(product_no)) { // containsKey(key)
				OrderBean temp = (OrderBean)hCart.get(product_no);
				quantity += Integer.parseInt(temp.getQuantity());
				temp.setQuantity(Integer.toString(quantity));
			}else { // 새 상품 주문 인 경우
				hCart.put(product_no, obean);
			}
		}
	}
	
	public Hashtable getCartList() {
	
		return hCart;
	}
	public void updateCart(OrderBean obean) {
		String product_no = obean.getProduct_no();
		hCart.put(product_no, obean);
	}
	public void deleteCart(OrderBean obean) {
		String product_no = obean.getProduct_no();
		hCart.remove(product_no);
	}
}
