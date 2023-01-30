//代码执行入口，请勿修改或删除
public void Run()
{
    foreach (DataColumn item in 传入的数据表.Columns)
    {
        // 遍历每个列名，拼接列名
        数据表总字符串.Append(item.ToString()).Append("\t");
    }
    数据表总字符串.Append("\n");



    foreach (DataRow item in 传入的数据表.Rows)
    {
        // 遍历每行，然后拼接每行的每列内容。
        for (int i = 0; i < 传入的数据表.Columns.Count; i++)
        {
            数据表总字符串.Append(item[i].ToString()).Append("\t");
        }
        // 每行拼接完之后加一个换行
        数据表总字符串.Append("\n");
    }


    // 把每行最后的\t\n改为\n
    数据表总字符串.Replace("\t\n", "\n");

    // 打印。
    System.Console.WriteLine(数据表名称 + "=\n" + 数据表总字符串.ToString());

}