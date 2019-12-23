import os

SPECIMEN_WIDTH_CM = 7.5  # 试样宽度，单位为厘米
SPECIMEN_HEIGHT_CM = 15  # 试样高度，单位为厘米

DOMAIN_EXTEND_CM = 4  # 模型箱在试样外扩张的宽度，单位为厘米
LOADING_PANEL_CM = 2  # 上下加载板向外扩充的大小，不能超过DOMAIN_EXTEND_CM

BALL_POROSITY = 0.05  # 试样的孔隙度
BALL_RADIUS_MIN_MM = 0.5  # 球的最小直径
BALL_RADIUS_MAX_MM = 0.8  # 球的最大直径

SAV_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sav')  # 存档保存路径
