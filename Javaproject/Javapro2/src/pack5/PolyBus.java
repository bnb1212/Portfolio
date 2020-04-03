package pack5;

public class PolyBus extends PolyCar {
	// ============ MEMBER FIELD ==========
	private int passenger = 10;

	// ============ METHOD ============
	public void show() {
		System.out.println("버스");
	} // 자식 고유의 메소드는 부모클래스(PolyCar에서 호출할 수 없다)

	@Override
	public void dispData() {
		System.out.println("버스의 승객 수는 " + passenger);
		System.out.println("버스의 속도는 " + speed);
	}

}
