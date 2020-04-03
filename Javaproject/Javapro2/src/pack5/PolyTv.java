package pack5;

public class PolyTv extends PolyProduct{
	
	@Override
	public void volumeControl() {
		System.out.println("TV 사운드 조절 후 : " + getVolume());
	}

	public void tvShow() {
		System.out.println("RV 고유 메소드");
	}
}
