# coding=utf-8

"""

"""
KEY_GAME_LOGIN = 5000  # 登录
KEY_GAME_REGISTER = 5001  # 注册
KEY_PUSH_OTHER_LOGIN = 5002  # 推送账号在别处登录
KEY_GET_ROOMS_PEOPLE = 5003  # 查看当前各房间人数

KEY_GAME_ENTER = 10000  # 进入游戏
KEY_GAME_CLASSIC_WX_EXIT = 10001  # 退出经典五星游戏
KEY_GAME_BET = 10002  # 游戏下注
KEY_GAME_GET_RECORD = 10003  # 获取游戏记录
KEY_GAME_EXIT = 10004  # 退出整个游戏
KEY_GAME_BET_BATCH = 10005  # 批量下注,用于续压,或代替单独押注
KEY_GAME_CANCEL_BET = 10006  # 取消押注

KEY_PUSH_GAME_START = 10100  # 推送游戏开始
KEY_PUSH_CURRENT_BET_INFO = 10101  # 推送所有玩家当前投注统计信息
KEY_PUSH_AWARD_RESULT = 10102  # 推送开奖结果

KEY_PUSH_SYSTEM_NOTICE = 100199   # 系统维护通知
