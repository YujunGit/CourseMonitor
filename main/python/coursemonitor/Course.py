#import json

class Course():
    """
    Course Class
    """
    def __init__(self, course:dict) -> None:
        """Constructor, create a course class from dict

        Args:
            course(dict): a dict contain all the information of a course
        """
        #Convert Json String to dict
        #course_dic = json.loads(course)
        
        self.id = course['id']
        self.term = course['term']
        self.enrollment = course['enrollment']
        self.seatsAvailable = course['seatsAvailable']
    
         
    def getSeatsAvailable(self) -> int:
        return self.seatsAvailable
    
    def isSeatAvailable(self) -> bool:
        return self.seatsAvailable > 0