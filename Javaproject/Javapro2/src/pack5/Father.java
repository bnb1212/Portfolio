package pack5;

public class Father extends GrandFa { // 부모, super, parent, 조상
										// 자식, sub, child, 파생
	// ==========MEMBER FIELD=============
	private int nai = 55;
	private int house = 1; // 현재 클래스의 고유 멤버
	public String gabo = "갤럭시 1세대 초판한정 물량"; // 부모클래스의 멤버 필드는 은닉화
	protected String gahun = "Understand a Polymorphism";

	// ==========CONSTRUCTOR===============
	public Father() {
		super(2); // 부모 생성자 호출.argument에 의해 선택적으로 호출
		System.out.println("아버지 생성자랍니다");
	}

	// ===========METHOD===================
	@Override // annotation : 부모 메소드와 동일해야함을 강요
	public int getNai() { // 부모 메소드와 동일한 메소드 선언 : 메소드 오버라이딩
//		int nai = 22;		
		return this.nai;		// 메소드에 final 걸면 파생 클래스에서 오버라이드 불가
	}

	@Override
	public String say() {
//		return super.say();
		return "JAVA Programmer 전문가가 되자";
	}
	
	public void showdata() {
		String gabo = "갤럭시탭 최신";
		
		System.out.println("가보 : " + gabo);
		System.out.println("가보 : " + this.gabo);
		System.out.println("가보 : " + super.gabo);
		
		System.out.println("나이 : " + getNai());
		System.out.println("나이 : " + getNai());
		System.out.println("나이 : " + super.getNai());
		
		eat();
		this.eat();
		super.eat();
	}
}
