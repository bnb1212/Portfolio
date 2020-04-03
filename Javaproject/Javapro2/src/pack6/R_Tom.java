package pack6;

public class R_Tom implements Resume {
	private String irum, phone, juso;

	// ====== CONSTRUCTOR ============
	public R_Tom() {

	}
	// ====== METHOD =================
	@Override
	public void setIrum(String irum) {
		this.irum = irum;
	}

	@Override
	public void setPhone(String phone) {
		this.phone = phone;
	}

	@Override
	public void print() {
//		Resume.SIZE = "b5"; // final 변수이므로 수정 불가
		System.out.println("이력서 용지 규격은 " + Resume.SIZE);
		System.out.println("이름 : " + irum + ", 전화  : " + phone + ", 주소 : " + juso);
		playJava(true);
		Resume.changeData();
	}
	
	public void setJuso(String juso) {
		this.juso = juso;
	}
	
	void abc() {
		System.out.println("톰의 고유 메소드");
	}
}
