相关函数说明：运行前，需先将文件另存到Raspberry-Pi-Pico目标板内
1.ws2812b(num, sm, pin)
num代表ws2812的数量
sm是内核，目前需要设置为0
pin是使用的引脚

2.set_pixel(n, r, g, b)
n是第几个ws2812
r, g, b是红绿蓝颜色

3show()，刷新显示

4.fill((r, g, b))，填充所有ws2812

5.set_pixel_line(n1,n2,r,g,b)，设置从n1到n2颜色

6.set_pixel_line_gradient(n1,n2,r1,g1,b1,r2,g2,b2)，设置从n1到n2渐变色