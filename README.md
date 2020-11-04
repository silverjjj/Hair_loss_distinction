# 모델 평가

version1 부터 version3까지는 이미지를 수정 및 추가를 하면서 데이터증강한 version들이다.

현재까진 V1의 경우가 가장 분류를 잘해낸다. 



### v1

![img](https://blog.kakaocdn.net/dn/EeMwO/btqMuOTE4Az/LPP7ACQ1AmnbQoLIlPnVx0/img.png)



### v2

![img](https://blog.kakaocdn.net/dn/48iKl/btqMqdG3sMv/yKLhRORMEsV4bK9Z4Ku3yK/img.png)



### v3

v3의 경우 validation loss가 굉장히  널뛰기 하는걸 볼수있다. 아마 데이터 증식에 따른 과대적합이 지속적으로 이뤄진거 같다. 

![img](https://blog.kakaocdn.net/dn/I0Yam/btqMvfcmmyQ/Fk62AMfJHkpqU9nheikXw0/img.png)



### v4

그래서 VGG16구조를 활용해서 다시 훈련을 진행했다. 훈련결과는 아래와 같다

훈련을 3~4번 진행할때부터 과대적합이 발생되기 시작한다. 최적화를 위해 훈련을 3번만 진행하겠다.

![img](https://blog.kakaocdn.net/dn/MLIp8/btqMwofBfuI/KWJ5KQ1fezmMfexUHsZquK/img.png)



### v5 

vgg16과 find-tuning(미세조정)을 사용하여 과대적합을 최소화하고 정확도를 높였다.

약 10번의 에포크부터 검증손실과 정확도가 불안정함을 볼수있다. 

![img](https://blog.kakaocdn.net/dn/bYsedb/btqMqBVl2H8/wIO5KPKuDS3QgTkgwSvkEk/img.png)



### v6

아래는 같은 코드에 10번의 에포크를 진행한 결과다.

![img](https://blog.kakaocdn.net/dn/utdbs/btqMvKJWx62/KYTkRLOY9SBHlt5UkbrTZk/img.png)