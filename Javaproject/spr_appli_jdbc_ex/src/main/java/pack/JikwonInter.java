package pack;

import java.util.List;

import javax.sql.DataSource;

import org.springframework.dao.DataAccessException;

public interface JikwonInter {
	void initList() throws DataAccessException;
	List<JikwonDto> getList();
}

