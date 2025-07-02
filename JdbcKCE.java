import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class JdbcKCE {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// TODO Auto-generated method stub
//		1) Load the Class
		Class.forName("com.mysql.cj.jdbc.Driver");
//		2) Connection Establish
		Connection con=null;
		con=DriverManager.getConnection("jdbc:mysql://localhost:3306/klndemo","root","root");
		if(con!=null)
			System.out.println("Connected Successfully Now Start Your code!!!");
		else
			System.out.println("Not yet Connected");
//		3) Creating Statements
		// insert
		Scanner sc = new Scanner(System.in);
//		String name = sc.nextLine();
//		String password = sc.nextLine();
//		String sql="insert into login values(?,?)";
//		PreparedStatement ps=con.prepareStatement(sql);
//		ps.setString(1, name);
//		ps.setString(2, password);
//		int row=ps.executeUpdate();
		System.out.println("------------------------Insertion Completed Successfullly--------------------------");
		
		// Update
		System.out.println("Update--->");
//		System.out.println("Enter Your Password");
//		String pass1 = sc.nextLine();
//		System.out.println("Enter Your Name");
//		String name1 = sc.nextLine();
//		String update = "update login set password=? where name=?;";
//		PreparedStatement ps1= con.prepareStatement(update);
//		ps1.setString(1, pass1);
//		ps1.setString(2, name1);
//		int row1=ps1.executeUpdate();
		System.out.println("-----------------------Updation is Completed Successfully----------------------");
		
		// Display 
		String view="Select * from login;";
		PreparedStatement ps2 = con.prepareStatement(view);
		ResultSet rs=ps2.executeQuery();
		while(rs.next())
		{
			System.out.println(rs.getString("name"));
			System.out.println(rs.getString("password"));
		}
		System.out.println("----------------Display Completed------------------");
		
		//Delete
		String name2=sc.nextLine();
		 String del="delete from login where name=?";
		 PreparedStatement ps3=con.prepareStatement(del);
		 ps3.setString(1, name2);
		 int row2=ps3.executeUpdate();
		System.out.println("--------------------------------------------------------");
	}

}