package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class DataDao extends SqlSessionDaoSupport{

	@Autowired
	public DataDao(SqlSessionFactory factory) {
		setSqlSessionFactory(factory);
	}
	
	public List<JikwonDto> jikwonList(String buser_name){
		System.out.println(buser_name);
		List<JikwonDto> list = getSqlSession().selectList("selectJikwonData", buser_name);
		
		return list;
	}
	
	public List<GogekDto> gogekList(String jikwon_no){
		System.out.println(jikwon_no);
		List<GogekDto> list = getSqlSession().selectList("selectGogekData", jikwon_no);
		
		return list;
	}
	
	
}
