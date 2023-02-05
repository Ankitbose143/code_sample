import logging

logging.basicConfig(filename="try.log")
leg = logging.getLogger()

leg.debug("its debug")
leg.info("its info")

asctime = 123
message = 'asank'
print(f'%{asctime} %(message)s')