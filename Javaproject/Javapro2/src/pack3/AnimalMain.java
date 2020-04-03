package pack3;

public class AnimalMain {
	public static void main(String[] args) {
		Animal tiger = new Animal();
		tiger.display();
		tiger.display(5);
		tiger.display("tiger");
		tiger.display("tiggger", 2);
		tiger.display(3, "giter");
		System.out.println("-----------");
		Animal dog = new Animal();
		dog.display();
		
		Animal hen = new Animal(2);
		hen.display();
		
		Animal wolfdog = new Animal("늑대");
		wolfdog.display();
		
		
	}
}
