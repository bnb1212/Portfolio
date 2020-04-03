package pack6;

public class VolumeTv implements Volume{
	private int volLevel;
	
	public VolumeTv() {
		volLevel = 0;
	}
	
	@Override
	public void volumeUp(int level) {
		volLevel += level;
		System.out.println("티비 볼륨 올리면 " + volLevel);
		
	}
	
	@Override
	public void volumeDown(int level) {
		volLevel -= level;
		if(volLevel <0)
			volLevel = 0;
		System.out.println("티비 볼륨 내리면 " + volLevel);
	}

}
