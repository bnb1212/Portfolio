package pack5;

public class HouseDog extends Dog{
	private String where = "집";
	
	public HouseDog(String name) {
		// TODO Auto-generated constructor stub
		super(name);
	}

	public void show() {
		System.out.println("거주 : " + where + " 안 ");
	}
	
	@Override
	public void print() {
		System.out.println(getName() + "는(은) " + where + "에 살고 있다");
	}
}
