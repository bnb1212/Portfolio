package javapro4_normal;

import org.bson.*;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;

public class DbMongo {

	public DbMongo() {
		try {
			MongoClient client = new MongoClient("localhost", 27017);
			MongoDatabase db = client.getDatabase("test"); 

			MongoCollection<Document> collection  = db.getCollection("user");
			System.out.println("건수 : " + collection.countDocuments());
			
			Document doc = collection.find().first();
			System.out.println("첫번째 자료 : " + doc.toJson());
			
			System.out.println();
//			FindIterable<Document> iter = collection.find();
//			MongoCursor<Document> cursor = iter.iterator();
//			MongoCursor<Document> cursor = collection.find().iterator();
			MongoCursor<Document> cursor = collection.find().limit(2).iterator();
			
			// 자료 추가
			Document ins_doc = new Document("name", "나이스").append("age", "33").append("job", "음악가");
			collection.insertOne(ins_doc);
			/*
			while(cursor.hasNext()) {
//				Document document = cursor.next();
//				String jsonResult = document.toJson();
				String jsonResult = cursor.next().toJson();
				System.out.println(jsonResult);
			}
			*/
			cursor = collection.find().iterator();
			while(cursor.hasNext()) {
				Document doc2 = cursor.next();
				System.out.println("이름 : " + doc2.get("name") 
								+ ", 나이 : " + doc2.get("age")
								+ ", 직업 : " + doc2.get("job")); 
				
			}
		} catch (Exception e) {
			// TODO: handle exception
		}
	}
	
	public static void main(String[] args) {
		new DbMongo();
	}
}
