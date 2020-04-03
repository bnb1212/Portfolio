package pack6;

public interface Volume {
	void volumeUp(int level); // public abstract void volumeUp(int level);
								// 추상클래스, 추상메소드 -> 다형성을 위해 오버라이딩을 강요

	void volumeDown(int level);
	// ...
//	public void print() {
//		// 인터페이스에는 일반 메소드 X
//	}
	
}
