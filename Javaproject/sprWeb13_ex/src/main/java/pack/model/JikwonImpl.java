package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Repository;

import pack.controller.JikwonBean;

@Repository // 로 해두었기 떄문에 스스로 객체 생성
public class JikwonImpl extends SqlSessionDaoSupport implements JikwonInter {

	@Autowired
	public JikwonImpl(SqlSessionFactory factory) { // setter로는 안들어감. 추상으로 받기때문에
		setSqlSessionFactory(factory);
	}

	
	@Override
	public List<JikwonDto> selectList() throws DataAccessException {
		return getSqlSession().selectList("selectJikwonAll");
	}
	

}
