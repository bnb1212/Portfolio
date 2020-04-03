package pack5;

public final class Me extends Father { // 클래스에 final 걸면 상.속.불.가.
	public final int abc = 10; // 수정 불가
	
	public Me() {
		System.out.println("내 생성자!");
	}
	
	public void biking() {
		System.out.println("자전거로 전국 일주 여행");
	}
	@Override
	public int getNai() {
		return super.getNai();
	}
	
	public void showMeData() {
		
	}
}
