'''
任务：统计每一个同学的作业，
1、统计是否运行成功，如果成功，输出成功结果，如果失败，输出失败结果；
2、统计代码行数、字符数，备注行数，字符数；
'''
import os

###遍历同学的目录
# 为什么要返回一个字典？用列表感觉会更好
def get_all_student_dir(path_dir):
    return {x : 0 for x in os.listdir(path_dir)}

###将不同编码的文件转换为utf8文件
def 

###动态运行代码
def run_py(name, path, stdent_score):
    content = os.system('python %s' % py_file)
    if content == None:
        log_file = open('%s_%s.txt' % (name, 'err'), 'w')
    else:
        log_file = open('%s_%s.txt' % (name, 'log'), 'w')
    print(content, file=log_file)

##转换文件格式，返回代码字符串
def convert_file(path):

##计算备注
def cul_beizhu(path):
    py_script = open(path, 'r', )
    
    

###主程序
def get_homework_info(path_dir,homework):
    """
    改作业的主程序
    path_dir -> str: 收集同学们的作业文件夹的文件夹路径
    homework -> str: 本次处理的作业名

    stdent_score:
    {
    name1:{'code_len': pass, 'code_line': pass, 'beizhu': pass, 'code_line': pass},
    name2:{'code_len': pass, 'code_line': pass, 'beizhu': pass, 'code_line': pass},
    }
    """
    name_dict = get_all_student_dir(path_dir)
    stdent_score = {}
    for name in name_dict.keys():
        stdent_score[name] = {}
        path = os.path.join(name_dict[name], homework)
        path = path.replace('/','\\') # 为什么这里还要replace？ os.path 应该会根据操作系统将path设置成对应的正确路径啊
        ##执行同学的代码，如果报错，输出到XXX_err.txt,如果成功，输出到XXX_log.txt
        run_py(name,path,stdent_score) # stdent_score 可以不用传入吧, 传入更可度
        # 文件转换
        code=convert_file(path)
        # 统计代码长度和字符数
        stdent_score[name]['code_len'] = len(code)
        lines=code.split('\n') 
        stdent_score[name]['code_line'] = len(lines)
        # 统计备注的长度
        # beizhu, beizhu_line = cul_beizhu(lines) # TODO beizhu是什么？在样例输出的结果图中只有备注的行数
        beizhu_tiaoshu = cul_beizhu(path)

        stdent_score[name]['beizhu'] = beizhu
        stdent_score[name]['code_line'] = beizhu_line
    ##输出结果
    print_result(name_dict,stdent_score)
    
    return stdent_score

if __name__=="__main__":
    path='homework/'
    homework='debug.py'
    score_dict=get_homework_info(path,homework)
