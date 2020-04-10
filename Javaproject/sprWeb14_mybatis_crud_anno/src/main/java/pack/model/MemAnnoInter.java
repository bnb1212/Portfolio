package pack.model;

import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import pack.controller.MemBean;

public interface MemAnnoInter {

	@Select("select * from mem")
	List<MemDto> getDataAll();
	
	@Select("select * from mem where num=#{num}")
	MemDto selectPart(String num);
	
	@Insert("insert into mem values(#{num}, #{name}, #{addr})")
	boolean insertData(MemBean bean);
	
	@Update("update mem set name=#{name}, addr=#{addr}, where num=#{num}")
	boolean updateData(MemBean bean);
	
	@Delete("delete from mem where num=#{num}")
	boolean deleteData(String num);
	
	
}
