Game of chaos 

The idea of game is that you have 3 points in a plane.
Starting point:  
Choose randomly one point in the plane. (it doesn't need to be inside a triangle because at some point it will fall into it without escape)
Iterative point:  
Randomly choose one of the vertex of the triangle and add a point in the half of the way to this vertex. This is your next starting point.
Repeat.

Adding condition about half of distance between vertices of a triangle we got this beautiful shape called Sierpinski's triangle.

This is how it suppose to look (100 000 points, plt.scatter(..., size=0.1, alpha=0.1)). Blue dots are vertices, Orange dot is starting point, Green ones are next steps of iteration.  
![image](https://user-images.githubusercontent.com/26064347/111077763-9adc1a00-84f2-11eb-840d-ce61ebffa6bd.png)


I will try to simulate different objects. Maybe in a square or octagon there will be similar fractals. Let's see.

Square game of chaos with standard configuration is just a mess distributed inside this square randomly.  
But we can add another condition e.g. in next iteration we cannot choose the same vertex.

Expectations:  
![image](https://user-images.githubusercontent.com/26064347/111076695-a842d580-84ed-11eb-8003-767889932aa4.png)

Reality:  
![image](https://user-images.githubusercontent.com/26064347/111076702-ad078980-84ed-11eb-8b58-e467cc1da545.png)


But after some adjustment (100 000 points, and arguments size = 0.2, alpha = 0.1 in plt.scatter()) reality seems more bearable:  
![image](https://user-images.githubusercontent.com/26064347/111077214-ff49aa00-84ef-11eb-8f04-d6e52df4b8af.png)

This is how triangle looks with this condition:  
![image](https://user-images.githubusercontent.com/26064347/111077460-294f9c00-84f1-11eb-8ae1-b83d878b00a6.png)

