package Quiz;

public class Regular extends Employee {
	// ===== MEMBER ============
	private int salary;

	// ===== CONSTRUCTOR =======
	public Regular(String irum, int nai, int salary) {
		super(irum, nai);
		this.salary = salary;

	}

	// ===== METHOD ============

	@Override
	public double pay() {
		return salary;
	}

	@Override
	public void print() {
		System.out.println();
		System.out.println("*** 정규직 ***");
		display();
		System.out.println("고정급 : " + pay());

	}
}