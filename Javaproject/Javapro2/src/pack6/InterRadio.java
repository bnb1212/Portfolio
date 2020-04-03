package pack6;

//public class InterRadio implements InterVol, InterVol2
public class InterRadio implements InterVol2 {
	// ===== MEMBER =========
	private int v = 0;

	public void volUp(int v) {
		this.v += v;
	}

	public void volDown(int v) {
		this.v -= v;
	}

	public void volOff() {
		System.out.println("라디오 끄기");
	}

	public void volResume() {
		System.out.println("라디오 켜기");
	}

	public void show() {
		System.out.println("현재 볼륨은 " + v);
	}
}
