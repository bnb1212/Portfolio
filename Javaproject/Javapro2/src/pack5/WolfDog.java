package pack5;

public class WolfDog extends Dog {
	private String where = "산";

	public WolfDog(String name) {
		super(name);
	}

	public WolfDog(String name, String where) {
		super(name); // 생성자는 다른 state보다 먼저 적어줘야 함
		this.where = where; // 위 아래 순서 바뀌면 안됨
	}

	public void show() {
		System.out.println("거주 : " + where + " 안 ");
	}

	@Override
	public void print() {
		System.out.println(getName() + "는(은) " + where + "에 살고 있다");
	}
	
	public void display() {
		print();
		this.print();
		super.print();
	}
}
