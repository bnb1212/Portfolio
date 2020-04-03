package pack9;

public class SinhanBank {
	private int money = 10000; // 스레드의 공유 자원용

	public int getMoney() {
		return money;

	}

	public void setMoney(int money) {
		this.money = money;
	}

	public synchronized void saveMoney(int save) { // 입금. 쓰레드의 동기화
		int m = getMoney();
		try {
			Thread.sleep(2000);
		} catch (Exception e) {

		}
		setMoney(m + save);
	}

	public synchronized void minusMoney(int mon) { // 출금
		int m = getMoney();
		try {
			Thread.sleep(3000);
		} catch (Exception e) {
			
		}
		setMoney(m - mon);
	}
}
