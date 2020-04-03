package aa.bb.pack4;

public class CoinIn {
	private int coin;
	private int jandon;

	// ========= CONSTRUCTOR ===================
	public CoinIn() {
	}

	// ========== GETTER & SETTER =============
	public void setCoin(int coin) {
		this.coin = coin;
	}

	public int getJandon() {
		return jandon;
	}

	// =========== METHOD ===================
	public String calc(int cupCount) {
		jandon = coin - (200 * cupCount);

		// 돈이 부족하다면 부족
		if (jandon < 0) {
			return "돈이 부족합니다 ";
		}
		else
			return "커피 " + cupCount + "잔과 잔돈 " + jandon + "원";
	}

}
