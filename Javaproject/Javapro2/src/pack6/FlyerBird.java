package pack6;

public class FlyerBird implements Flyer{
	
	
	@Override
	public void fly() {
		System.out.println("날개를 휘저으며 숲속으로 날아감");
	}
	
	@Override
	public boolean isAnimal() {
		return true;
	}
}
