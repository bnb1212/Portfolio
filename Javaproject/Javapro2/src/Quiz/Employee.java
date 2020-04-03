package Quiz;

public abstract class Employee {
	// ==== MEMBER ===========
	private String irum;
	private int nai;

	// ==== CONSTUCTOR =======
	public Employee(String irum, int nai) {
		this.irum = irum;
		this.nai = nai;

	}

	// ==== METHOD ===========
	public abstract double pay();

	public abstract void print();

	public void display() {
		System.out.println("이름 : " + irum + "\n나이 : " + nai + "살 ");
	}
}
