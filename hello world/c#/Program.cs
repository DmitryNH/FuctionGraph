using HC.Serverless.Function.Common;
using System;
using System.IO;

namespace src
{
    class Program
    {
        static void Main(string[] args) { }
        public Stream myFunc(Stream input,IFunctionContext context)
        {
            //Get function name
            string f_name = "Hello world! Function name is " + context.FunctionName;
            //Print function name
            Console.WriteLine(f_name);

            var ms = new MemoryStream();
            var sw = new StreamWriter(ms);
            sw.Write(f_name);
            sw.Flush();
            ms.Position = 0;
            return ms;
        }
    }
}