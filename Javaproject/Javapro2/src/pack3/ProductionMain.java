package pack3;

public class ProductionMain {
	
	public static void main(String[] args) {
		Production coffee = new Production("coffee", 600);
		
		coffee.setProductionDay("2020-01-28");
		
		coffee.display();
		coffee.setProductionDay("2020-01-01");
		coffee.display("Americano");
		coffee.setProductionDay("2020-01-15");
		coffee.display("Caramel_Maciatto", 5000);
	}
}
