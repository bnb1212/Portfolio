package Quiz;

public class Salesman extends Regular {
	// ===== MEMBER ============
	private int sales;
	private double commission;

	// ===== CONSTRUCTOR =======
	public Salesman(String irum, int nai, int salary, int sales, double commission) {
		super(irum, nai, salary);
		this.sales = sales;
		this.commission = commission;
	}

	// ===== METHOD ============
	@Override
	public double pay() {
		return super.pay() + (sales * commission);
	}

	@Override
	public void print() {
		System.out.println();
		System.out.println("*** 영업직 ***");
		display();
		System.out.println("수령액 : " + pay());

	}

}
