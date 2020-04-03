package Quiz;

public class Temporary extends Employee {
	// ==== MEMBER ==========
	private int ilsu;
	private int ildang;

	// ===== CONSTRUCTOR =====
	public Temporary(String irum, int nai, int ilsu, int ildang) {
		super(irum, nai);
		this.ilsu = ilsu;
		this.ildang = ildang;
	}
	// ===== METHOD =========
	@Override
	public double pay() {
		return ilsu * ildang;
	}

	@Override
	public void print() {
		System.out.println();
		System.out.println("*** 임시직 ***");
		display();
		System.out.println("월급 : " + pay() + "원");

	}

}
