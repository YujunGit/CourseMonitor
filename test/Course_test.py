import unittest

from main.python.coursemonitor.Course import Course

class CourseTest(unittest.TestCase):
    """This test case class contains basic unit tests for Course class.
    """
    CLASS1 = {'id': 358883, 'term': '202330', 'termDesc': 'Spring 2023 Semester', 'courseReferenceNumber': '33271', 'partOfTerm': '1', 'courseNumber': '4380', 'subject': 'FINA', 'subjectDescription': 'Finance &amp; Insurance', 'sequenceNumber': '01', 'campusDescription': 'Boston', 'scheduleTypeDescription': 'Lecture', 'courseTitle': 'Financial Data Analytics', 'creditHours': None, 'maximumEnrollment': 40, 'enrollment': 40, 'seatsAvailable': 0, 'waitCapacity': 0, 'waitCount': 0, 'waitAvailable': 0, 'crossList': None, 'crossListCapacity': None, 'crossListCount': None, 'crossListAvailable': None, 'creditHourHigh': None, 'creditHourLow': 4, 'creditHourIndicator': None, 'openSection': False, 'linkIdentifier': None, 'isSectionLinked': False, 'subjectCourse': 'FINA4380', 'faculty': [{'bannerId': '2782817', 'category': None, 'class': 'net.hedtech.banner.student.faculty.FacultyResultDecorator', 'courseReferenceNumber': '33271', 'displayName': 'Popescu, Marius', 'emailAddress': None, 'primaryIndicator': True, 'term': '202330'}], 'meetingsFaculty': [{'category': '01', 'class': 'net.hedtech.banner.student.schedule.SectionSessionDecorator', 'courseReferenceNumber': '33271', 'faculty': [], 'meetingTime': {'beginTime': '1030', 'building': 'BK', 'buildingDescription': 'Behrakis Health Sciences Cntr', 'campus': 'BOS', 'campusDescription': 'Boston', 'category': '01', 'class': 'net.hedtech.banner.general.overall.MeetingTimeDecorator', 'courseReferenceNumber': '33271', 'creditHourSession': 4.0, 'endDate': '04/19/2023', 'endTime': '1135', 'friday': False, 'hoursWeek': 3.25, 'meetingScheduleType': 'LEC', 'meetingType': 'CLAS', 'meetingTypeDescription': 'Class', 'monday': True, 'room': '105', 'saturday': False, 'startDate': '01/09/2023', 'sunday': False, 'term': '202330', 'thursday': True, 'tuesday': False, 'wednesday': True}, 'term': '202330'}], 'reservedSeatSummary': None, 'sectionAttributes': [{'class': 'net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator', 'code': 'UBBA', 'courseReferenceNumber': '33271', 'description': 'Business Admin', 'isZTCAttribute': False, 'termCode': '202330'}]}
    
    CLASS2 = {'id': 359294, 'term': '202330', 'termDesc': 'Spring 2023 Semester', 'courseReferenceNumber': '33682', 'partOfTerm': '1', 'courseNumber': '4380', 'subject': 'FINA', 'subjectDescription': 'Finance &amp; Insurance', 'sequenceNumber': '02', 'campusDescription': 'Boston', 'scheduleTypeDescription': 'Lecture', 'courseTitle': 'Financial Data Analytics', 'creditHours': None, 'maximumEnrollment': 40, 'enrollment': 38, 'seatsAvailable': 2, 'waitCapacity': 0, 'waitCount': 0, 'waitAvailable': 0, 'crossList': None, 'crossListCapacity': None, 'crossListCount': None, 'crossListAvailable': None, 'creditHourHigh': None, 'creditHourLow': 4, 'creditHourIndicator': None, 'openSection': False, 'linkIdentifier': None, 'isSectionLinked': False, 'subjectCourse': 'FINA4380', 'faculty': [{'bannerId': '2782817', 'category': None, 'class': 'net.hedtech.banner.student.faculty.FacultyResultDecorator', 'courseReferenceNumber': '33682', 'displayName': 'Popescu, Marius', 'emailAddress': None, 'primaryIndicator': True, 'term': '202330'}], 'meetingsFaculty': [{'category': '01', 'class': 'net.hedtech.banner.student.schedule.SectionSessionDecorator', 'courseReferenceNumber': '33682', 'faculty': [], 'meetingTime': {'beginTime': '0915', 'building': 'DG', 'buildingDescription': 'Dodge Hall', 'campus': 'BOS', 'campusDescription': 'Boston', 'category': '01', 'class': 'net.hedtech.banner.general.overall.MeetingTimeDecorator', 'courseReferenceNumber': '33682', 'creditHourSession': 4.0, 'endDate': '04/19/2023', 'endTime': '1020', 'friday': False, 'hoursWeek': 3.25, 'meetingScheduleType': 'LEC', 'meetingType': 'CLAS', 'meetingTypeDescription': 'Class', 'monday': True, 'room': '230', 'saturday': False, 'startDate': '01/09/2023', 'sunday': False, 'term': '202330', 'thursday': True, 'tuesday': False, 'wednesday': True}, 'term': '202330'}], 'reservedSeatSummary': None, 'sectionAttributes': [{'class': 'net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator', 'code': 'UBBA', 'courseReferenceNumber': '33682', 'description': 'Business Admin', 'isZTCAttribute': False, 'termCode': '202330'}]}
    
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_getSeatsAvailable(self):
        
        course = Course(self.CLASS1)
        seatsAvailable = course.getSeatsAvailable()

        self.assertEquals(seatsAvailable, 0)
    
    def test_isSeatAvailale(self):
        course1 = Course(self.CLASS1)
        course2 = Course(self.CLASS2)
        self.assertFalse(course1.isSeatAvailable())
        self.assertTrue(course2.isSeatAvailable())
        
        
    
if __name__ == "__main__":
	unittest.main()
    