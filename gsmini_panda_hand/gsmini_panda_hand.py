import copy
import pybullet as p
import numpy as np
import functools
from gym import spaces
import pybulletX as px  
from pybulletX.utils.space_dict import SpaceDict

class GSminiPandaHand(px.Robot): 
    MAX_FORCES = 100  
    gripper_joint_names = ["panda_finger_joint_left", "panda_finger_joint_right"]
    digit_joint_names = ["finger_gsmini_joint_right", "finger_gsmini_joint_left"]

    def __init__(self, robot_params):
        super().__init__(**robot_params)  # call parent's init
        self.reset()

    def get_states(self):
        gripper_joint = self.get_joint_states()[-1]
        states = self.state_space.new()
        states.gripper_width = 2 * np.abs(gripper_joint.joint_position)
        return states

    # Direct control
    def control_fingers(self, gripper_width):
        half_width = gripper_width / 2
        p.setJointMotorControl2(self.id, self.gripper_joint_ids[0], p.POSITION_CONTROL, targetPosition=half_width)
        p.setJointMotorControl2(self.id, self.gripper_joint_ids[1], p.POSITION_CONTROL, targetPosition=half_width)

    # Indirect Control From panel
    def set_actions(self, actions:dict): # actions from action_space
        gripper_width = actions.get("gripper_width", 0.0)
        max_forces = self.MAX_FORCES
        if actions.get("gripper_force"):
            max_forces[self.gripper_joint_ids] = actions["gripper_force"]
        # self.control_fingers(gripper_width)
        for joint_id in self.gripper_joint_ids:
            p.setJointMotorControl2(self.id, joint_id, p.POSITION_CONTROL, targetPosition=gripper_width / 2, force=max_forces)

    def grasp(self, width, grip_force=20):
        pass
        
    @property
    def gripper_joint_ids(self):
        return [self.get_joint_index_by_name(name) for name in self.gripper_joint_names]
    
    @property
    def gsmini_joint_ids(self):
        return [self.get_joint_index_by_name(name) for name in self.digit_joint_names]
      
    @property
    @functools.lru_cache(maxsize=None)
    def state_space(self):
        return SpaceDict(
            {
                "gripper_width": spaces.Box(low=0, high=0.08, shape=(1,), dtype=np.float32)
            }
        )
    @property
    @functools.lru_cache(maxsize=None)
    def action_space(self):
        action_space = copy.deepcopy(self.state_space)
        action_space["gripper_force"] = spaces.Box(
            low=0, high=self.MAX_FORCES, shape=(1,)
        )
        return action_space