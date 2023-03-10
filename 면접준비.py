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
소프트맥스는 다중분류에서 쓰이는 손실함수로, 가중합을 라벨 클래스에 개수에 따라서 총합이 1인 확률로 나타나게됨''',
'순전파':'''
입력층에서 생기는 신호가 은닉층을 거쳐 출력층으로 가는 과정을 의미한다.이 과정에서 가중치와 편향을 통해 나온신호가
활성화함수로 통해 다음층으로 계속 전달 출력층에서는 가중치가 초기화되고 후에 역전파과정에서 가중치가 갱신됨''',
'손실함수':'''
예측값과 실제값의 차이를 나타내는 함수로 머신러닝에서 성능과 직결됨. 대표적인 것은 회귀의 mse와 분류의 크로스엔트로피. 이진분류는 binary-entropy를 쓰고 회귀는 mse mae
다중분류는 categorical-crossentropy와 sparse-cross-entropy를 쓴다''',
'역전파':'''
역전파는 순전파와는 반대로 손실함수를 전달하여서 손실함수를 줄이는 쪽으로 가중치를 갱신해 나가는 과정이다. 여기서 손실함수를 줄이기 위해서 경사하강법을 사용한다''',
'경사하강법':'''
손실함수를 최소로 하는 것이 제일 좋은데 이때 손실함수식에서 미분을 통해서 가장 최소값을 찾게 된다. 이때 미분 과정이 경사하강법''',
'옵티마이저':'''
경사하강법에서 데이터를 얼마나 사용하나 따라서 사용법이 달라지는데 이를 옵티마이저라고 한다. sgd등 adam등등''',
'sgd':'''
확률적 경사하강법으로 매 이터레이션마다 하나의 데이터로 손실함수 가중치를 계산''',
'학습률':'''
학습률이란 가중치 갱신시에 경사하강법에 대한 기울기값을 얼마나 적용시킬지를 정함 이때 학습률이 너무 작으면 최적까지 찾아가는데 오래걸리고 너무 크면 최적의 값을 건너뛸 수도 있다.
따라서 최적의 학습률을 찾아야한다. 이를 학습률 계획법이라고 한다 compile에서 adam등을 설정하면됨''',
'가중치 초기화':'''
가중치를 처음에 설정하는 것으로 사비에르와 허 초기화가 있다.''',
'xavier':'''
원래는 표준정규분포에서 뽑지만 이 경우에는 활성화 함수를 할 경우에 0이나 1로만 나와서 문제이다. 이때 이전 층의 노드가 n 개일 때, 현재 층의 가중치를 표준편차가 
1/sqrt(n)인 정규분포로 초기화 Xavier 초기화는 활성화 함수가 시그모이드(Sigmoid)인 신경망에서는 잘 동작합니다''',
'he초기화':'''
.하지만 활성화 함수가 ReLU 일 경우에는 층이 지날수록 활성값이 고르지 못하게 되는 문제를 보이는데요.이때 이전 층의 노드가 n 개일 때, 현재 층의 가중치를 표준편차가 
2/sqrt(n)인 정규분포로 초기화 결론 Sigmoid ⇒ Xavier 초기화를 사용하는 것이 유리 ReLU ⇒ He 초기화 사용하는 것이 유리''',
'Dropout':'''
데이터의 일부를 정해서 학습을 하지 않는 것 과적합을 방지하기 위해서'''
}


dict_nlp = {
'벡터화':'''
단어나 문장은 컴퓨터가 인식할 수 없다. 따라서 이들을 컴퓨터가 알아볼 수 있는 벡터로 만들어 주어야 한다. 이를 벡터화라고 하고 벡터화에는 등장횟수기반 벡터화와 분포기반 벡터화의 
2가지 방법이 있다.''',
'텍스트 전처리':'''
텍스트를 범용적으로 사용하기 위한것으로 트리밍, 불용어 처리, 소문자화등등이 있다. (차원의 저주 해결)''',
'토큰화':'''
문장이 들어오면 띄어쓰기를 기준으로 토큰화시켜서 나눔''',
'불용어 처리':'''
and나 i처럼 많이 나오는 단어는 많이 나오지만 분석에서는 아무런 도움도 되지 않아서 이런 단어는 코퍼스에서 제외한다.''',
'통계적 트리밍':'''
통계적 트리밍을 통해서 너무 횟수가 많은 토큰이나 적은 토큰을 삭제''',
'어간추출(stemming)':'''
ing나 ed처럼 이런거는 끼게 되면 너무 형태가 다양해지니 원형만 넣고 이런 단어는 삭제함''',
'표제어 추출(Lemmatization)':'''
토큰들의 원형을 찾아서 수정함 얘를 들어 played의 경우 표제어인 play가 토큰화되어 들어가게 됨 물론 이는 stemming보다 더 오래걸림''',
'문서-단어 행렬':'''
각 행에는 문장이 들어가고 열에는 단어 토큰이 들어가서 이 토큰이면 1이고 아니면 0으로 한다''',
'Bag-of-Words':'''
빈도횟수를 기반으로 하는 토큰화로 순서를 고려하지 않고 빈도수를 토큰화된 숫자로 표현하는 것 i가 8번 쓰였으면 i는 8 이렇게''',
'TF-IDF':'''
단어가 여러 문서에 쓰일때는 중요도가 떨어지게 되니 이를 고려한 방법으로 log(전체 문서수 / w 단어가 있는 문서수)로 계산하는데 이러면 단어가 여러 문서에 많이 쓰이면 
값이 작아지는 경향 특정 문서에 등장하는 단어에 가중치를 주는 방법''',
'코사인 유사도':'''
단어끼리 유사한 지를 비교하는 것으로 토큰화된 단어들을 코사인유사도를 구한다. 서로 같으면 1 반대면 -1 90도이면 0 얘는 원 핫 인코딩의 경우 단어끼리 코사인 유사도를 구할 경우
0이 나오는 단점을 해결해줌''',
'최근접 이웃(knn)':'''
knn은 쿼리와 가장 가까운 상위 K개의 근접한 데이터를 찾아서 K개 데이터의 유사성을 기반으로 점을 추정하거나 분류''',
'분포기반표현':'''
비슷한 위치에서 등장하는 단어들은 비슷한 의미를 가진다는 분포가설에 의거하여서 표현하고자 하는 벡터는 주변단어에 의해서 결정되는 것 word2vec과 fasttext가 있다''',
'임베딩':'''
원핫인코더의 단점을 해결하기 위해서 고정길이의 벡터로 만들기''',
'word2vec':'''
단어를 그대로 벡터화 하는 것으로 cbow와 skip_gram등이 있다. cbow는 주변단어로 중심단어를 예측하는 것이고 skip-gram은 중심단어를 기반으로 주변단어를 예측하는 것 skip-gram이 
더 성능이 좋다 단점은 새로운 단어의 경우 벡터화를 못함. 이를 oov out of voca라고 한다''',
'fasttext(철자단위임베딩)':'''
철자단위로 나눠서 분석을 진행함 이경우에는 철자의 경우 기존 벡터에 있으면 의미를 유추 할 수 있어서 예를 들어 맞벌이를 모르는데 맞은 맞선 맞대다 등등이 있고 벌이는 벌다의 경우면
맞벌이를 유추가능함''',
'rnn(recurrent nerual network) 순환신경망':'''
시퀀스형 데이터를 입력으로 받는 모델로써 입력데이터의 길이에 제한이 없다는 장점이 있다.은닉층이 출력층으로 가기도 하고 다음 은닉층의 입력으로 들어가게 되는 모델로 시퀀스형 데이터를 처리하는데 유용한 모델이다. 활성화 함수는 하이퍼 탄젠트 함수를 사용한다. 단점은 
순차적으로 데이터를 입력해서 병렬화가 불가능해서 gpu를 사용해도 의미가 없다. 또한 하이퍼 탄젠트 함수값을 역전파에서 미분해서 계속 역전파되면서 곱해지면 기울기가 작아지는데 이를 기울기 
소실문제라고 한다. 반대로 살짝만 커도 기울기가 커지는 기울기 폭발문제''',
'통계적 언어 모델(statistic language model)':'''
조건부 확률에 의거하여 앞에 특정 단어가 올때의 확률계산 i am student의 경우 p(i) * p(i|am) *p(i am | student) 이렇게 계산 단점은 모르는 단어가 앞에 나오는 경우 뒤에는 확률이 0으로 됨
백오프나 n-gram으로 해결함''',
'lstm(장단기 기억망)':'''
cell state가 추가되고 forget gate가 추가되어서 기존 rnn이 역전파에서 과거정보가 사라지는것을 방지하기 위해서 과거정보를 얼마나 유지할지를 정하는 forget gate가 생기고 tahn 활성화
함수를 사용하지 않는 cell state로 정보의 손실이 없다는 특징이 있다. ''',
'grm':'''''',
'attension(어텐션)':'''rnn의 경우 기울기 소실로 인한 장기 의존성 문제가 있고 이를 해결하기 위한것이 lstm과 gru이다.하지만 얘네도 문제가 있는데 얘네는 장기의존성을 해결하기 위해서 
은닉층이 시퀀스 전체를 기억하고 있는데 만약 문장의 길이가 길어지면 모델링이 어렵다는 점이다. 이를 해결하기 위해서 나온 것이 어텐션이다.어텐션은 인코더와 디코더구조로 은닉층의 정보를 
디코더로 넘겨준다. 이때 쿼리 키 밸류의 방식을 사용한다. 먼저 디코더의 쿼리와 인코더의 키를 백터 내적하고 소프트 맥스를 취하고 다시 여기에 밸류 값을 내적해서 제일 큰 값을 선택하는 
구조이다. i am a dog이라고 하면 하나씩 인코더에 들어가서 4개의 히든스테이트가 만들어 진다. 이게 디코더에 전달되고 디코더는 우선 히든스테이트의 쿼리와 키인 인코더의 히든 스테이트를 
내적해서 소프트맥스를 취해줌. 그리고 소프트 맥스를 해서 확률값으로 바꿔줌 이후에 value인 히든스테이트와 다시 내적하고 이를 하나로 합침. 이때 쿼리-키가 연관성이 높은게 가장 많이 들어
있어서 출력을 결정해줌 ''',
'하이퍼볼릭탄젠트':'''
순환신경망의 활성화 함수로 시그모이드 함수의 단점을 보완 (기울기 소실) 하이퍼볼릭탄젠트는 -1에서 1사이의 함수값인데 시그모이드는 0-1사이에 있으니 미분시 더 값의 범위가 다양함''',
'seq2seq':''''''
}


dict_cv={
'cnn(순환신경망)':'''
순환신경망은 컨볼루션레이어,풀링레이어,완전연결레이어로 이루어져 특징추출을 먼저하고 이후에 분류를 진행하는 구조이다. 이미지 데이터의 특징을 추출하기 위해서 벡터화된 이미지 데이터에
합성곱 필터를 곱해서 특징을 추출하는데 이를 합성곱 레이어라고 한다. 이때 패딩처리나 스트라이드 값설정으로 합성곱층을 변경할 수 있다. 이후에 풀링레이어에서 특징을 보존하게 된다. 처음에는
자세한 정보를 담지 못하지만 깊게 은닉층을 형성 할 수록 이미지는 작이지고 이미지 정보를 잘 보존하게 된다. 이후에는 다층신경망의 구조로 분류를 진행한다.''',
'전이학습':'''
전이학습은 기존 사전학습모델은 그대로 쓰고(특징추출) 완전연결신경망만 바꾸는 것이다. resnet,vgg,googlenet등이 있다.'''



}


random_key = random.sample(list(dict_m), 10) # https://janeljs.github.io/python/sample()/
print(random_key)


'''
단일 클래스 분류와 다중 클래스 분류의 목적함수/손실함수 설명, 
SVM이란 무엇이며 수식적으로 설명, 어떤 모델과 파라미터를 조정하며 성능 개선한 경험 더 자세히 설명.'''