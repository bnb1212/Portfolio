package pack9;

public class SinhanBankMain {
	public static SinhanBank myBank = new SinhanBank();

	public static void main(String[] args) {
		System.out.println("초기 예금액 : " + myBank.getMoney());
		Kim kim = new Kim();
		KimWife wife = new KimWife();
		
		kim.start();
		wife.start(); // 두개의 스레드는 자원을 공유하는 것이 아니다ㅏㅏㅏ
//		초기 예금액 : 10000
//		남편 예금 후 잔고 : 15000
//		아내 출금 후 잔고 : 7000
		
		
	}
}
