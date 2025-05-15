class Linecounter:

    def __init__(self,file_name):
        self.file_name=file_name
        self.line = []
    def read(self):
        f =open(self.file_name,"r")
        self.line=f.readlines()
    def fetch_ip_add(self):
        self.ip_add=map(lambda x:x.split(" ")[0],self.line)
        self.ip_add=[*self.ip_add]
        return self.ip_add
    def ip_add_20(self):
        less_20=[*filter(lambda x :int(x.split(".")[0])<20,self.ip_add)]
        return self.less_20
    def ratio(self):
        return len(self.ip_add_20())/len(self.fetch_ip_add())