package com.huawei.demo;
import com.huawei.services.runtime.Context;

public class hello_world {
    public static void main(String args[]) {}
    
    public String handler(Object event, Context context){
        //Get function name
        String f_name = "Hello world! Function name is " + context.getFunctionName();
        //Print function name
        System.out.println(f_name);

        return f_name;
    }
}

