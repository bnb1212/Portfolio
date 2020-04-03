package pack8;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;

public class IoTest1 {
	public static void main(String[] args) throws Exception {
		// 1byte 단위의 입출력
//		System.out.println("1byte 입력");
//		int a = System.in.read(); // 'a' -> 1byte "a" -> 2byte (문자열의 끝에 null)
		// read()는 한바이트만 받음
//		System.out.println("a:" + a + " "+ (char)a);

		OutputStreamWriter os = new OutputStreamWriter(System.out);
//		byte imsi = 98;
//		os.write(imsi);
//		os.flush(); // flush는 버퍼를 깨끗이 비운다. close는 가비지컬렉터에 쓰던 메모리 해제요청
//		os.close();

		BufferedWriter bw = new BufferedWriter(os, 1024);
		PrintWriter out = new PrintWriter(bw);
		out.println(123);
		out.print("문자열 출력");
		out.close();
		bw.close();
		os.close();
		System.out.println("문자열 출력");

		System.out.println();
		
		File f = new File("c:/work/iotest.txt");
		FileWriter fw = new FileWriter(f);
		BufferedWriter bw2 = new BufferedWriter(fw, 1024);
		PrintWriter out2 = new PrintWriter(bw2);
		 
		out.println("날씨가 좋네");
		out.println("내일까지");
		out.println("견디자");
		
		out2.close();
		bw2.close();
		fw.close();
		
	}
}
