package pack;

import other.OutFileInter;

public class MessageImpl implements MessageInter {
	private String name1, name2;// 생성자용
	private int year;
	
	private MyInfo myInfo;
	private String spec; // 프로퍼티용
	private MyInfo myInfo2;
	private OutFileInter fileInter;
	
	public MessageImpl(String name1, String name2, int year, MyInfo myInfo) { // Constuctor Injection 하는중
		this.name1 = name1; 
		this.name2 = name2;
		this.year = year;
		this.myInfo = myInfo;
	
		
		
	}
	
	
	public void setSpec(String spec) {
		this.spec = spec;
	}

	public void setMyInfo2(MyInfo myInfo2) {
		this.myInfo2 = myInfo2;
	}
	
	public void setFileInter(OutFileInter fileInter) {
		this.fileInter = fileInter;
	}
	
	public void sayHi() {
		// 출력 담당
		String msg = name1 + " " + name2;
		msg += "\n" + (year + 20);
		msg += "\n" + myInfo.myData();
		msg += "\n" + spec;
		msg += "\n" + myInfo2.myData();
		
		System.out.println(msg);

		fileInter.outFile(msg);
	}

}
