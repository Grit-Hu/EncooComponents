//代码执行入口，请勿修改或删除

public void Run()
{
       //在这里编写您的代码
   //获取总物理内存大小
            ManagementClass cimobject1 = new ManagementClass("Win32_PhysicalMemory");
            ManagementObjectCollection moc1 = cimobject1.GetInstances();
            double available=0, capacity=0;
            foreach (ManagementObject mo1 in moc1)
            {
                capacity += ((Math.Round(Int64.Parse(mo1.Properties["Capacity"].Value.ToString()) / 1024 / 1024 / 1024.0, 1)));
            }
            moc1.Dispose();
            cimobject1.Dispose();
            //获取内存可用大小
            ManagementClass cimobject2 = new ManagementClass("Win32_PerfFormattedData_PerfOS_Memory");
            ManagementObjectCollection moc2 = cimobject2.GetInstances();
            foreach (ManagementObject mo2 in moc2)
            {
                available += ((Math.Round(Int64.Parse(mo2.Properties["AvailableMBytes"].Value.ToString()) / 1024.0, 1)));

            }
            moc2.Dispose();
            cimobject2.Dispose();

            Console.WriteLine("总内存=" + capacity.ToString() + "G");
            Console.WriteLine("可使用=" + available.ToString() + "G");
            Console.WriteLine("已使用=" + ((capacity - available)).ToString() + "G," + (Math.Round((capacity - available) / capacity * 100, 0)).ToString() + "%");
            
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
