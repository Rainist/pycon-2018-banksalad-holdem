<h1 align="center">Pycon 2018 X Banksalad Holdem</h1>

<p align="center">
  <img src="./resources/banksalad-holdem.png" alt="banksalad-hold'em" width="384px" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-Rainist-blue.svg" alt="love" />
</p>

- 뱅크샐러드 홀덤
    + 뱅크샐러드 홀덤은 기존의 텍사스 홀덤에서 몇가지 규칙을 변경하여 구현되었습니다.
    + 5명의 플레이어가 하나의 게임에 참여하여 플레이 하게 되며, 2명의 플레이어가 남거나 100라운드가 끝났을 경우 한 경기가 끝나게 됩니다. (경기 종료 규칙 TBD)

## Rule
---
### 용어
 - 핸드(hands) : 플레이어의 손 패
 - 커뮤니티 카드(community cards) : 공통으로 열리는 맨 처음의 3장의 카드
 - 턴 카드(turn card) : 2번째로 열리는 1장의 카드
 - 리버 카드(river card) : 마지막으로 열리는 1장의 카드

### 게임의 진행
 - 게임의 진행은 일반적인 텍사스 홀덤과 비슷합니다.
 - 뱅샐 홀덤에서 선 및 딜러버튼은 없으며, 매 라운드마다 랜덤으로 선정된 플레이어부터 게임을 시작하게 됩니다. (TBD)
 - SB 및 BB도 존재하지 않습니다. (TBD)

 1. 게임에 참여한 플레이어는 2장의 카드를 받고 베팅을 합니다.
 2. 3장의 커뮤니티 카드가 오픈되고 베팅을 합니다.
 3. 1장의 턴 카드가 오픈되고 베팅을 합니다.
 4. 1장의 리버 카드가 오픈되고 베팅을 합니다.
 5. 남은 플레이어가 공통으로 오픈된 5장의 카드와 손패를 비교하여 순위를 매깁니다.

- 모든 사용자가 접을 경우 판돈은 사라집니다.

### 뱅샐홀덤 족보
    + 높은 순서대로 나열되어 있습니다.

>+ 로얄 스트레이트 플러시 (TBD)
>+ 백 스트레이트 플러시 (TBD)
>+ 스트레이트 플러시
>+ 포카드
>+ 풀하우스
>+ 플러시
>+ 마운틴 (TBD)
>+ 백 스트레이트 (TBD)
>+ 스트레이트
>+ 트리플
>+ 투 페어
>+ 원 페어
>+ 탑

### 같은 족보일 경우의 판단
- 스트레이트 이상의 족보에서는 일반적인 한국 룰인 스페이드 > 다이아 > 하트 > 클로버의 문양 순으로 높은 패로 인정됩니다.
- 트리플 이하에서는 패가 만들어진 카드 중 가장 높은 숫자를 비교합니다.

### 베팅 조건
- 참여비 (TBD)
- 최소 참여비 (TBD)

---

## How to play

`example.py` 의 `always_bet(...)` 함수를 참고하여 `turn.py` 의 `bet(...)` 함수를 수정하여 Pull Request 를 보내시면 됩니다.

```
def bet(
    my_chips: int,
    my_cards: List[Card],
    bet_players: List[Other],
    betting_players: List[Other],
    community_cards: List[Card],
    min_bet_amt: int,
    max_bet_amt: int,
    total_bet_amt: int
) -> int:
    pass
```

`0`을 `return` 하게 되면 해당 턴은 포기(`die`)한다는 의미입니다.

### Parameters:

- my_chips: 남은 칩 수
- my_cards: 플래이어의 손 패 (2장)
- bet_players: 이번 턴에 배팅한 플레이어들
- betting_players: 아직 배팅하지 않은 플레이어들
- community_cards: 커뮤니티 카드 + 턴 카드 + 리버 카드 (3장~5장)
- min_bet_amt: 가능한 최소 배팅액
- max_bet_amt: 가능한 최대 배팅액
- total_bet_amt: 여태까지 배팅한 누적 금액

### Test:
작성한 코드를 테스트 하려면, `__main__.py` 에서 `example.always_bet` 대신 `turn.py` 의 `bet` 함수를 `import` 하고 테스트 해보시면 됩니다

---
