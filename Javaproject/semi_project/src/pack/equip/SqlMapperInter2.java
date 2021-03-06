package pack.equip;


import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;

public interface SqlMapperInter2 {
	@Select("select * from equip")
	public List<EquipDto> selectEquip();
	
	@Select("select equip_no, equip_name, equip_stock, equip_info, equip_image from equip where equip_no=#{no}")
	public EquipDto selectEquipOne(String no);
	
	@Insert("insert into equip (equip_name, equip_stock, equip_info, equip_image) values (#{equip_name},#{equip_stock},#{equip_info}, #{equip_image})")
	public int insertEquip(EquipFormBean bean);
	/*
	@Update("update membertab set name=#{name} where id=#{id}")
	public int updateData(DataFormBean bean);
	*/
	@Delete("delete from equip where equip_no=#{equip_no}")
	public int deleteEquip(String equip_no);
	
	
}
