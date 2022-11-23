import json
from main.python.coursemonitor.Course import Course

class SearchResult():
    """
    Search Result Class
    """
    def __init__(self, response_text:str) -> None:
        """Constructor, c

        Args:
            response_text (str): response.text a json string
        """
        
        #Convert Json String to dict
        response_dic = json.loads(response_text)
        
        self.success = response_dic['success']
        self.totalCount = response_dic['totalCount']
        self.data = response_dic['data']
        
        #init courselist
        self.courselist = []
        self.initCourseList()
        
        
    def isSearchSuccess(self) -> bool:
        return self.success
    
    def getTotalCount(self) -> int:
        return self.totalCount
    
    def initCourseList(self):
        count = self.getTotalCount()
        for i in count:
            self.courselist[i] = Course(self.data[i])
            
    def getCourseList(self) -> list:
        return self.courselist