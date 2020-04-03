package Quiz;

public class Manager extends Regular {
	// ===== MEMBER ==========
	private double incentive;

	// ===== CONSTRUCTOR =====
	public Manager(String irum, int nai, int salary) {
		super(irum, nai, salary);
	}

	// ===== METHOD ==========

	@Override
	public double pay() {
		if (super.pay() >= 2500000)
			incentive = super.pay() * 0.6;
		else if (super.pay() >= 2000000)
			incentive = super.pay() * 0.5;
		else
			incentive = super.pay() * 0.4;
		return super.pay() + incentive;
	}

	@Override
	public void print() {
		System.out.println();
		System.out.println("*** 관리직 ***");
		display();
		System.out.println("수령액 : "+pay());
	}
}