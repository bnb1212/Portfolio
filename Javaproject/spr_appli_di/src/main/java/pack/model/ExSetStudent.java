package pack.model;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ExSetStudent implements ExStudentInter {
	
	public String getStudent() {
		String student = "";
		try {

			System.out.println("작성자는 ? ");
			InputStreamReader reader = new InputStreamReader(System.in);
			BufferedReader breader = new BufferedReader(reader);

			student = breader.readLine();
		} catch (Exception e) {

		}
		return student;
	}
}
