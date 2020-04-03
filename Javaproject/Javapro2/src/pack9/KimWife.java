package pack9;

public class KimWife extends Thread{ //김씨 고객의 배우자
	@Override
	public void run() {
		SinhanBankMain.myBank.minusMoney(3000);
		System.out.println("아내 출금 후 잔고 : " + SinhanBankMain.myBank.getMoney());
	}

}
