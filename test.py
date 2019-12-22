import itasca

itasca.command('model new')
import importlib

import make_sample
import settings

importlib.reload(make_sample)
importlib.reload(settings)

make_sample.make_sample()
