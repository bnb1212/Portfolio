package pack8;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class BinaryProcess {
	public static void main(String[] args) throws Exception {
		BinaryData data = new BinaryData();
		
		File dir = new File("c:/work/");
		File file = new File(dir, "abcbi.data");
		FileOutputStream fo = new FileOutputStream(file);
		BufferedOutputStream bo = new BufferedOutputStream(fo, 1024);
		ObjectOutputStream oo = new ObjectOutputStream(bo);
		oo.writeObject(data);
		oo.close();
		bo.close();
		fo.close();
		System.out.println("저장 성공");
	
		System.out.println();
		// 이진 자료 파일 읽기
		File file2 = new File(dir, "abcbi.data");
		FileInputStream fis = new FileInputStream(file2);
		BufferedInputStream bi = new BufferedInputStream(fis, 1024);
		ObjectInputStream oi = new ObjectInputStream(bi);
		
		Object obj = oi.readObject();
		BinaryData data2 = (BinaryData)obj;
		System.out.println(data2.i);
		System.out.println(data2.d);
		System.out.println(data2.s1);
		System.out.println(data2.s2);
		
		oi.close();
		bi.close();
		fis.close();
	}
}
