package pack8;

public class Quiz2_2Dto {
	//상품은 새우깡과 감자깡 둘만 고정
	// 100 -> 강북, 200-> 강남, 300-> 강서, 그외 -> 기타
	// 감자깡 소계 및 금액, 새우깡 소계 및 금액
	private String product;
	private int areacode, amount;
	
	public String getProduct() {
		return product;
	}
	public void setProduct(String product) {
		this.product = product;
	}
	public int getAreacode() {
		return areacode;
	}
	public void setAreacode(int areacode) {
		this.areacode = areacode;
	}
	public int getAmount() {
		return amount;
	}
	public void setAmount(int amount) {
		this.amount = amount;
	}
	
	
}
