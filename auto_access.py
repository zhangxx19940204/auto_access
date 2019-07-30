from wxpy import *
bot = Bot()

# 机器人账号自身
myself = bot.self

# 登录成功 --- 向文件传输助手发送消息
bot.file_helper.send('自动同意功能已准备就绪')



# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
	# 接收捕获的异常
	try:
		# 接受好友请求
		new_friend = msg.card.accept()
		# 向新的好友发送消息
		new_friend.send('欢迎啊，来我们聊聊')
	except:
		bot.file_helper.send('检查用户请求')
	
@bot.register()
def print_others(msg):
	print(msg)
	file_handle = open('data/%s.txt'%('data',), mode='a')
	file_handle.write('%s\n'%(msg,))
	file_handle.close()

	# 消息都会经过此方法,对用户进行回复
	full_str = msg.text
	check_str = "把你添加到通讯录"
	result = check_str in full_str
	if result :
		msg.reply_msg('欢迎啊，来我们聊聊')
	elif '可以开始聊天' in full_str:
		msg.reply_msg('欢迎啊，来我们聊聊2')
	else:
		# msg.reply_msg('你好呀')
		print(msg.receive_time)

embed()
