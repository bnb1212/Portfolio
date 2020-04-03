package pack.auto2;

import org.springframework.stereotype.Component;

import pack.auto.SenderInter;

@Component("s2")
public class Sender2 implements SenderInter {
	public void show() {
		System.out.println("show 메소드2 수행");
	}
}
