package pack5;

public class GrandFa {
	// ========MEMBER FIELD============
	private int nai = 80;
	public String gabo = "아이폰 1세대 초판한정 물량";
	protected String gahun = "Understand a Object.";

	// ========CONSTRUCTOR=============
	public GrandFa() {
		// TODO Auto-generated constructor stub
		System.out.println("할아버지 생성자");
	}

	public GrandFa(int nai) {
		this(); // 현재 클래스의 생성자 
		this.nai = nai;
	}

	// ============METHOD===============
	public String say() {
		return "할아버지 말씀 : Be a Data Scientist.";
	}

	public void eat() {
		System.out.println("밥은 맛있게 ");
	}

	public int getNai() {
		return nai;
	}
	
}
