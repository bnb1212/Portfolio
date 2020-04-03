package pack6;

public class FlyerMain {
	public static void main(String[] args) {
		System.out.println(Flyer.FAST);

		FlyerBird bird = new FlyerBird();
		bird.fly();
		FlyerAirplane airplane = new FlyerAirplane();
		airplane.fly();
		
		System.out.println();
		FlyerUtil.show(bird); // static 영역은 크지 않다는것 다시한번 상기할것
		FlyerUtil.show(airplane); // 이런거시 다형성이다아아아아아아아아아
	}
}
