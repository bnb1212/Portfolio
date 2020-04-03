package pack6;

public class VolumeRadio implements Volume{
	private int volLevel;
	
	public VolumeRadio() {
		volLevel = 0;
	}
	
	@Override
	public void volumeUp(int level) {
		volLevel += level;
		System.out.println("라디오 볼륨 올리면 " + volLevel);
		
	}
	
	@Override
	public void volumeDown(int level) {
		volLevel -= level;
		if(volLevel <0)
			volLevel = 0;
		System.out.println("라디오 볼륨 내리면 " + volLevel);
	}

}
