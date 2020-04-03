package pack5;

public class PolyTaxi extends PolyCar {
	// ============ MEMBER FIELD ==========
	private int passenger = 2;

	// ============ METHOD ============
	public void show() {
		System.out.println("Mr.택시");
	} // 자식 고유의 메소드는 부모클래스(PolyCar에서 호출할 수 없다)

	@Override
	public void dispData() {
		System.out.println("택시의 승객 수는 " + passenger);
	}

}
