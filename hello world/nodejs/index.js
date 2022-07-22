exports.handler = async (event, context) => {
    f_name = context.getFunctionName()
    f_name = "Hello world! Function name is " + f_name
    console.log(f_name);
    return f_name;
}
