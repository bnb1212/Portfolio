import java.io.PrintWriter;
import java.net.Socket;

public class NetTest3Client {
	public static void main(String[] args) {
		try {
			Socket socket = new Socket("192.168.0.80", 9999);
			
			PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
			
			out.println("kukuRu_kuku" + "\n");
			out.close();
			socket.close();
		} catch (Exception e) {
			System.out.println("Client err : " + e);
		}
	}
}
