package main

import (
    "fmt"
    "huaweicloud.com/go-runtime/go-api/context"
    "huaweicloud.com/go-runtime/pkg/runtime"
)

// Handler function
func Handler(payload []byte, ctx context.RuntimeContext) (interface{}, error) {
    //f_name := ctx.GetFunctionName()
	var f_name string = "Hello world! Function (Go1.x) name is " + ctx.GetFunctionName()
	fmt.Println(f_name)

    return f_name, nil
}

func main() { 
    runtime.Register(Handler) 
}

