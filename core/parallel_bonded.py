# 本代码用于生成平行连接绑定
import itasca
from itasca import wall, ball, ballarray


def contact_model():
    itasca.command('contact model linearpbond range contact type "ball-ball"')
    itasca.command('contact method bond gap 0.5e-4')


def linear_stiffness():
    # 设置线刚度
    itasca.command('contact method deform emod 1.0e9 krat 1.0')
    # 设置连接的度
    itasca.command('contact method pb_deform emod 1.0e9 krat 1.0')
    # 设置连接的强度
    itasca.command('contact property pb_ten 10.0e6 pb_coh 50.0e6 pb_fa 0.0')
    # 设置能量耗散比
    itasca.command('contact property dp_nratio 0.5')
    # 设置球与球间的摩擦
    itasca.command('contact property fric 0.577 range contact type "ball-ball"')
    # 重置球的位移
    itasca.command('ball attribute displacement multiply 0.0')
    # 设置线性力为0，并使得连接的力为0
    itasca.command('contact property lin_force 0.0 0.0 lin_mode 1')
    ballarray.set_force_contact(ballarray.force_contact() * 0)
    itasca.command('model cycle 1')
    itasca.command('model solve ratio-average 1e-5')


def parallel_bonded():
    contact_model()
    linear_stiffness()
