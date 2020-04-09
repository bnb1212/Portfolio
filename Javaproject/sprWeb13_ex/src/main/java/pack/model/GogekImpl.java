package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.stereotype.Repository;

import pack.controller.GogekBean;
@Repository
public class GogekImpl extends SqlSessionDaoSupport implements GogekInter {

	@Autowired
	public GogekImpl(SqlSessionFactory factory) { // setter로는 안들어감. 추상으로 받기때문에
		setSqlSessionFactory(factory);
	}

	@Override
	public List<GogekDto> selectGogek(String no) throws DataAccessException {
		return getSqlSession().selectList("selectGogek", no);
	}

}
