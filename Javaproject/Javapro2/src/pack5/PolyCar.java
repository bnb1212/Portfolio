package pack5;

public class PolyCar {

	protected int speed = 50; // protected를 보면 부모클래스로 쓰이겠구나 짐작해볼 수 있다

	public PolyCar() {
		System.out.println("나는야 자동차");
	}

	public void dispData() {
		System.out.println("속도는 " + speed);
	}

	public int getSpeed() {
		return speed;
	}
}
