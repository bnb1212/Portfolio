package pack2;

import pack3.Bank;

public class BankMain3 {
	public static void main(String[] args) {
		// 다른 프로젝트의 클래스는 import 불가. 물리적으로 프로젝트 내에 복사해 와야함
		Bank joe = new Bank();
		System.out.println(joe.getMoney());
	}
}
