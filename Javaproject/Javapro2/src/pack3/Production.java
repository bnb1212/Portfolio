package pack3;

public class Production {
	private String name;
	private int price;
	private String productionDay;

	public Production(String name, int price) {
		this.name = name;
		this.price = price;
	}

	public void setProductionDay(String productionDay) {
		this.productionDay = productionDay;
	}

	public void display() {
		System.out.println("상품명 : " + name + " 가격 : " + price + " 생산일 : " + productionDay);
	}

	public void display(String name) {
		this.name = name;
		System.out.println("상품명 : " + name + " 가격 : " + price + " 생산일 : " + productionDay);
	}

	public void display(String name, int price) {
		this.name = name;
		this.price = price;
		System.out.println("상품명 : " + name + " 가격 : " + price + " 생산일 : " + productionDay);
	}
}
