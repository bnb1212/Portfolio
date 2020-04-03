package pack6;

public class FlyerBall extends FlyerAdapter{
	
	@Override
	public void fly() {
		System.out.println("야구공이 날아감");
	}
	
	public static void main(String[] args) {
		new FlyerBall().fly();
	}
}
