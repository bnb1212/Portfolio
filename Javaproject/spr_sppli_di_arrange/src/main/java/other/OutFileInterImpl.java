package other;

import java.io.FileWriter;

public class OutFileInterImpl implements OutFileInter{
	private String filePath;
	
	public void setFilePath(String filePath) {
		this.filePath = filePath;
	}
	
	@Override
	public void outFile(String msg) {
		// TODO Auto-generated method stub
		try {
			FileWriter writer = new FileWriter(filePath);
			writer.write(msg);
			writer.close();
			System.out.println("파일 저장 성공");
		} catch(Exception e) {
			System.out.println("outfile err: " + e);
		}
	}

	@Override
	public void etc() {
		// TODO Auto-generated method stub
		
	}
}
