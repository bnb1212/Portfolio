package pack8;

public class StudentDTO {
	// 자료형(Type)이 다른 여러개의 기억장소(변수)를 레코드로 묶어서 이용할 수 있음
	private String hakbun, irum;
	private int jumsu;

	public String getHakbun() {
		return hakbun;
	}

	public void setHakbun(String hakbun) {
		this.hakbun = hakbun;
	}

	public String getIrum() {
		return irum;
	}

	public void setIrum(String irum) {
		this.irum = irum;
	}

	public int getJumsu() {
		return jumsu;
	}

	public void setJumsu(int jumsu) {
		this.jumsu = jumsu;
	}

}
