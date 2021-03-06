package pack.controller;

import pack.model.DataDaoInter;
import pack.model.DataDaoImpl;

public class SelectServiceImpl implements SelectService {
	//private DataDaoimpl daoImpl;
	private DataDaoInter daoInter; 
	
	public SelectServiceImpl(DataDaoInter daoInter) {
		// 생성자를 통해 DataDaoInter 객체에 파생 객제츼 주소를 치환
		System.out.println("SelectServiceImpl 생성자");
		this.daoInter = daoInter;
	}

	public void selectProcess() {
		System.out.println("selectProcess에서 DaoInter의 메소드 수행");
		daoInter.selectDb();
	}
}
