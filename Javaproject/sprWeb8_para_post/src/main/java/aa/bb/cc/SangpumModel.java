package aa.bb.cc;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

//@Repository
@Component
public class SangpumModel {
	public String ComputeData(SangpumBean bean) {
		String data= "품명 : " + bean.getSang()
					+ ", 금액  : " + (bean.getSu()*bean.getDan());
					
		return data;
	}
}
