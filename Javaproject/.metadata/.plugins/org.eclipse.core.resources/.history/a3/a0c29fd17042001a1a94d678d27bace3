package aa.bb.pack4;

import java.util.Scanner;

public class Machine {
	private int cupCount;
	CoinIn ci = new CoinIn();
	
	public Machine() {
		
	}
	
	// ===========GETTER & SETTER============
	public void setCupCount(int cupCount) {
		this.cupCount = cupCount;
	}
	
	// ===============METHOD=================
	public void showData() {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("동전을 입력하세요 : ");
		ci.setCoin(sc.nextInt());
		System.out.println("몇 잔을 원하시나요 : ");
		cupCount = sc.nextInt();
		
		System.out.println(ci.calc(cupCount));
		sc.close();
	}
	
	
}
