package pack.admin;


import java.util.List;

import org.apache.ibatis.annotations.Select;

import pack.equip.EquipDto;

public interface SqlMapperInter {
	@Select("select * from admin")
	public List<AdminDto> selectAdmin();
	/*
	@Insert("insert into membertab(id, name, passwd, reg_date) values (#{id},#{name},#{passwd},now())")
	public int insertData(DataFormBean bean);
	
	@Update("update membertab set name=#{name} where id=#{id}")
	public int updateData(DataFormBean bean);
	
	@Delete("delete from membertab where id=#{id}")
	public int deleteData(String id);
	*/

	public List<EquipDto> selectEquip();
	
}
