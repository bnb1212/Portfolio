package pack;

//핵심 로직 클래스
public class MessageImpl implements MessageInter{
	private String name;
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void sayHi() {
		System.out.println("안녕 " + name + "님! 비지니스 로직 처리 중");
		//...
	}
}
