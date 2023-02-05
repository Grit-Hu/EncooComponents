//代码执行入口，请勿修改或删除
public void Run()
{
    //在这里编写您的代码
    midpoint = totalDistance*3/5; // 加速度切换点
    // 当前位移小于预期总位移时，计算每次位移并加入列表。对应每秒10次位移
    while( currentDistance < totalDistance) { 
		// 切换点前加速度+，切换点后加速度-
        if (currentDistance < midpoint){
            currentAcceleration = positiveAcceleration;
            //Console.WriteLine("speed up.");
        }
        else{
            currentAcceleration = nagetiveAcceleration;
            //Console.WriteLine("slow down.");
        }

        initialVelocity = velocity; // 当前循环初始速度=当前速度
		
        velocity = initialVelocity+currentAcceleration*time; // 计算本次位移速度
        
        xMove = velocity*time+1/2*currentAcceleration*time*time; // 计算本次位移距离
        currentDistance = currentDistance+xMove; // 计算当前总位移
        tracksList.Add(Convert.ToInt32(xMove));
        if (Convert.ToInt32(currentDistance) % 10 == 0) {
            Console.WriteLine("currentDistance="+currentDistance);
        }
        if (xMove <= 0){ // 本次位移为0则多加几个0（模拟人的停顿，然后退出循环。
            tracksList.Add(0);
            tracksList.Add(0);
            tracksList.Add(0);
            tracksList.Add(0);
            tracksList.Add(0);
            break;
        }
    }

}
//在这里编写您的函数或者类