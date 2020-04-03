package pack5;

public class Dog {
	private String name = "개";

	public Dog() {

	}

	public Dog(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public String callName() {
		return "종류 : " + name;
	}
	public void print() {
		System.out.println(name + " : 한국에 살고 있다");
		
	}
}
