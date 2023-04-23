#!/usr/bin/env python
# coding=utf-8
'''
Author: JiangJi
Email: johnjim0816@gmail.com
Date: 2023-02-21 20:32:12
LastEditor: JiangJi
LastEditTime: 2023-04-16 23:44:39
Discription: 
'''
class DefaultConfig:
    def __init__(self) -> None:
        pass
    def print_cfg(self):
        print(self.__dict__)
        
class MergedConfig:
    def __init__(self) -> None:
        pass
class GeneralConfig():
    def __init__(self) -> None:
        self.env_name = "gym" # name of environment
        self.new_step_api = True # whether to use new step api of gym
        self.wrapper = 'envs.wrappers.CliffWalkingWapper2' # wrapper of environment
        self.render = True # whether to render environment
        self.render_mode = "human" # 渲染模式, "human" 或者 "rgb_array"
        self.algo_name = "DQN" # name of algorithm
        self.mode = "train" # train or test
        self.mp_backend = "mp" # 多线程框架，ray或者mp(multiprocessing)，默认mp
        self.seed = 0 # random seed
        self.device = "cuda" # device to use
        self.train_eps = 1000 # number of episodes for training
        self.test_eps = 200 # number of episodes for testing
        self.eval_eps = 10 # number of episodes for evaluation
        self.eval_per_episode = 5 # evaluation per episode
        self.max_steps = 200 # max steps for each episode
        self.load_checkpoint = False
        self.load_path = "Train_CartPole-v1_DQN_20230419-224210" # path to load model
        self.show_fig = False # show figure or not
        self.save_fig = True # save figure or not
