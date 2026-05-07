# Bagram (21 Number Game)
A terminal-based Python game where you go head to head against a computer in a battle of counting strategy. The player who says 21 loses.

---

## How to Play
1. Run the game and choose whether to go **first or second**
2. On your turn, choose how many numbers to enter (1 to 3)
3. Numbers must be consecutive - no skipping
4. The player forced to say **21 loses**

---

## Features
- Play against a computer opponent that uses the **multiples-of-4 strategy**
- Choose to go first or second - going second gives you the chance to win
- Input validation for non-integers, out of range amounts, and wrong sequence numbers
- Computer is capped at 3 numbers per turn just like the player
- Forced to say 21 when the last number is 20

---

## How the Computer Thinks
The computer always tries to land on multiples of 4 - **4, 8, 12, 16, 20** - which mathematically forces the opponent to say 21. If you go second, you can use the same strategy against it by grabbing 2, 3, 4 on your first turn.

---

## Tech Stack
| Technology | Purpose |
|---|---|
| Python | Game logic and terminal interface |

---

## Getting Started

### Prerequisites
- Python 3 installed

### Installation
```bash
# Clone the repository
git clone https://github.com/kevvvvvz/bagram.git

# Navigate into the project
cd bagram

# Run the game
python numbers.py
```

---

## Winning Strategy
If you choose to go **second** (computer goes first):
- Computer opens with `[1]`
- Enter **3 numbers: 2, 3, 4** to land on 4
- From there, always enter enough numbers to land on the next multiple of 4
- The computer will be forced to say 21

---

## Future Improvements
- Multiplayer mode (two human players)
- Difficulty settings (easy computer plays randomly, hard uses the strategy)
- Score tracking across multiple rounds
