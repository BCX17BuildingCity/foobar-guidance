import org.apache.commons.lang3.StringUtils;
import org.jsoup.nodes.Document;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Created by LAD5NU3 on 31.07.2015.
 */
public class RCPPayloadDecoder {

    public static String decodeMessage(Document response) {
        String decodedMessage;

        String type = checkType(response.getElementsByTag("type").text());
        Integer len = parseLength(response.getElementsByTag("len").text());
        String str = response.getElementsByTag("str").text();

        decodedMessage = decode( str, len, type);

        return decodedMessage;
    }

    public static Integer parseLength(String len) {

        Integer length = 0;

        if (StringUtils.isNotBlank(len) || StringUtils.isNotEmpty(len)) {
            length = Integer.parseInt(len);
        }

        return length;
    }

    public static String decode( String resultString, Integer resultLength, String resultType) {

        StringBuilder decodedResult = new StringBuilder();

        StringTokenizer eachHexValue = new StringTokenizer(resultString, " ");

        if (eachHexValue.countTokens() != resultLength) {
            // System.out.println("There is something wrong");
        }

        /*System.out.println("ResultString: " + resultString);
        System.out.println("ResultLaege: " + resultLength);
        System.out.println("ResultType: " + resultType);*/

        if ("P_UNICODE".equals(resultType)) {
            String firstPart;
            String secondPart = new String();

            while (eachHexValue.hasMoreTokens()) {
                firstPart = eachHexValue.nextToken();

                if (eachHexValue.hasMoreTokens()) {
                    secondPart = eachHexValue.nextToken();
                }
                char decodeCahr = (char) Integer.parseInt(firstPart + secondPart, 16);
                decodedResult.append(decodeCahr);
            }
        }
        else if ("P_OCTET".equals(resultType))
        {
            System.out.println(resultString);
            decodedResult.append(resultString);
        }

        else if ("P_STRING".equals(resultType))
        {
            decodedResult.append(resultString);
        }

        return decodedResult.toString();
    }

    public static String checkType(String commandType) {

        String foundType = "UNKNOWN";

        List<String> knownTypes = new ArrayList<>();
        knownTypes.add("F_FLAG");
        knownTypes.add("T_OCTET");
        knownTypes.add("T_WORD");
        knownTypes.add("T_INT");
        knownTypes.add("T_DWORD");
        knownTypes.add("P_OCTET");
        knownTypes.add("P_STRING");
        knownTypes.add("P_UNICODE");

        for (String knownType : knownTypes) {
            if (commandType != null) {
                if (commandType.toUpperCase().startsWith(knownType)) {
                    foundType = knownType;
                    break;
                }
            }
        }
        return foundType;

    }
}
