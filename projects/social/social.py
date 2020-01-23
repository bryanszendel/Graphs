import random
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i)

        # Create friendships
        possible_friendships = []
        visited = []
        visited_inc = 0
        for user in self.users:
            for friend in self.users:
                if user < friend:
                    possible_friendships.append((user, friend))
            visited.append(user)
            visited_inc += 1

        random.shuffle(possible_friendships)
        # print(possible_friendships[:num_users*avg_friendships])
        for pair in possible_friendships[:num_users]:
            self.add_friendship(pair[0], pair[1])

    def get_neighbors(self, user_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.friendships[user_id]

    def dfs(self, starting_id, destination_id):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()

        # Put the starting point in that
        stack.push([starting_id])
        
        # Make a set to track where we've been
        visited = set()
        
        # While there is stuff in the queue/stack
        while stack.size() > 0:
        #   Pop the first item
            path = stack.pop()
            vertex = path[-1]
        #   If not visited:
            if vertex not in visited:
                if vertex == destination_id:
        #           DO THE THING!
                    return path
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
        #           Copy path to avoid pass by reference bug
                    new_path = list(path) # make a 'copy' rather than 'reference'
                    new_path.append(next_vert)
                    stack.push(new_path)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        user_friendships = self.friendships[user_id]
        print('user_friendships', user_friendships)
        for user in user_friendships:
            friends = self.dfs(user, user_id)
            new_friends = []
            for friend in friends:
                if friend != user:
                    new_friends.append(friend)
            visited[user] = new_friends
            # visited[user] = self.dfs(user, user_id)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships, "\n")
    connections = sg.get_all_social_paths(1)
    print(connections)
