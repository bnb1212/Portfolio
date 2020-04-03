package pack.exam;

import java.io.Reader;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class SqlMapConfig2 {
	public static SqlSessionFactory sqlSession; // sql 사용시 필요 메소드를 저장

	static {
		String source = "pack/exam/Configuration2.xml";
		try {
			Reader reader = Resources.getResourceAsReader(source);
			sqlSession = new SqlSessionFactoryBuilder().build(reader);
			reader.close();
		} catch (Exception e) {
			System.out.println("SqlMapCon err :" + e);
		}

	}

	public static SqlSessionFactory getSqlSession() {
		return sqlSession;
	}

}
