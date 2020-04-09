package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Repository;

import pack.controller.SangpumBean;

@Repository
public class SangpumImpl extends SqlSessionDaoSupport implements SangpumInter {

	@Autowired
	public SangpumImpl(SqlSessionFactory factory) { // setter로는 안들어감. 추상으로 받기때문에
		setSqlSessionFactory(factory);
	}

	
	@Override
	public List<SangpumDto> selectList() throws DataAccessException {
		return getSqlSession().selectList("selectDataAll");
	}
	
	@Override
	public List<SangpumDto> search(SangpumBean bean) throws DataAccessException {
		return getSqlSession().selectList("selectSearch", bean);
	}

}
