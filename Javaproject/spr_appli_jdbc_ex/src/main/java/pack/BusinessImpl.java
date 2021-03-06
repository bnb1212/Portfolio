package pack;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class BusinessImpl implements BusinessInter {
	@Autowired
	private JikwonInter jikwoninter;

	
	public void dataList() {
		List<JikwonDto> list;
		jikwoninter.initList();
		
		System.out.println("==== 직원정보 ==== ");
		System.out.println("사번\t직원명\t부서명\t직급");
		
		
		for(JikwonDto s:jikwoninter.getList()) {
			System.out.println(s.getJikwon_no() + "\t" 
								+ s.getJikwon_name() + "\t"
								+ s.getBuser_name() + "\t"
								+ s.getJikwon_jik());
			
		}
		System.out.println("인원수 : " + jikwoninter.getList().size());
		
	}
	

}
