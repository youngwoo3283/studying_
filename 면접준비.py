import random

dict_m = {
'머신러닝' : '''
머신러닝이란 데이터로부터 유용한 예측을 하기 위해 모델이라고 불리는 소프트웨어를 학습시키는 과정을 말합니다.
머신러닝 모델이란 예측에 활용할 수 있는 데이터 간의 수학적 관계, 규칙, 패턴 등을 의미합니다.
머신러닝의 목적은 기존의 데이터로부터 패턴을 학습한 뒤 새로운 데이터가 들어왔을 때 예측을 잘 하는 것입니다''',
'지도학습':'''
많은 문제와 정답을 학습한 후 새로운 문제가 들어왔을 때 학습한 내용을 기반으로 답을 예측하는 것입니다. 지도학습은 라벨이 있는 것으로 분류와 예측이 있다.''',
'분류' : '''
분류는 특정 데이터가 어떤 분야에 속할 확률을 구하는 것으로 다중분류와 이중분류등이 있다.''',
'기준모델' : '''
모델을 만들기에 앞서 이 모델을 평가하기 위한 가장 기초적인 모델 회귀의 경우 타겟의 평균값으로 기준을 설정하고 분류의 경우 타겟의 최빈값으로 기준모델을 만든다''',
'일반화' : '''
일반화(Generalization)란 모델을 만드는 데 사용된 분포와 동일한 분포에서 추출한 이전에는 볼 수 없었던 새로운 데이터에 적절하게 적응하는 모형의 능력을 의미합니다.
즉, 머신러닝의 목적은 일반화가 잘 된 예측 모델을 만드는 것이라고 할 수 있습니다.''',
'3-way-holdout':'''
holdout은 데이터를 나누는 것이다. 원래는 테스트 데이터와 훈련데이터로 나눈다. 이때 테스트 데이터를 나눌경우 한번만 테스트를 해야 하는데 이는 테스트를 여러번 할 경우
모델이 테스트 데이터에 맞춰지기 때문이다. 따라서 이를 방지하기 위해 검증데이터까지 3부분으로 나눈 것이 3-way-holdout이다''',
'mse' : '''''',
'mae' : '''''',
'r2' : '''''',
'Cross-Validation':'''
3부분으로 나누는 것은 몇가지의 문제가 있다. 우선 데이터가 적은 경우에는 3부분으로 나누기에 무리가 있다. 그리고 모델의 경우 학습이나 검증 테스트를 무작위로 나누게 되는데
이경우에 랜덤으로 모델이 만들어져서 검증이나 테스트가 제대로 이루어지지 않을 수 있다. 이때 해결로 나온것이 교차검증이다. 교차검증중에 대표적인 k-folfd를 보면 우선
k=5라고 하면 5개로 데이터를 나누고 1번을 우선 검증으로 하고 모델 성능을 체크, 이후 2,3,4,5도 체크해서 종합해서 검증을 하는 것''',
'Stratified kfold':'''
레이블 데이터가 불균형한 경우에 kfold를 하면 제대로 검증이 이루어 지지않는다. 예를 들어 신용카드 사기 검출에서 사기 레이블은 굉장히 적지만 중요함, 만약 얘네가 검증에 없게
분포가 된다면 모델 성능이 안좋을 수 밖에 따라서 레이블의 분포를 먼저 보고 나누는게 stratified이다.''',
'과대적합' : '''
과적합은 훈련데이터를 노이즈까지 과하게 학습해서 새로운 데이터에 예측을 잘 하지 못하는 것, 이는 서로 다른 데이터가 왔을경우에 변동되는 분산이 커서 그렇다. ''',
'과소적합' : '''
과소적합은 데이터를 너무 적게 학습해서 성능이 잘 안나옴, 과대적합은 훈련데이터의 성능은 높지만 과소적합은 모두 성능이 낮음 이경우에는 실제값과 예측값의 차이인 편향이 커서 그런 것이다''',
'과적합방지':'''
과적합을 방지하기 위해서 많은 데이터를 투입시킨다. 이는 교차검증과 비슷한 맥락이다. 두번째로 차원의 저주를 해결하기 위한 데이터의 특성을 줄인다. 마지막으로 모델에
규제항을 더하는 정규모델을 만든다. 이는 회귀계수가 커지는 것을 방지한다''',
'회귀계수':'''
회귀식에서 h0이나 h1을 말하는 것으로 얘네가 선형이면 선형회귀, 비선형이면 비선형회귀식이 된다. 이때 x의 차수에 따라서는 다중회귀가 되기도 한다.''',
'차원의 저주':'''
데이터의 수보다 특성이 많을때에 차원의 저주가 나타난다. 차원의 저주는 데이터 간의 거리가 커지게 되서 모델의 성능이 내려가게 된다. 이는 knn최근접알고리즘에서 가장 크게 나타난다.
해결하기위해서는 특성중요도에 따라서 특성을 줄이거나 데이터를 모으는 것''',
'knn알고리즘':'''''',
'정규화':'''
정규화는 규제항을 두어서 회귀계수의 상승을 줄여서 과적합을 방지하고자 한다. 이떄 편향을 늘리고 분산을 줄이는 트레이드 오프 방식을 사용한다. 규제항에 따라서
ridge, lasso, elestic등이 있다.''',
'ridge':'''
릿지는 회귀계수의 식에 가중치들의 제곱합(L2)을 더하는 방식으로 영향력이 적은 애들은 계수값이 0에 근접하게 됨''',
'lasso':'''
lasso는 회귀계수식에 가중치의 절댓값(L1)을 더하는 방식으로 영향력이 작은 회귀계수는 0이 된다''',
'elesticnet':'''
엘라스틱넷은 릿지와 라쏘를 합한 것으로 변수 선택기능을 가지지 못하는 릿지 회귀분석와 다중공선성이 높으면 좋은 성능을 가지지 못하는 라쏘회귀모델의 단점들을 절충한 모델''',
'다중공선성' :'''
회귀에서 변수들은 서로 독립적이어야 하는데 변수끼리 상관관계가 높아서 변수의 표준오차가 증가함 왜? 어떤 결과에 대해서 a,b가 상관관계가 높으면 a 때문인지 b때문인지를 모르기 떄문''',
'로지스틱회귀분석':'''
회귀식은 결과가 무한대인데 여기서 시그모이드 함수를 씌우면 0에서 1사이의 결과값이 나온다. 0.5이상이면 클래스 1으로 0이하이면 클래스 0으로 분류한다''',
'분류평가지표':'''
정확도,정밀도,재현율,f1score,roc_auc_score''',
'정확도':'''
올바르게 예측한수/전체예측수''',
'정밀도':'''
tp/tp + fp 참이라고 예측한 것중에서 실제 참인 것''',
'재현율':'''
실제 참인 것중에서 참이라고 에측 한 것, tp/tp  + fn''',
'f1':'''
정확도와 재현율의 조화평균, 라벨이 불균형일 때 쓰임 이는 strafied kfold와 비슷한듯''',
'fall_out':'''
실제 거짓인 것중에서 참으로 예측 fp/fn + fp''',
'roc_curve':'''
폴아웃과 재현율의 그래프, 재현율은 실제참인것에서 참으로 예측, 폴아웃은 실제 거짓인 것에서 참으로 예측, 커브가 왼쪽으로 기울수록 더 좋은 모델''',
'auc':'''
roc_curve의 그래프의 면적을 의미하는 것인데 1에 가까울 수록 더 좋은 모델이라고 함''',
'선형회귀':'''
특성과 타겟의 관계를 선형적이라고 가정하고, 비용함수를 최소로하는 파라미터를 찾는 모델''',
'결정트리':'''
선형회귀는 선형관계일때인데 만약 비선형이면 할 수 없다. 이때 쓰는 것이 결정트리이다. 이는 타겟을 yes/no의 질문으로 나누어 나가는데 이때 나무같아서 결정트리모델
회귀와 분류 모두됨. 회귀는 마지막 노드의 평균 분류는 마지막 노드의 최빈값으로 예측함''',
'불순도':'''
결정트리모델의 손실함수로 여기서 불순도를 최소로 해야됨 불순도란 여러 범주가 섞여있는 정도. 이를 이용해서 분할함 대표적인 것이 지니불순도와 엔트로피 여기서 만약
빨간 파란 비율이 6:4이면 불순도가 높고 8:2이면 불순도가 낮다''',
'결정트리의 특징':'''
시각화로 이해하기 쉽고 전처리가 별로 필요없다.(전처리하면 나누는 기준 같은것도 어짜피 전처리되서 같음) 단점은 작은 데이터로도 가지가 바뀌기 때문에 불안정하고,
기존 데이터로 기준을 만들고 나누기 때문에 외삽이 어려움 외부 데이터에 예측의 성능이 안좋음''',
'앙상블':'''
여러 모델을 종합해서 학습해서 예측을 하는것 따라서 일반화가 더 잘됨 bagging과 boosting이 있음''',
'bagging':'''
Bagging의 핵심은 각 기본 모델(weak learner)들이 학습 시 상호 영향을 주고받지 않고 독립적, 병렬적으로 학습된다는 것입니다.
대표적으로 Random Forest 모델이 있습니다.이떄 각 모델의 오차가 상쇄되어 분산이 줄어든다''',
'boosting':'''
Boosting은 과정을 반복할수록 최종 모델의 복잡도를 상승시키며, 모델의 편향을 줄여 과소적합을 피하도록 해 줍니다.
모델들이 순차적으로 학습되는 과정에서 전체 모델은 점차 데이터의 세밀한 곳까지 꼼꼼히 볼 수 있게 되며, 최종 예측값은 점점 정확해집니다,AdaBoost, Gradient Boosting,xgboos,catboost''',
'Gradient Boosting':'''
다음 모델이 이전 모델의 잔차(Residual)를 학습하는 구조입니다. 이는 잔차가 큰 관측치를 더 학습하도록 하는 효과가 있으며, 
이전 모델이 틀린 만큼을 직접 학습하며 이전 모델을 순차적으로 보완합니다.''',
'objective':'''
목적함수로 회귀나 분류등으로 설정해서 부스팅 함수에서 쓸 수 있다.''',
'SimpleImputer':'''
결측값을 채우는 것으로 채울때 평균이나 중앙값등으로 채운다''',
'n_estimators':'''
weak learner들의 개수로 학습을 하는 것의 개수를 의미함''',
'learning_rate':'''
단계별로 얼마나 모델들을 반영할지를 정함, 너무 크면 과대적합이 일어나고 작으면 너무길어짐 0.3정도''',
'max_depth':'''
트리의 탐색 깊이를 의미하고 보통 얘가 제일 영향을 많이 미침, 너무 깊으면 과적합,메모리증가 5 - 12''',
'subsample과 colsample_bytree':'''
데이터의 일반화 성능을 올리기 위해서 샘플링할 비율을 설정함''',
'Early Stopping':'''
n_esti를 최적화를 위해서 일정 기준의 성능향상이 안되면 멈추는 것''',
'수치형변수의전처리':'''
Min-Max Scaling(x - min/max-min),표준화 얘네는 분포는 바꾸지 않음. clipping와 rank변환 로그변환등이 분포까지 바꿈''',
'범주형변수의 전처리':'''
오디너리, 원핫, 타겟, 카운트인코딩''',
'하이퍼파라미터튜닝':'''
Grid Search는 해당 범위를 전부확인 최적을 찾을 수 있지만 오래걸림,Randomized Search는 특정범위에서 랜덤하게 선택 시간은 덜걸림 하지만 최적을 찾지 못할수도 있음
Bayesian Search는 기존 결과에서 더 좋은 성능이 나오도록 탐색함(위의2개보다메모리를 엄청아낌)''',
'모델해석':'''
Feature Importance:특성중요도(카디널리티가 높으면 중요할 수 있으니 제외시켜야함),Drop_col_importance:특정특성을 제외하고 성능을 평가해서 성능이확줄면 중요하다고 알게되는 방식
(단 학습마다 drop하니 번거로움),permutation재학습을 안하기 위해서 노이즈를 주어서 파악함 ''',
'iceplot':'''
특정변수가 증가/감소에 따라서 결과값이 어떻게 달라지는지 알 수 있음. 특성이 어떻게 영향을 미치나''',
'pdpplot':'''
ice는 한 데이터에 대해서이지만 전체에 대해서는 pdp로 ice의 평균''',
'데이터누수':'''
학습데이터의 정보가 테스트 데이터에 있다던가, 예측시에 못쓰는 특성을 사용하는 경우, 별다른 전처리나 처리를 안해도 성능이 너무 좋은 경우 이경우는 의심
이때 전처리를 하기전에 데이터를 나누거나 파이프라인을 만들어서 예방한다'''


}

dict_c = {
'선택정렬':'''
선택정렬은 정렬 알고리즘의 하나로 가장 작은 값을 먼저 찾아서 가장 왼쪽에 위치시키고 다음에 작은 값을 그 다음에 위치시키는 알고리즘이다.
이때 시간복잡도는 외부반복과 내부반복이기 때문에 log(n^2)''',
'삽입정렬':'''
삽입정렬은 앞에 하나의 값을 고정하고 그뒤로 값을 하나 정해서 왼쪽으로 하나씩 비교해서 작으면 계속 왼쪽으로 간다. 이때 가장 왼쪽값은 가장 작은값 시간복잡도는 logn^2''',
'버블정렬':'''
버블정렬은 2개의 값을 비교해서 자리를 바꾸고 다음값으로 계속 넘어가는 알고리즘이다.역시 중첩이니 log(n^2)이다''',
'해시테이블':'''
해시테이블은 키를 활용하여 값에 직접 접근이 가능한 구조이다. 해싱의 목적은 앞에서 배웠던 정렬알고리즘들과는 다르게 검색이다. 장점은 데이터 양에 영향을 덜 받으며 성능이 빠르다.(키를 통해 값을 검색한다.)
파이썬의 딕셔너리는 내부적으로 해시테이블 구조로 구현되어있다. 해시(Hash)는 해시 함수를 통해 나온 값이다. 해싱(Hashing)은 쉽게 말해서 다 흩뜨려놓고, 키와 매칭되는 값을 검색하는 과정이다. ''',
'해시충돌':'''
해시충돌은 키가 들어갈 자리(버킷)가 없는 경우에 발생한다. 해결하기 위한 방법으로 체이닝과 오픈어드레싱이 있다. 체이닝은 값에 리스트 형태로 여러 값이 들어갈 수 있게 하는 것이고 오픈 어드레싱은 
충돌이 일어나면 할당이 안된 다른 주소에 할당 하는 것이다.'''

}

dict_d = {
'퍼셉트론':'''
퍼셉트론은 딥러닝의 기본이 되는 요소로 다수의 신호를 입력으로 받아서 하나의 출력값을 만들어 내는 구조이다''',
'활성화함수':
'가중치-편향 연산을 통해서 나온 가중합을 얼마만큼의 신호로 출력할 지를 결정하는 함수, 시그모이드 소프트맥스 랠루 ',
'계단함수':'''
임계값을 기준으로 임계값을 넘으면 1을 안넘으면 0을 출력해주는 함수 근데 계단 함수는 경사하강법으로 가중치를 역전파를 할 수 없다. 미분시에 0이 나오기 때문''',
'시그모이드':'''
계단함수의 단점을 방지하는 게 시그모이드 얘는 임계값을 넘으면 1에 가까워지고 안넘으면 0에 가까워짐. 곡선형태여서 모든구간에서 미분이 가능함 근데 얘는 계속 사용하면
기울기 소실 문제가 발생함''',
'기울기 소실':'''''',
'랠루(relu)':'기울기 소실을 해결하기 위한 것이 relu이다.relu는 값이 양수이면 그냥 양수값을 리턴하지만 음수값은 0으로 리턴한다',
'소프트맥스':'''
소프트맥스는 다중분류에서 쓰이는 손실함수로, 가중합을 라벨 클래스에 개수에 따라서 총합이 1인 확률로 나타나게됨'''



}

random_key = random.sample(list(dict_m), 10) # https://janeljs.github.io/python/sample()/
print(random_key)


'''
단일 클래스 분류와 다중 클래스 분류의 목적함수/손실함수 설명, 
SVM이란 무엇이며 수식적으로 설명, 어떤 모델과 파라미터를 조정하며 성능 개선한 경험 더 자세히 설명.'''