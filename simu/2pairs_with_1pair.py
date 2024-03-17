from Class import *
from tqdm import tqdm
import time


def main(discard: int, iterations: int):
    assert discard in range(1, 6)

    cnt_2pairs = 0
    for _ in tqdm(range(iterations)):
        deck = Deck()
        hand = Hand(upper_limit=8)
        # 先抽两张一样大的牌
        for i in range(2):
            hand.deal(deck)

        deck.shuffle()
        while len(hand) < 8:
            card = deck.deal()
            flag = True
            for i in range(len(hand)):
                if card.get_rank() == hand.get_card(i).get_rank():
                    deck.add_card_now(card)
                    deck.shuffle()
                    flag = False
                    break
            if flag:
                hand.add_card(card)

        # 弃五张摸五张
        for i in range(discard):
            hand.discard(hand.get_card(2), deck)

        # 一共有8张牌，其中有两对
        assert len(hand) == 8
        flag = False
        for i in range(2, 8):
            for j in range(i + 1, 8):
                if hand.get_card(i).get_rank() == hand.get_card(j).get_rank() and hand.get_card(i).get_rank() != 'Ace':
                    flag = True
                    break
            if flag:
                break
        cnt_2pairs += 1 if flag else 0

    print(f'原有1对弃{discard}张后出现两对的概率为{cnt_2pairs / iterations:.3%}')
    time.sleep(1)


if __name__ == '__main__':
    main(1, 1000000)
    main(2, 1000000)
    main(3, 1000000)
    main(4, 1000000)
    main(5, 1000000)
