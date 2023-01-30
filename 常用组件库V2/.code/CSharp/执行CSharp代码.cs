
//代码执行入口，请勿修改或删除
public void Run()
{
    //在这里编写您的代码
                //新建一个Stopwatch变量用来统计程序运行时间
            Stopwatch watch = Stopwatch.StartNew();
            //获取本机运行的所有进程ID和进程名,并输出哥进程所使用的工作集和私有工作集
            foreach (Process ps in Process.GetProcesses())
            {
                PerformanceCounter pf1 = new PerformanceCounter("Process", "Working Set - Private", ps.ProcessName);
                PerformanceCounter pf2 = new PerformanceCounter("Process", "Working Set", ps.ProcessName);
                Console.WriteLine("{0}:{1}  {2:N}KB", ps.ProcessName, "工作集(进程类)", ps.WorkingSet64 / 1024);
                Console.WriteLine("{0}:{1}  {2:N}KB", ps.ProcessName, "工作集        ", pf2.NextValue() / 1024);
                //私有工作集
                Console.WriteLine("{0}:{1}  {2:N}KB", ps.ProcessName, "私有工作集    ", pf1.NextValue() / 1024);

            }

            watch.Stop();
            Console.WriteLine(watch.Elapsed);
}
//在这里编写您的函数或者类