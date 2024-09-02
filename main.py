import pyscca
import zipfile
import os
import shutil

class ParsePrefetch :
    
    def __init__(self):
        self.output = {}

    def parse_prefetch(self,filename):
        #last_run_times = []
        last_run_times = dict()
        try :
           
            scca = pyscca.open(filename)
            self.output[str(scca.get_executable_filename())]={}
            self.output[str(scca.get_executable_filename())]["count"]= scca.run_count
            self.output[str(scca.get_executable_filename())]["mapped_files"]= scca.file_metrics_entries

            self.output[str(scca.get_executable_filename())]["hash"] = format(scca.prefetch_hash, 'x').upper()
            for x in range(9):
                
                if scca.get_last_run_time_as_integer(x) > 0:
                    
                    self.output[str(scca.get_executable_filename())]['date'+str(x)] = scca.get_last_run_time(x).strftime("%Y-%m-%d %H:%M:%S")

                else:
                     self.output[str(scca.get_executable_filename())]['date'+str(x)] = "N/A"

        except IOError:
            self.output["Error"] = "file doesn't exists"
        except NameError :
            self.output["Error"] = "file is not defined"


    def get_parse_prefetch(self,filename) :
       
        if zipfile.is_zipfile(filename):
            
            with zipfile.ZipFile(filename, 'r') as zip:
                # printing all the contents of the zip file
                
                # extracting all the files
                zip.extractall()
                # Get the filename  of all prefetch files
                # The first item is the name of folder
                list_prefetch = zip.namelist()

                # We apply all 
                for file in list_prefetch[1:] :
                    self.parse_prefetch(file)
            
                # After processing we can rm directory for next times
                shutil.rmtree(list_prefetch[0])
             
        else :
            # if not zip file then parsesingle file
            self.parse_prefetch(filename)

        return self.output


if __name__ == '__main__':
    
    pf_file = "../test/test.PF_DATA"
    pf_file1 = "../test/Prefetch.zip"
    parser = ParsePrefetch()
    res = parser.get_parse_prefetch(pf_file1)
    print(res)

