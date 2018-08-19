<h1 align="center">Pycon 2018 x Banksalad Hold'em</h1>

<p align="center">
  <img src="./resources/banksalad-holdem.png" alt="banksalad-hold'em" width="256px" />
</p>

<p align="center">
  <a href="https://travis-ci.org/Rainist/pycon-2018-banksalad-holdem">
    <img src="https://travis-ci.org/Rainist/pycon-2018-banksalad-holdem.svg?branch=develop" alt="Travis CI Build Status" />
  </a>
  <a href="https://www.python.org/downloads/release/python-370/">
    <img src="https://img.shields.io/badge/python-3.7-blue.svg" alt="python 3.7" />
  </a>
  <a href="https://rainist.com/recruit">
    <img src="https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-Rainist-blue.svg" alt="love" />
  </a>
</p>
<p align="center">
    <a href="https://pycon2018.banksalad.com">https://pycon2018.banksalad.com</a>
</p>

- 뱅크샐러드 홀덤은 기존의 텍사스 홀덤에서 몇 가지 규칙을 변경하여 구현되었습니다.
- 5명의 플레이어가 하나의 게임에 참여하여 플레이하게 되며, 2명의 플레이어가 남거나 100라운드가 끝났을 경우 한 게임이 끝나게 됩니다.
    - 두 명의 플레이어가 살아 남을 경우, 두 명이 모두 다음 라운드에 진출합니다.
    - 100 라운드가 끝나 세 명 이상의 플레이어가 살아 남을 경우, 칩을 가장 많이 소지한 플레이어 둘이 다음 라운드에 진출합니다.
- 본 게임은 해커톤 품질의 코드로 만들어져 행사 동안 수시로 패치가 올라올 수 있습니다. 때때로 변경사항이 있는지 확인 부탁드립니다.

## How to Play

### Code

[turn.py](holdem/turn.py) 의 `bet(...)` 함수를 구현하신 후, 프로그램을 실행해볼 수 있습니다.

```python
def bet(
    my_chips: int, # 남은 칩 수
    my_cards: List[Card], # 플레이어의 손 패 (2장)
    bet_players: List[Other], # 이번 턴에 베팅한 플레이어들
    betting_players: List[Other], # 아직 베팅하지 않은 플레이어들
    community_cards: List[Card], # 커뮤니티 카드 + 턴 카드 + 리버 카드 (3장 ~ 5장)
    min_bet_amt: int, # 가능한 최소 베팅액
    max_bet_amt: int, # 가능한 최대 베팅액
    total_bet_amt: int # 여태까지 베팅한 누적 금액
) -> int:
    pass
```

#### Return

- 베팅할 칩의 수 (Int)
  - `0`을 `return` 하게 되면 해당 턴은 포기(`die`)한다는 의미입니다.
  - 반드시 `min_bet_amt`와 `max_bet_amt`를 고려하여 베팅할 칩 수를 결정해주세요. (올바르지 않은 범위의 값을 반환할 경우, 자동으로 해당 라운드에서 제외됩니다.)
  - 가지고 있는 모든 칩을 베팅할 경우 올인 형태로 진행됩니다.
- 함수 실행 중 에러가 발생할 경우, 해당 라운드에서 제외됩니다.
- 함수 실행 시간이 1초 이상 걸릴 경우, 해당 라운드에서 제외됩니다. 

#### Example

```python
def always_bet(
    my_chips: int,
    my_cards: List[Card],
    bet_players: List[Other],
    betting_players: List[Other],
    community_cards: List[Card],
    min_bet_amt: int,
    max_bet_amt: int,
    total_bet_amt: int
) -> int:
    if my_chips >= min_bet_amt:
        return min(max_bet_amt, min_bet_amt)
    else:
        return 0

```

[example.py](holdem/example.py)의 `always_bet(...)` 의 경우, 현재 게임 상황을 고려하지 않고 반드시 베팅을 하도록 구현되어 있습니다. 


### Run

> 뱅크샐러드 홀덤은 Python3.7 이상의 버전과 UNIX 환경만 지원합니다. 해당 환경에서 진행이 어려우신 분은 Docker를 이용하여 진행 부탁드립니다.

작성하신 코드를 테스트해보기 위해, 직접 프로그램을 실행해볼 수 있습니다. [\_\_main\_\_.py](holdem/__main__.py)의 하단 실행부 코드를 변경하여, 다양한 환경에서 실험해보실 수 있습니다.

```bash
python3 -m holdem
```

UNIX 이외의 환경에서는 올바르게 동작하지 않습니다. UNIX 이외의 환경에서는 **Docker**를 활용하여 코드를 실행해보실 수 있습니다.

```bash
docker-compose run holdem
```

> 게임이 실행 후 생성된 `play.log` 파일을 [뱅크샐러드 카지노](https://pycon2018.banksalad.com)에 업로드하시면 게임이 진행된 과정을 눈으로 확인하실 수 있습니다!


## Submission

- **2018년 8월 19일 일요일 오후 4시까지** 제출된 코드에 대해서만 참여자격이 부여됩니다.
- 작성하신 코드([turn.py](holdem/turn.py))를 [GitHub Gist](https://gist.github.com/)에 업로드 하신 후, 업로드된 Gist 링크를 [여기](https://goo.gl/forms/v4Nup2q7kgBlmmUh1)를 통해 제출해주세요.

## Prize

<p align="center">
  <img src="./resources/ipad-pro.png" alt="ipad" width="256px" />
</p>
<h3 align="center">1등 / iPad Pro 10.5"</h3>

<p align="center">
  <img src="./resources/airpods.png" alt="ipad" width="154px" />
</p>
<p align="center">2등 / AirPods</p>

<p align="center">3등 / Starbucks 상품권</p>

### Tournament

1. 제출하신 분들을 랜덤하게 5인 조로 나눠서, 토너먼트 방식으로 진행하여 결승 진출자 다섯 분을 선발합니다. 
1. 최종 우승자를 가리는 결승전과 시상식은 __8월 19일 오후 4시 30분에 뱅크샐러드 OST 룸(202)에서 진행됩니다.__ 
1. 시상식에 참여하지 못하신 분께는 죄송하지만 상품 제공이 어렵습니다. 상품 수령을 위해 __반드시 시상식에 참여 부탁드립니다.__


-----

## Rule

### 게임의 진행

> 게임의 진행은 일반적인 [텍사스 홀덤](https://en.wikipedia.org/wiki/Texas_hold_%27em)과 비슷합니다.
>
> 뱅크샐러드 홀덤에서는 라운드마다 무작위로 선정된 플레이어부터 게임을 시작하게 됩니다.

1. 게임에 참여한 플레이어는 참가비로 1개의 칩을 냅니다.
1. 2장의 카드를 받고 베팅을 합니다.
1. 3장의 플랍 카드가 오픈되고 베팅을 합니다.
1. 1장의 턴 카드가 오픈되고 베팅을 합니다.
1. 1장의 리버 카드가 오픈되고 베팅을 합니다.
1. 남은 플레이어가 공통으로 오픈된 5장의 커뮤니티 카드와 2장의 핸드를 비교하여 순위를 매긴 후 베팅된 칩을 가져갑니다.

베팅(2-5번 과정) 중 플레이어의 베팅 상태에 따라

1. 모든 플레이어가 죽을<sub>die</sub> 경우에는 베팅된 칩이 모두 사라집니다. 
1. 한 명의 플레이어만 남을 경우 해당 플레이어가 베팅된 칩을 모두 가져갑니다.

### 코드 작성 규칙

1. 파이썬 특유의 해킹을 이용한 플레이는 게임의 재밌는 진행을 위해 금지합니다. 제출하신 코드를 살펴본 후 문제가 있을 경우 말씀드리겠습니다.
1. 기존에 작성된 코드([madehands.py](holdem/core/madehands.py) 등)는 필요하실 경우 얼마든지 사용하셔도 괜찮습니다. 단 `import` 구문 작성이 올바르게 되었는지 확인 부탁드립니다.
1. 사용을 원하시는 라이브러리(ex.[Keras](https://keras.io/))가 있으시다면 [Issue](https://github.com/Rainist/pycon-2018-banksalad-holdem/issues)로 의견 남겨주시거나, 파이콘 뱅크샐러드 부스에 들러주세요 :)

### 용어

- 콜<sub>call</sub>: 앞 순서의 플레이어가 판돈을 올린 것을 받아들인다는 의미입니다.
- 레이즈<sub>raise</sub>: 앞 순서의 플레이어가 판돈을 올린 것을 받아들이되, 추가로 베팅을 하는 것을 의미합니다.
- 폴드<sub>fold</sub> : 해당 라운드를 포기합니다. 다이<sub>die</sub>라고도 합니다.
- 핸드<sub>hands</sub> : 플레이어의 손에 있는 2장의 카드
- 플랍<sub>flop</sub> : 처음으로 열리는 3장의 카드
- 턴 카드<sub>turn card</sub> : 2번째로 열리는 1장의 카드
- 리버 카드<sub>river card</sub> : 마지막으로 열리는 1장의 카드
- 커뮤니티 카드<sub>community cards</sub> : 바닥에 놓여 공통으로 사용되는 카드
- 쇼다운<sub>showdown</sub> : 리버 카드까지 열리고 남은 사람들끼리 패를 비교하는 과정
- 올인<sub>all-in</sub> : 현재 플레이어가 가진 모든 금액을 거는 행위

### 베팅 조건

- 게임이 시작되면 모든 플레이어는 200개의 칩을 가지고 시작합니다.
- 라운드마다 참여비 칩 한 개를 모든 플레이어에게 받습니다.
- 뱅크샐러드 홀덤에서는 자기 차례에 콜, 레이즈를 할 수 있으며 선으로 뽑힌 플레이어부터 판돈을 제시하고 다른 플레이어들에게 돌아가며 제시된 판돈에 대해 콜을 할지, 레이즈를 할지 정하게 됩니다.
  - 콜을 할 경우 다른 플레이어로 순서가 넘어갑니다.
  - 레이즈를 할 경우, 해당 플레이어를 기준으로 한 바퀴를 다시 돌게 됩니다.
- 라운드를 진행하는 중에 올인을 하게 되면 해당 플레이어를 기준으로 한 바퀴를 다시 돌고 모든 플레이어의 선택이 끝난 후에는 마지막 쇼다운까지 베팅 없이 진행됩니다.

### 뱅크샐러드 홀덤 족보

> 배점이 높은 순서대로 나열되어 있습니다.

#### 로열 플러시

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h10.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h11.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h12.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h13.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h1.png" width="15%"></img>

#### 스트레이트 플러시

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c3.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c4.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c5.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c6.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c7.png" width="15%"></img>

#### 포카드

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s9.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/d9.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h9.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c9.png" width="15%"></img>

#### 풀하우스

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h2.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s2.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h12.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c12.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/d12.png" width="15%"></img>

#### 플러시

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h2.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h5.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h6.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h8.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h11.png" width="15%"></img>

#### 스트레이트

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c7.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c8.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h9.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s10.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h11.png" width="15%"></img>

#### 트리플

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h3.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s3.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/d3.png" width="15%"></img><br>
<img src="https://cdn.banksalad.com/pycon2018/casino/cards/d13.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h13.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s13.png" width="15%"></img>

#### 투 페어

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s11.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h11.png" width="15%"></img>
<img src="https://cdn.banksalad.com/pycon2018/casino/cards/c5.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s5.png" width="15%"></img><br>
<img src="https://cdn.banksalad.com/pycon2018/casino/cards/s1.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c1.png" width="15%"></img>
<img src="https://cdn.banksalad.com/pycon2018/casino/cards/h8.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/d8.png" width="15%"></img>

#### 원 페어

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h10.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s10.png" width="15%"></img><br>
<img src="https://cdn.banksalad.com/pycon2018/casino/cards/c2.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/d2.png" width="15%"></img>

#### 하이 카드

<br><img src="https://cdn.banksalad.com/pycon2018/casino/cards/c1.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h4.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h7.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/s9.png" width="15%"></img><img src="https://cdn.banksalad.com/pycon2018/casino/cards/h11.png" width="15%"></img>

### 같은 족보일 경우의 판단

- 로열 플러시가 두벌 이상 나왔을 경우에는 _(거의 불가능한 확률)_ **스페이드 > 다이아몬드 > 하트 > 클로버** 순으로 높은 패로 인정됩니다.
- 로열 플러시가 아닌 경우에는 패가 만들어진 카드 중 가장 높은 숫자만을 비교합니다.
- 패가 같은 플레이어가 여러 명인 경우에는 만들어진 패의 숫자를 비교합니다.
- 만들어진 패의 숫자도 같은 경우에는 그 판은 동점이 되어 판돈은 플레이어 수로 나누어 가져갑니다.

## Any Questions?

[Issue](https://github.com/Rainist/pycon-2018-banksalad-holdem/issues)를 통해 질문을 남겨주시거나, 파이콘 뱅크샐러드 부스를 방문해주세요 😎
