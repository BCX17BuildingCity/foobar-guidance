import org.jsoup.nodes.Document;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.*;

import javax.xml.bind.DatatypeConverter;

/*import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.apache.commons.lang3.StringUtils;

import javax.xml.bind.DatatypeConverter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.List;*/

public class Main {

	public static void main(String[] args) throws UnknownHostException, IOException {
		// TODO Auto-generated method stub
		CameraConnector camCon = new CameraConnector();

		String camResponse = camCon.connectTo("100.103.1.215",
				"/rcp.xml?command=0x0b4a&type=P_OCTET&direction=READ&num=1");
		
		String camResponsesfh = camResponse.replaceAll("\\s+","");
		System.out.println("->" + camResponsesfh);
		String counter = camResponsesfh.substring(6, 134);
		System.out.println("-->" + counter);
		String value =  camResponsesfh.substring(134, 142);
		counter = counter.replaceAll("00", "");
		System.out.println("v: " + value);
		
		System.out.print(getString(counter));
		System.out.print(getInteger(value));
		
		
		
		
		
		/*
		byte[] s = DatatypeConverter.parseHexBinary(camResponsesfh);
		String myString = new String(s, "ISO-8859-1");
		System.out.println("[" + myString + "]");
		/*
        String hexMessage = "b0c20f0b004b0004014000b4004d000280000041002678004000000000000000006400000051eb85002e147b";
        byte[] si = DatatypeConverter.parseHexBinary(hexMessage);
        System.out.print(new String(si)+"");
		
        
	    for (int i = 3; i < s.length-1; i+=2) {
	    	
	        //output.append((char)Integer.parseInt(str, 16));
	    	byte[] temp = {s[i], s[i+1]};
	    	String tempStr = new String(temp, "US-ASCII");
	    	System.out.println(tempStr.replaceAll("\n", "")+"blub");
	    	//new String((temp, "ASCII");
	        //System.out.print(((char)Integer.parseInt(Byte.toString(s[i]))) + "-");
	        
	    }
	    //System.out.println(s.toString());
		//String result = new String(, "UTF-8");
		//System.out.println(result);
        
        
        
        
        
        
        
        /*
		String hostName = "100.127.9.1";
		int portNumber = 1337;
		
		try{
			Socket dataSocket = new Socket(hostName, portNumber);
			DataOutputStream dOut = new DataOutputStream(dataSocket.getOutputStream());

			// Send first message
			dOut.writeByte(1);
			dOut.writeUTF("This is the first type of message.");
			dOut.flush(); // Send off the data
			
		} catch (UnknownHostException e) {
		    System.err.println("Caught UnknownHostException: " + e.getMessage());
		} catch (UnknownError e){
			System.err.println("Caught UnknownError: " + e.getMessage());
		}


*/
	}

	private static String getString(String byteString) {
		StringBuilder output = new StringBuilder();
	    for (int i = 0; i < byteString.length(); i+=2) {
	        String str = byteString.substring(i, i+2);
	        output.append((char)Integer.parseInt(str, 16));
	    }
	    return output.toString();
	}
	
	private static int getInteger(String byteString) {
		return Integer.parseInt(byteString);
		}

}
