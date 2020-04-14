import math

from gym_minigrid.minigrid import Goal, Grid, MiniGridEnv
from gym_minigrid.register import register


class RandomRewardLocEnv(MiniGridEnv):

    def __init__(self, size, agent_view_size=7):
        super().__init__(
            grid_size=size, max_steps=4 * size * size, see_through_walls=True, 
            agent_view_size=agent_view_size
        )

    def _gen_grid(self, width, height):
        # create empty grid
        self.grid = Grid(width, height)

        # generate surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # initialize agent position
        self.agent_pos = (width // 2, height // 2)
        self.agent_dir = 0

        # randomly place goal square
        self.place_obj(Goal(), top=None, size=None, max_tries=math.inf)

        # set textual mission
        self.mission = "get to the green goal square"

class EmptyRandomRewardLocEnv8x8(RandomRewardLocEnv):
    def __init__(self):
        super().__init__(size=8)

register(
    id='MiniGrid-Empty-Random-Reward-8x8-v0',
    entry_point='gym_minigrid.envs:EmptyRandomRewardLocEnv8x8'
)
