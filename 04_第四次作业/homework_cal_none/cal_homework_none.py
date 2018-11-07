'''
任务：统计每一个同学的作业，
1、统计是否运行成功，如果成功，输出成功结果，如果失败，输出失败结果；
2、统计代码行数、字符数，备注行数，字符数；
'''
import os
import subprocess

###遍历同学的目录
def get_all_student_dir(path_dir):
    """
    返回每个同学的文件路径字典
    {name: file_path,...}
    """ 
    name = [x for x in os.listdir('homework')]
    return {x : os.path.join(path_dir, x) for x in name}

###将不同编码的文件转换为utf8文件
def convert_code():
    """
    实现了对文件原编码的判定，并重新编码为utf-8
    TODO 对文件原编码怎么判定啊
    """
    pass


###动态运行代码
def run_py(name, path, stdent_score):
    out = subprocess.Popen(["python", path], stdout=subprocess.PIPE)
    content = out.communicate()[0].decode('utf-8')
    content_len = len(content.split('\n'))
    stdent_score[name]['out_len'] = content_len
    if content == None:
        log_file = open('%s_%s.txt' % (name, 'err'), 'w')
        stdent_score[name]['flag'] = 0
    else:
        log_file = open('%s_%s.txt' % (name, 'log'), 'w')
        stdent_score[name]['flag'] = 1
    log_file.write(content)
    

##转换文件格式，返回代码字符串
def convert_file(path):
    """
    将文件读取出来，供后面统计
    """
    with open(path, 'r') as f:
        content = f.read()
    return content

##计算备注
def cul_beizhu(lines):
    """
    保存备注内容并记录行数
    : lines -> list of strings: 源文件的每一行
    : return
    : beizhu -> list of strings: 筛出来的每一行备注
    : beizhu_line -> int: 备注行数
    """
    beizhu = []
    for line in lines:
        if line.startswith('#') or line.startswith("'"):
            beizhu.append(line)
    beizhu_line = len(beizhu)
    return (beizhu, beizhu_line)

## 打印结果
def print_result(name_dict, stdent_score):
    """
    在终端打印结果
    """
    for name in name_dict.keys():
        print('%s代码检查结果:' % name)
        print('代码行数: %d, 代码字符数: %d, 注释行数: %d' % (stdent_score[name]['code_line'],stdent_score[name]['code_len'], stdent_score[name]['beizhu_line'])) 
        if stdent_score[name]['flag'] == 0:
            print('运行失败，输出行数: %d' % stdent_score[name]['out_len']) 
        else:
            print('运行成功，输出行数: %d' % stdent_score[name]['out_len']) 


###主程序
def get_homework_info(path_dir,homework):
    """
    改作业的主程序
    path_dir -> str: 收集同学们的作业文件夹的文件夹路径
    homework -> str: 本次处理的作业名

    stdent_score:
    {
    name1:{'code_len': pass, 'code_line': pass, 'beizhu': pass, 'beizhu_line': pass}, 'flag': pass, 'out_len': pass
    name2:{'code_len': pass, 'code_line': pass, 'beizhu': pass, 'beizhu_line': pass}, 'flag': pass, 'out_len': pass
    }
    """
    name_dict = get_all_student_dir(path_dir)
    stdent_score = {}
    for name in name_dict.keys():
        # 生成作业文件路径
        stdent_score[name] = {}
        path = os.path.join(name_dict[name], homework)
        #path = path.replace('/','\\') # 为什么这里还要replace？ os.path 应该会根据操作系统将path设置成对应的正确路径啊

        ##执行同学的代码，如果报错，输出到XXX_err.txt,如果成功，输出到XXX_log.txt
        run_py(name,path, stdent_score) # stdent_score 可以不用传入吧

        # 文件转换
        code=convert_file(path)

        # 统计代码长度和字符数
        stdent_score[name]['code_len'] = len(code)
        lines=code.split('\n') 
        stdent_score[name]['code_line'] = len(lines)

        # 统计备注的长度
        beizhu, beizhu_line = cul_beizhu(lines) # TODO beizhu是什么？在样例输出的结果图中只有备注的行数

        stdent_score[name]['beizhu'] = beizhu
        stdent_score[name]['beizhu_line'] = beizhu_line

    ##输出结果
    print_result(name_dict,stdent_score)
    
    return stdent_score

if __name__=="__main__":
    path='homework/'
    homework='debug.py'
    score_dict=get_homework_info(path,homework)
