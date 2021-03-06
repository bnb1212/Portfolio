package pack.controller;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import pack.model.MoneyInter;

public class MyProcess implements MyInter {
	private MoneyInter inter;
	private int re[];

	public MyProcess(MoneyInter inter) {
		this.inter = inter;
	}

	public void inputMoney() {
		try {
			InputStreamReader reader = new InputStreamReader(System.in);
			BufferedReader breader = new BufferedReader(reader);
			int myMoney = 0;
			System.out.println("금액 입력 : ");
			myMoney = Integer.parseInt(breader.readLine());
			re = inter.calcMoney(myMoney);
		} catch (Exception e) {
			System.out.println("inputMoney err : " + e);
		}
	}

	public void showResult() {
		/*
		 * String ss = ""; ss = "만원 : " + re[0] + "\n"; ss += "천원 : " + re[1] + "\n"; }
		 * // 문자열 더하기는 속도를 저하시키는 원인
		 */
		StringBuffer sb = new StringBuffer();
		sb.append("만원 : " + re[0] + "\n");
		sb.append("천원 : " + re[1] + "\n");
		sb.append("백원 : " + re[2] + "\n");
		sb.append("십원 : " + re[3] + "\n");
		sb.append("원 : " + re[4] + "\n");
		System.out.println(sb.toString());
	}
}