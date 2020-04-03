package pack6;

public class FlyerUtil {
	public static void show(Flyer f) {
		f.fly();
		System.out.println("동물인가용? " + f.isAnimal());
	}
}
