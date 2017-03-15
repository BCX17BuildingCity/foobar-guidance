import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import javax.xml.bind.DatatypeConverter;
import java.io.IOException;
import java.util.StringTokenizer;


/**
 * Created by LAD5NU3 on 29.02.2016.
 */
public class CameraConnector {

    public String getSerialNumber(String ip)
    {
         String rawSerial = connectTo(ip,  "/rcp.xml?command=0x0ae7&type=P_OCTET&direction=READ");

         StringTokenizer stringTokenizer = new StringTokenizer(rawSerial);

        StringBuilder serial = new StringBuilder();

         while (stringTokenizer.hasMoreTokens())
         {
             byte[] s = DatatypeConverter.parseHexBinary(stringTokenizer.nextToken());
            serial.append(s[0]);
         }

        return serial.toString();
    }

    public String getMACAdress(String ip)
    {
        String rawMAC = connectTo(ip, "/rcp.xml?command=0x00bc&type=P_OCTET&direction=READ");

        return rawMAC.replace(" ", ":");


    }

    public String getCTN (String ip)
    {
        String ctn = connectTo(ip, "/rcp.xml?command=0x0be7&type=P_STRING&direction=READ");

        return ctn;
    }

    public String getFirmwareVersion(String ip)
    {
        String firmware = connectTo(ip, "/rcp.xml?command=0x002f&type=P_STRING&direction=READ");

        return firmware;
    }

    public void setToFactoryDefaults(String ip)
    {
        connectTo(ip, "/rcp.xml?command=0x09a0&type=F_FLAG&direction=WRITE");
    }

    public String connectTo(String ip, String rcpCommand) {

        Document doc = null;

        String getCommand = "http://" + ip + rcpCommand;

        try {
            doc = Jsoup.connect(getCommand).get();

        } catch (IOException e1) {
            System.out.println("Cannot connect to camera with ip address '" + ip + "'");
            return "";
        }

        return  RCPPayloadDecoder.decodeMessage(doc);


    }
}
