package etc_pack;

//import pack3.Bank;
//import pack3.Animal;
import pack3.*; // 권장하지 않음 -> 낭비가 있음


public class BankMain2 {
	public static void main(String[] args) {
		Bank john = new Bank();
		// System.out.println(john.imsi); // default는 같은 패키지, private은 같은 클래스
		System.out.println(john.imsi2); // public은 같은 프로젝트
		System.out.println(john.getMoney());
	}
}
