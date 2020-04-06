package pack.business;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Service;

import pack.model.DataDto;
import pack.model.SangpumInter;

@Service
@ComponentScan("pack.model")
public class BusinessImpl implements BusinessInter {
	@Autowired
	@Qualifier("sangpumImpl")
	private SangpumInter inter;

	public void dataList() {
		List<DataDto> list = inter.selectDataAll();
		// 출력
		for (DataDto d : list) {
			System.out.println(d.getCode() + " " + d.getSang() + " " + d.getSu() + " " + d.getDan() + " ");
		}
	}

	

}
