package pack.mybatis;

import java.io.Reader;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import pack.admin.SqlMapperInter;
import pack.equip.SqlMapperInter2;
import pack.qnaboard.SqlMapperInter3;
import pack.reviewboard.SqlMapperInter4;

public class SqlMapConfig {
	public static SqlSessionFactory sqlSession; // sql 사용시 필요 메소드를 저장

	static {
		String source = "pack/mybatis/Configuration.xml";
		try {
			Reader reader = Resources.getResourceAsReader(source);
			sqlSession = new SqlSessionFactoryBuilder().build(reader);
			reader.close();
			
			Class[]	mappers = {SqlMapperInter.class, SqlMapperInter2.class, SqlMapperInter3.class, SqlMapperInter4.class};
			for(Class m:mappers) {
				//Mapper 등록
				sqlSession.getConfiguration().addMapper(m);
			}
			
		} catch (Exception e) {
			System.out.println("SqlMapCon err :" + e);
		}

	}

	public static SqlSessionFactory getSqlSession() {
		return sqlSession;
	}

}
