/*
Hiren Shah
SDEV 325 7380
4/23/2021
Professor Matthew L. Brown, Ph.D
Demonstrating Porous Defenses Final
CWE759-Mitigated
Use of One_Way Hash without SALT 
*/
 
import java.util.*;
import java.security.SecureRandom;
import java.security.NoSuchAlgorithmException;

public class OneWaySaltMit {
	public static void main(String[] args) {
    	System.out.println("Enter a word to print out: ");
    	Scanner sc = new Scanner(System.in);
    	String str = sc.nextLine();
    	System.out.println(Hashed(str));
    	
		}
	
private static String Hashed(String str) {
	String result = "";
//	Date date = new Date();
//	str += date.toString();
try {
	str = getSalt() + str + getSalt();
}
catch(Exception e) {
	e.printStackTrace();
}
	String newStr = "";
	for (int i=0; i<str.length(); i++) {
		
		if (i % 2 == 1) {
			newStr += str.charAt(str.length()-i);
		}
		else {
			newStr = str.charAt(i) + newStr;
		}
			
			
	}
		for(int i=0; i<newStr.length(); i++) {
			result += Character.getNumericValue(newStr.charAt(i)) % 7;
		
	}
	return result;
		
	}

private static String getSalt() throws NoSuchAlgorithmException {
	try {
		
	
	SecureRandom secureRand = SecureRandom.getInstance("SHA1PRNG");
	//create array for the salt (16 bytes length)
	byte[] salt = new byte[16];
	secureRand.nextBytes(salt);
	return new String(salt);
	}
	catch(Exception e) {
		e.printStackTrace();
	}
	return null;
}
	
}
