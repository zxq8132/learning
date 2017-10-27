#by zxq
user_data={
    'acc'
}
def run():
    '''
    程序启动时，函数启动时，立即调用，处理和用户交互的数据
    :return:
    '''
    acc_data=auth.acc_login(user_data,acc_logger)
    if user_data['is_authenticated']:
        user_dat['account_data']=acc_data
        interactive(user_data)
