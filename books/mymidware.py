import time 
import logging
import os

logger = logging.getLogger()
log_file = os.path.dirname(__file__) + "\log.txt"

hdlr = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)


class ViewEfficiencyMiddleware(object):   

    def process_view(self, request, view_func, view_args, view_kwargs):  
        self.start = time.clock()
        logger.info("%s" % "views call")

    # def process_request(self, request):
    #     self.start = time.clock()


    def process_response(self, request, response):
        self.end = time.clock()

        cost_time = self.end - self.start
        logger.info("%s:%s" % (str(request.path), str(cost_time)))

        return response
