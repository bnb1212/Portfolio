package pack5;

public class AniLion extends Animal {

	@Override 
	public String callName() {
		return "사자";
	}

	@Override
	public String eat() {
		return "동물";
	}

	@Override
	public String action() {
		return "밤";
	}

	@Override
	protected void print() {
	    System.out.println("사자 클래스에서 선택적으로 오버라이드");
	}
	
	public void eatOther() {
		System.out.println("가끔은 물도 마심");
	}
}
