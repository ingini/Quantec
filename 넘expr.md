Numpy
numpy의 다중 배열은 c배열 기반으로 하며, 개발자는 간편하게 C or 포트란 언어와 numpy를 섞어 사용할 수 있다. 
numpy는 파이썬과 레거시 코드를 이어주는 다리 역할을 한다.

numexpr  - 배열 표현을 최적화하고 멀티코어를 지원

배열 접근시 슬라이싱으로 인덱스에 접근하는 것이 속도가 빠르다

다차원 배열의 각 축에 대한 인덱스 배열을 사용해 펜시 인덱싱
ex )
a = np.array([9,8,7,6,5,4,3,2,1,0])
idx = np.array([0,2,5])
print(a[idx])

a= np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
idx1 = np.array([0,1])
idx2 = [[0,1],[3,2]]
idx3 = [[0,2],[1,1]]
print(a[idx1])
print(a[idx2,idx3])


브로드캐스팅 - 삼각법, 논리, 반올림 (.sqrt = 제곱근)
ex)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
A * B

r_i = np.random.rand(10,2)
norm = np.sqrt((r_i ** 2).sum(axis=1))
print(norm)

numpy 입자 시뮬레이터 개선

ParticleSimulator.evolve 함수의 루프가 전체 실행 속도를 저하한다.

for i in range(nsteps):
	for p in self.particles:
		norm = (p.x **2 + p.y**2)**0.5
			v_x = (-p.y)/norm
			v_y = p.x/norm

			d_x = timestep * p.ang_speed * v_x
			d_y = timestep * p.ang_speed * v_y

			p.x += d_x
			p.y += d_y

각 루프는 하나의 입자만을 처리한다.
but 각 입자의 위치와 회전속도를 저장하는 배열이 있다면 브로드캐스팅 기법으로 사용하여
루프를 재작성할 수 있다.
시간을 기준으로 (입자개수 ,2) 형태의 배열에 저장하는 것이 일반적이며, 회전 속도는 (입자개수) 형태로 저장한다
r_i 와 ang_speed_i 를 호출하고 다음 코드에서 초기화!

r_i = np.array([[p.x, p.y] for p in self.particles])
ang_speed_i = np.array([p.ang_speed for p in self.particles])

벡터 (x,y) 에 대해 수직인 입자의 이동 속도는 아래와 같이 정의
v_x = -y / norm
v_y = x / norm

노름은 '노름 계산' 절에서 학습한 방법대로 아래와 같이 계산.
norm_i = ((r_i **2).sum(axis =1)) ** 0.5

(-y, x)의 경우 다음과 같이 r_i 의 x와 y값을 맞바꾸고 첫번째 축에 -1을 곱한다.
v_i  = r_i[: [1,0]] / norm_i

v_i[:,0] *= -1
이동거리는 v_i와 ang_speed_i, timestamp를 곱한 값이다.
ang_speed_i 는 (nparticles) 형태이기 때문에 (nparticles,2) 형태인 v_i 와 맞추기 위해 두 번째 축이 필요하다.

numpy.newaxis 상수를 사용해 축을 추가한다.
d_i = timestep * ang_speed_i[:, np.newaxis] *  v_i
r_i += d_i

for i , p in enumerate(self.particles):
    p.x, p.y = r_i[i]

한줄에 최대한 많은 연산을 축약하는 것이 코드 최적화의 효과를 높인다.


Numexpr은 NumPy에 대한 빠른 수치 평가 기입니다.
 이를 통해 배열에서 작동하는 표현식 (예 : "3 * a + 4 * b")은 Python에서 동일한 계산을 수행하는 것보다 
가속화되고 메모리를 덜 사용합니다.

또한 멀티 스레드 기능은 모든 코어를 사용할 수 있습니다.
 특히 메모리에 바운드되지 않은 경우 (예 : 초월 함수를 사용하는 경우) 계산 속도를 높일 수 있습니다.

마지막으로, numexpr은 Intel의 VML (Vector Math Library,
 일반적으로 Math Kernel Library 또는 MKL에 통합 된 Vector Math Library)을 사용할 수 있습니다. 
이를 통해 초월 식을 더욱 가속화 할 수 있습니다.


