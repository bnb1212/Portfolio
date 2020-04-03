package pack6;

public class FlyerAirplane implements Flyer{
	
	
	@Override
	public void fly() {
		System.out.println("엔진소리를 힘차게 내며 이란으로 날아감");
	}
	
	@Override
	public boolean isAnimal() {
		return false;
	}
}
