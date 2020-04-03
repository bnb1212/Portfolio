package aa.bb.pack4;

public class PohamCar { // 여러개의 부품(클래스)들을 조립해 완성차를 만드는 클래스

	int speed = 0;
	String ownerName, turnMessage;
	PohamHandle handle; // 클래스의 포함 ( has a 관계 )
	// 생성자(Constructor)
	public PohamCar(String name) {
		ownerName = name;
		handle = new PohamHandle();
	}

	void turnHandle(int q) {
		if (q > 0)
			turnMessage = handle.rightTurn(q);
		if (q < 0)
			turnMessage = handle.leftTurn(q);
		if (q == 0)
			turnMessage = handle.straight(q);

	}

}
