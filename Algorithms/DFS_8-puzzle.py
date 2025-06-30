class State:
    def __init__(self, board, goal, moves=0):
        self.board = board
        self.moves = moves
        self.goal = goal

    # i1과 i2를 교환하여서 새로운 상태를 반환한다.
    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, moves)

    def expand(self, moves):
        result = []
        i = self.board.index(0)  # 숫자 0(빈칸)의 위치를 찾는다.
        if not i in [0, 1, 2]:  # UP 연산자
            result.append(self.get_new_board(i, i - 3, moves))
        if not i in [0, 3, 6]:  # LEFT 연산자
            result.append(self.get_new_board(i, i - 1, moves))
        if not i in [2, 5, 8]:  # DOWN 연산자 -> 사실 RIGHT 연산자로 추정
            result.append(self.get_new_board(i, i + 1, moves))
        if not i in [6, 7, 8]:  # RIGHT 연산자 -> 사실 DOWN 연산자로 추정
            result.append(self.get_new_board(i, i + 3, moves))
        return result

    # 객체를 출력할 때 사용한다.
    def __str__(self):
        return str(self.board[:3]) + "\n" + \
            str(self.board[3:6]) + "\n" + \
            str(self.board[6:]) + "\n" + \
            "------------------"

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash((tuple(self.board)))


if __name__ == "__main__":
    puzzle=[2, 8, 3,
            1, 6, 4,
            7, 0, 5]

    goal = [1, 2, 3,
            8, 0, 4,
            7, 6, 5]

    # open 리스트
    not_visited = [State(puzzle, goal)]
    visited_set = set()
    moves = 0
    while not_visited:  # 스택이 빌 때까지
        current = not_visited.pop()  # 방문하려는 노드를 not_visited에서 삭제
        print(current, current.moves)
        if current.board == goal:
            print("탐색 성공")
            break

        if current not in visited_set:
            visited_set.add(current)
            moves = current.moves + 1

            for state in current.expand(moves):
                if state not in visited_set:  # 이미 거쳐간 노드가 아니면
                    not_visited.append(state)  # 리스트 추가
