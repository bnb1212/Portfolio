package pack8;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.StringTokenizer;

public class IoTest5 {
	public static void main(String[] args) {
		// 전국 도서관 자료 읽기 : data.go.kr
		try {
			File file = new File("c:/work/전국도서관표준데이터.csv");
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);

			int count = 0;
			System.out.println("도서관명\t시도명\t시군구명");
			while (true) {
				count++;
				String ss = br.readLine();
				ss = br.readLine();
				if (ss == null || count > 30)
					break;
				StringTokenizer tok = new StringTokenizer(ss, ",");
				String s1 = tok.nextToken();
				String s2 = tok.nextToken();
				String s3 = tok.nextToken();

				System.out.println(s1 + "\t" + s2 + "\t" + s3);
			}
		} catch (Exception e) {
			System.out.println("err : " + e);
		}

	}
}
