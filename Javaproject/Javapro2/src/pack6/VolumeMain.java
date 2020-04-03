package pack6;

public class VolumeMain {

	public static void main(String[] args) {
		// 인터페이스로 상속
//		Volume volume = new Volume(): // 인터페이스는 객체 생성 불가
		Volume volume;
		
		// ===== METHOD =======
		VolumeRadio radio = new VolumeRadio();
		VolumeTv tv = new VolumeTv();
		radio.volumeUp(30);
		radio.volumeDown(5);
		tv.volumeUp(25);
		tv.volumeDown(3);
		
		System.out.println();
		volume = radio;
		volume.volumeUp(1);
		volume = tv;
		volume.volumeUp(1);
		
		System.out.println();
		Volume v[] = new Volume[2];
		v[0] = radio;
		v[1] = tv;
		
		for(Volume kbs:v) {
			kbs.volumeDown(2);
		}
	}

}
