package pack;

public class Message1 implements MessageInter{
	
	public Message1() {
	}
	
	
	@Override
	public void sayHello(String name) {
		System.out.println("안녕" + name + "씨");
	}

}
