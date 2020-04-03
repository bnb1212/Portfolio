package pack5;

public class JepumMain {
	public static void main(String[] args) {
//		Jepum jepum = new Jepum(); // 추상메소드이기 떄문에 객체화 할수 없다!
		
		Jepum jepum = null;
		
		Jepum_Tv tv = new Jepum_Tv();
		jepum = tv; // 이걸 위해서 추상화를 하는 것
		jepum.volumeControl();
		
		Jepum_Radio radio = new Jepum_Radio();
		jepum = radio;
		jepum.volumeControl();
		
	}
	
}
