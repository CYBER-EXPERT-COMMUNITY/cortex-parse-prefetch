#!/home/debian/myenv/prefetch/bin/python3.9

# encoding: utf-8

from cortexutils.analyzer import Analyzer
from main import ParsePrefetch as pf

class ORCParsePrefetch(Analyzer):

   

    def __init__(self):
        Analyzer.__init__(self)
        self.service = self.get_param('config.service', None, 'Service parameter is missing')

    
    #
    def summary(self, raw):
        taxonomies = []
        namespace = "ParseData"
        if self.service == 'ParsePrefetch':
            level = 'info'
            value = 'test'
            taxonomies.append(self.build_taxonomy(level, namespace, self.service, value))
        return {"taxonomies": taxonomies}

    def run(self):
        Analyzer.run(self)

        #
        if self.service == 'ParsePrefetch' and self.data_type == 'file':
            #
            try:
                path = self.get_param('file', None, 'File parameter is missing.'),
                filename = self.get_param('filename', None, 'Filename is missing.')
                
                # self.report({"Path":path,
                #              "Name":filename
                #             })
                
                try :
                    mypf = pf()
                    #self.report(mypf.get_parse_prefetch(filename=str(path[0])+'/'+filename))
                    self.report(mypf.get_parse_prefetch(filename=self.getParam("file")))
                    #self.report(mypf.get_parse_prefetch(filename="/Users/machakos/Desktop/test/test.PF_DATA"))
                    #
                   # path =  path+'/'
                    #filename = path+filename
                    #self.report({"Path":str(path[0])+'/'+filename})
                    #self.report({"Path":self.getParam("file")})
                    #self.report(mypf.get_parse_prefetch(filename=str(path[0])+'/'+filename))
                    #self.report({"Path":path+'/'+filename,"Prefetch2":"tata"})
                    #self.report({"Path":path+'/'+filename,"Prefetch2":"tata"})
                    # self.report({"7ZG.EXE":{"date":[{"date1":'2021-04-12 10:02:12',"date2":'2020-10-28 08:10:39'}]},
                    #  "MICROSOFTEDGE.EXE":{"date":[{"date1":'2021-04-12 10:02:12',"date2":'2020-10-28 08:10:39'}]}
                    #  })
                    #self.report({'7ZG.EXE': {'count': '4','prefetchhah':"rr",'date0':'2021-04-12 10:02:12'},'OPE.EXE': {'count': '4','prefetchhah':"rr",'date0':'2021-04-12 10:02:12'}})#, {'prefetchhah': 'F49B3D46'}, {'date0': '2021-04-12 10:02:12', 'date1': '2020-10-28 08:10:39', 'date2': '2020-10-07 12:25:32', 'date3': '2020-10-07 07:53:38', 'date4': 'N/A', 'date5': 'N/A', 'date6': 'N/A', 'date7': 'N/A'}}})
                #     self.report({
                # 'MICROSOFTEDGE.EXE': {
                #     'count': 10,
                #      'hash': 'F6B9D1D8',
                #       'date0': '2021-06-02 08:53:52',
                #        'date1': '2021-01-06 07:24:19',
                #         'date2': '2020-12-18 09:51:09',
                #          'date3': '2020-12-10 08:15:41',
                #           'date4': '2020-05-18 11:57:06',
                #            'date5': '2020-05-18 08:54:59',
                #             'date6': '2020-05-13 07:10:20',
                #              'date7': '2020-05-04 07:16:45'},
                    
                #      'DLLHOST.EXE': {
                #      'count': 1,
                #       'hash': 'F7FC6593',
                #        'date0': '2021-06-18 05:38:09',
                #         'date1': 'N/A', 
                #         'date2': 'N/A',
                #         'date3': 'N/A', 
                #          'date4': 'N/A',
                #           'date5': 'N/A',
                #            'date6': 'N/A',
                #             'date7': 'N/A'}
                            
                #             })
                 
                    #self.report()
                    
                    
                except  Exception as e:
                    self.unexpectedError(e)

            except Exception as e:
                self.unexpectedError(e)
        else:
            self.notSupported()

if __name__ == '__main__':
    ORCParsePrefetch().run()
