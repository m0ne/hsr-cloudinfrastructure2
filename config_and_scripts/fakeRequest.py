from mitmproxy import ctx                                                                         
from mitmproxy import http                                                                        
flag=False                                                                                        
def request(flow: http.HTTPFlow):                                                                 
 ctx.log.info("Faking Destination Address")                                                
        flow.request.host = "10.0.0.10"                                                           
                                                                                                  
def response(flow: http.HTTPFlow):                                                                
        flow.response.status_code=200                                                             
        flow.response.content=bytes("You just have been intercepted","UTF-8")                     
        ctx.log.info("RESPONSE SENT")
