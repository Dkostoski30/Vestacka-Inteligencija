# from searching_framework import Problem, breadth_first_graph_search
#
#
# # state (zmija, red_apples, orientacija)
# def validate_state(snake, snake_head, red_apples):
#     if snake_head in snake or snake_head in red_apples:
#         return False
#     if snake_head[0] < 0 or snake_head[0] >= 10 or snake_head[1] < 0 or snake_head[1] >= 10:
#         return False
#     return True
#
#
# def ProdolziPravo(state, red_apples):
#     snake = list(state[0])
#     snake_head = snake[-1]
#     green_apples = list(state[1])
#     orientacija = state[2]
#
#     if orientacija == 'gore' and validate_state(snake, (snake_head[0], snake_head[1] + 1), red_apples):
#         snake.append((snake_head[0], snake_head[1] + 1))
#
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'dolu' and validate_state(snake, (snake_head[0], snake_head[1] - 1), red_apples):
#         snake.append((snake_head[0], snake_head[1] - 1))
#
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'desno' and validate_state(snake, (snake_head[0] + 1, snake_head[1]), red_apples):
#         snake.append((snake_head[0] + 1, snake_head[1]))
#
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'levo' and validate_state(snake, (snake_head[0] - 1, snake_head[1]), red_apples):
#         snake.append((snake_head[0] - 1, snake_head[1]))
#
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     snake = tuple(snake)
#     green_apples = tuple(green_apples)
#     return snake, green_apples, orientacija
#
#
# def SvrtiDesno(state, red_apples):
#     snake = list(state[0])
#     snake_head = snake[-1]
#     green_apples = list(state[1])
#     orientacija = state[2]
#
#     if orientacija == 'gore' and validate_state(snake, (snake_head[0] + 1, snake_head[1]), red_apples):
#         snake.append((snake_head[0] + 1, snake_head[1]))
#         orientacija = 'desno'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'dolu' and validate_state(snake, (snake_head[0] - 1, snake_head[1]), red_apples):
#         snake.append((snake_head[0] - 1, snake_head[1]))
#         orientacija = 'levo'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'desno' and validate_state(snake, (snake_head[0], snake_head[1] - 1), red_apples):
#         snake.append((snake_head[0], snake_head[1] - 1))
#         orientacija = 'dolu'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'levo' and validate_state(snake, (snake_head[0], snake_head[1] + 1), red_apples):
#         snake.append((snake_head[0], snake_head[1] + 1))
#         orientacija = 'gore'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     snake = tuple(snake)
#     green_apples = tuple(green_apples)
#     return snake, green_apples, orientacija
#
#
# def SvrtiLevo(state, red_apples):
#     snake = list(state[0])
#     snake_head = snake[-1]
#     green_apples = list(state[1])
#     orientacija = state[2]
#
#     if orientacija == 'gore' and validate_state(snake, (snake_head[0] - 1, snake_head[1]), red_apples):
#         snake.append((snake_head[0] - 1, snake_head[1]))
#         orientacija = 'levo'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'dolu' and validate_state(snake, (snake_head[0] + 1, snake_head[1]), red_apples):
#         snake.append((snake_head[0] + 1, snake_head[1]))
#         orientacija = 'desno'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'desno' and validate_state(snake, (snake_head[0], snake_head[1] + 1), red_apples):
#         snake.append((snake_head[0], snake_head[1] + 1))
#         orientacija = 'gore'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     elif orientacija == 'levo' and validate_state(snake, (snake_head[0], snake_head[1] - 1), red_apples):
#         snake.append((snake_head[0], snake_head[1] - 1))
#         orientacija = 'dolu'
#         snake_head = snake[-1]
#         if snake_head in green_apples:
#             green_apples = [apple for apple in green_apples if apple != snake_head]
#         else:
#             snake = snake[1:]
#
#         snake = tuple(snake)
#         green_apples = tuple(green_apples)
#
#     snake = tuple(snake)
#     green_apples = tuple(green_apples)
#     return snake, green_apples, orientacija
#
#
# class Snake_Game(Problem):
#     def __init__(self, initial, red_apples, goal=None):
#         super().__init__(initial, goal)
#         self.red_apples = red_apples
#
#     def successor(self, state):
#         possible_moves = dict()
#
#         new_state = ProdolziPravo(state, self.red_apples)
#         if state[0] != new_state[0]:
#             possible_moves["ProdolzhiPravo"] = new_state
#
#         new_state = SvrtiDesno(state, self.red_apples)
#         if state[0] != new_state[0]:
#             possible_moves["SvrtiDesno"] = new_state
#
#         new_state = SvrtiLevo(state, self.red_apples)
#         if state[0] != new_state[0]:
#             possible_moves["SvrtiLevo"] = new_state
#
#         return possible_moves
#
#
#     def actions(self, state):
#         return self.successor(state).keys()
#
#     def result(self, state, action):
#         return self.successor(state)[action]
#
#     def goal_test(self, state):
#         return len(state[1]) == 0
#
# if __name__ == '__main__':
#     n = int(input())
#     green = []
#
#     for i in range(0, n):
#         apple = input().split(',')
#         apple = [int(apple[0]), int(apple[1])]
#         green.append(tuple(apple))
#
#     m = int(input())
#     red = []
#
#     for i in range(0, m):
#         apple = input().split(',')
#         apple = [int(apple[0]), int(apple[1])]
#         red.append(tuple(apple))
#
#     s = ((0, 9), (0, 8), (0, 7))
#     orien = 'dolu'
#
#     snake_problem = Snake_Game((s, tuple(green), orien), tuple(red))
#     solution = breadth_first_graph_search(snake_problem)
#     if solution is not None:
#         print(solution.solution())
#     else:
#         print("[]")


import bisect

"""
Defining a class for the problem structure that we will solve with a search.
The Problem class is an abstract class from which we make inheritance to define the basic
characteristics of every problem we want to solve
"""


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """Given a state, return a dictionary of {action : state} pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once.

        :param state: given state
        :return:  dictionary of {action : state} pairs reachable
                  from this state
        :rtype: dict
        """
        raise NotImplementedError

    def actions(self, state):
        """Given a state, return a list of all actions possible
        from that state

        :param state: given state
        :return: list of actions
        :rtype: list
        """
        raise NotImplementedError

    def result(self, state, action):
        """Given a state and action, return the resulting state

        :param state: given state
        :param action: given action
        :return: resulting state
        """
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares
        the state to self.goal, as specified in the constructor. Implement
        this method if checking against a single self.goal is not enough.

        :param state: given state
        :return: is the given state a goal state
        :rtype: bool
        """
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from state1
        via action, assuming cost c to get up to state1. If the problem is such
        that the path doesn't matter, this function will only look at state2.
        If the path does matter, it will consider c and maybe state1 and action.
        The default method costs 1 for every step in the path.

        :param c: cost of the path to get up to state1
        :param state1: given current state
        :param action: action that needs to be done
        :param state2: state to arrive to
        :return: cost of the path after executing the action
        :rtype: float
        """
        return c + 1

    def value(self):
        """For optimization problems, each state has a value.
        Hill-climbing and related algorithms try to maximize this value.

        :return: state value
        :rtype: float
        """
        raise NotImplementedError


"""
Definition of the class for node structure of the search.
The class Node is not inherited
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create node from the search tree,  obtained from the parent by
        taking the action

        :param state: current state
        :param parent: parent state
        :param action: action
        :param path_cost: path cost
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node.

        :param problem: given problem
        :return: list of available nodes in one step
        :rtype: list(Node)
        """
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Return a child node from this node

        :param problem: given problem
        :param action: given action
        :return: available node  according to the given action
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Return the sequence of actions to go from the root to this node.

        :return: sequence of actions
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Return the sequence of states to go from the root to this node.

        :return: list of states
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node.

        :return: list of states from the path
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """We want the queue of nodes at breadth_first_search or
    astar_search to not contain states-duplicates, so the nodes that
    contain the same condition we treat as the same. [Problem: this can
    not be desirable in other situations.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Definitions of helper structures for storing the list of generated, but not checked nodes
"""


class Queue:
    """Queue is an abstract class/interface. There are three types:
        Stack(): Last In First Out Queue (stack).
        FIFOQueue(): First In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Adds the item into the queue

        :param item: given element
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Adds the items into the queue

        :param items: given elements
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Returns the first element of the queue

        :return: first element
        """
        raise NotImplementedError

    def __len__(self):
        """Returns the number of elements in the queue

        :return: number of elements in the queue
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Check if the queue contains the element item

        :param item: given element
        :return: whether the queue contains the item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """A queue in which the minimum (or maximum) element is returned first
     (as determined by f and order). This structure is used in
     informed search"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: sorting function, if order is min, returns the element
                      with minimal f (x); if the order is max, then returns the
                      element with maximum f (x).
        :param f: function f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


"""
Uninformed graph search
The main difference is that here we do not allow loops,
i.e. repetition of states
"""


def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
     If two paths reach a state, only use the best one.

    :param problem: given problem
    :param fringe: empty queue
    :return: Node
    """
    closed = {}
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed[node.state] = True
            fringe.extend(node.expand(problem))
    return None


def breadth_first_graph_search(problem):
    """Search the shallowest nodes in the search tree first.

    :param problem: given problem
    :return: Node
    """
    return graph_search(problem, FIFOQueue())


# state(snake, snake_dir, green apples)
def validate_state(state, obstacles):
    snake = state[0]
    snake_head = snake[-1]

    if snake_head in obstacles:
        return False
    if snake_head[0] < 0 or snake_head[0] >= 10 or snake_head[1] < 0 or snake_head[1] >= 10:
        return False
    if snake_head in snake[:-1]:
        return False

    return True


def move_south(state, obstacles):
    snake = list(state[0])
    snake_dir = state[1]
    green_apples = state[2]
    snake_head = snake[-1]
    new_snake_head = (snake_head[0], snake_head[1] - 1)
    snake.append(new_snake_head)
    if new_snake_head in green_apples:
        green_apples = list(green_apples)
        for green_apple in green_apples:
            if green_apple != new_snake_head:
                green_apples.remove(green_apple)
        green_apples = tuple(green_apples)
    else:
        snake = snake[1:]

    snake = tuple(snake)
    new_state = (snake, snake_dir, green_apples)
    if validate_state(new_state, obstacles):
        return new_state
    else:
        return state


def move_west(state, obstacles):
    snake = list(state[0])
    snake_dir = state[1]
    green_apples = state[2]
    snake_head = snake[-1]
    new_snake_head = (snake_head[0] - 1, snake_head[1])
    snake.append(new_snake_head)
    if new_snake_head in green_apples:
        green_apples = list(green_apples)
        for green_apple in green_apples:
            if green_apple != new_snake_head:
                green_apples.remove(green_apple)
        green_apples = tuple(green_apples)
    else:
        snake = snake[1:]

    snake = tuple(snake)
    new_state = (snake, snake_dir, green_apples)
    if validate_state(new_state, obstacles):
        return new_state
    else:
        return state


def move_east(state, obstacles):
    snake = list(state[0])
    snake_dir = state[1]
    green_apples = state[2]
    snake_head = snake[-1]
    new_snake_head = (snake_head[0] + 1, snake_head[1])
    snake.append(new_snake_head)
    if new_snake_head in green_apples:
        green_apples = list(green_apples)
        for green_apple in green_apples:
            if green_apple != new_snake_head:
                green_apples.remove(green_apple)
        green_apples = tuple(green_apples)
    else:
        snake = snake[1:]

    snake = tuple(snake)
    new_state = (snake, snake_dir, green_apples)
    if validate_state(new_state, obstacles):
        return new_state
    else:
        return state


def move_north(state, obstacles):
    snake = list(state[0])
    snake_dir = state[1]
    green_apples = state[2]
    snake_head = snake[-1]
    new_snake_head = (snake_head[0], snake_head[1] + 1)
    snake.append(new_snake_head)
    if new_snake_head in green_apples:
        green_apples = list(green_apples)
        for green_apple in green_apples:
            if green_apple != new_snake_head:
                green_apples.remove(green_apple)
        green_apples = tuple(green_apples)
    else:
        snake = snake[1:]

    snake = tuple(snake)
    new_state = (snake, snake_dir, green_apples)
    if validate_state(new_state, obstacles):
        return new_state
    else:
        return state


def SvrtiLevo(state, obstacles):
    snake_dir = state[1]
    if snake_dir == 'gore':
        new_state = move_west(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'levo', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'dolu':
        new_state = move_east(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'desno', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'levo':
        new_state = move_south(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'dolu', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'desno':
        new_state = move_north(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'gore', green_apples)
            return new_state
        else:
            return state


def SvrtiDesno(state, obstacles):
    snake_dir = state[1]
    if snake_dir == 'dolu':
        new_state = move_west(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'levo', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'gore':
        new_state = move_east(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'desno', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'desno':
        new_state = move_south(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'dolu', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'levo':
        new_state = move_north(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            new_state = (snake, 'gore', green_apples)
            return new_state
        else:
            return state


def ProdolziPravo(state, obstacles):
    snake_dir = state[1]
    if snake_dir == 'dolu':
        new_state = move_south(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            # new_state = (snake, 'levo', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'gore':
        new_state = move_north(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            # new_state = (snake, 'desno', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'desno':
        new_state = move_east(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            # new_state = (snake, 'dolu', green_apples)
            return new_state
        else:
            return state
    if snake_dir == 'levo':
        new_state = move_west(state, obstacles)
        if new_state != state:
            snake = new_state[0]
            green_apples = new_state[2]
            # new_state = (snake, 'gore', green_apples)
            return new_state
        else:
            return state


class SnakeGame(Problem):
    def __init__(self, initial, obstacles, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        possible_moves = dict()
        new_state = SvrtiLevo(state, self.obstacles)

        if new_state != state:
            possible_moves["SvrtiLevo"] = new_state

        new_state = SvrtiDesno(state, self.obstacles)
        if new_state != state:
            possible_moves["SvrtiDesno"] = new_state

        new_state = ProdolziPravo(state, self.obstacles)
        if new_state != state:
            possible_moves["ProdolzhiPravo"] = new_state

        print(possible_moves)
        return possible_moves

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_state(self, state):
        green_apples = state[2]
        return len(green_apples) == 0


if __name__ == '__main__':
    n = int(input())
    green = []

    for i in range(0, n):
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        green.append(tuple(apple))

    m = int(input())
    red = []

    for i in range(0, m):
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        red.append(tuple(apple))

    s = ((0, 9), (0, 8), (0, 7))
    orien = 'dolu'
    snake_problem = SnakeGame((s, orien, tuple(green)), tuple(red))
    solution = breadth_first_graph_search(snake_problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("[]")
