package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;


@Repository
public class DataDao extends SqlSessionDaoSupport{ // 어노테이션 쓸땐 extends할 필요 없다
	@Autowired
	public DataDao(SqlSessionFactory factory) {
		setSqlSessionFactory(factory);
		
	}
	
	public List<SangpumDto> sangpumList(){
		List<SangpumDto> list = getSqlSession().selectList("selectDataAll");
		return list;
	}

	
	

}
