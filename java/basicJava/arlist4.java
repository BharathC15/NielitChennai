import java.util.*;
class Student{  
    int rollno;  
    String name;  
    int age;  
    Student(int rollno,String name,int age){  
        this.rollno=rollno;  
        this.name=name;  
        this.age=age;  
    }  
  }  
    public class arlist4 {
     public static void main(String[] args) {
        Student s1=new Student(101,"abc",23);  
        Student s2=new Student(102,"xyz",21);  
        Student s3=new Student(103,"lmn",25); 
        
        ArrayList<Student> studentData=new ArrayList<Student>();  
        studentData.add(s1);
        studentData.add(s2);  
        studentData.add(s3);  
        Iterator sPointer=studentData.iterator();   
        while(sPointer.hasNext()){  
            Student sData=(Student)sPointer.next();  
            System.out.println(sData.rollno+" "+sData.name+" "+sData.age);  
        }  
     } 
  }




  