package pack5;

public class Jepum_Tv extends Jepum{
	
	public Jepum_Tv() {
		System.out.println("TV 생성자");
	}
	
	@Override
	public void volumeControl() { // 추상을 구체화시켜주어야 함
		 System.out.println("TV 소리 조절");
		
	}
}
