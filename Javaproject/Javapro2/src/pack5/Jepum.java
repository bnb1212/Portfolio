package pack5;

public abstract class Jepum {
	public int volume = 0;
	
	public Jepum() {
		System.out.println("제품 추상클래스 생성자!");
	}
	
	abstract public void volumeControl();
	
	public void volumeShow() {
		System.out.println("소리 크기 : " + volume);
	}
}
