package pack.auto;

import org.springframework.stereotype.Component;

@Component("s1")
public class Sender implements SenderInter {
	public void show() {
		System.out.println("show 메소드 수행");
	}
}
