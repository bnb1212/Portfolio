package aa.bb.pack4;

public class PohamCarMain {
	
	public static void main(String[] args) { // third party
		PohamCar tom = new PohamCar("jiun");
		
		tom.turnHandle(30);
		System.out.println(tom.ownerName + "의 회전량은 " + tom.turnMessage + " " +
				tom.handle.quantity);
		tom.turnHandle(0);
		System.out.println(tom.ownerName + "의 회전량은 " + tom.turnMessage + " " +
				tom.handle.quantity);
		
		System.out.println();
		PohamCar kildong = new PohamCar("길동");
		kildong.turnHandle(-10);
		System.out.println(kildong.ownerName + "의 회전량은 " + kildong.turnMessage + " " +
				kildong.handle.quantity);
	}
}
