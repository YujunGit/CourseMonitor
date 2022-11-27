import unittest

from main.python.coursemonitor.SearchResult import SearchResult
from main.python.coursemonitor.Course import Course

class SearchResult_test(unittest.TestCase):
    """This test case class contains basic unit tests for Course class.
    """
    RESULT_1 = '{\n  "success": true,\n  "totalCount": 0,\n  "data": null,\n  "pageOffset": 0,\n  "pageMaxSize": 20,\n  "sectionsFetchedCount": 0,\n  "pathMode": null,\n  "searchResultsConfigs": null,\n  "ztcEncodedImage": null\n}'
    
    RESULT_2 = '{\n  "success": true,\n  "totalCount": 2,\n  "data": \n  [\n    {\n      "id": 358883,\n      "term": "202330",\n      "termDesc": "Spring 2023 Semester",\n      "courseReferenceNumber": "33271",\n      "partOfTerm": "1",\n      "courseNumber": "4380",\n      "subject": "FINA",\n      "subjectDescription": "Finance &amp; Insurance",\n      "sequenceNumber": "01",\n      "campusDescription": "Boston",\n      "scheduleTypeDescription": "Lecture",\n      "courseTitle": "Financial Data Analytics",\n      "creditHours": null,\n      "maximumEnrollment": 40,\n      "enrollment": 40,\n      "seatsAvailable": 0,\n      "waitCapacity": 0,\n      "waitCount": 0,\n      "waitAvailable": 0,\n      "crossList": null,\n      "crossListCapacity": null,\n      "crossListCount": null,\n      "crossListAvailable": null,\n      "creditHourHigh": null,\n      "creditHourLow": 4,\n      "creditHourIndicator": null,\n      "openSection": false,\n      "linkIdentifier": null,\n      "isSectionLinked": false,\n      "subjectCourse": "FINA4380",\n      "faculty": \n      [\n        {\n          "bannerId": "2803501",\n          "category": null,\n          "class": "net.hedtech.banner.student.faculty.FacultyResultDecorator",\n          "courseReferenceNumber": "33271",\n          "displayName": "Popescu, Marius",\n          "emailAddress": null,\n          "primaryIndicator": true,\n          "term": "202330"\n        }\n      ],\n      "meetingsFaculty": \n      [\n        {\n          "category": "01",\n          "class": "net.hedtech.banner.student.schedule.SectionSessionDecorator",\n          "courseReferenceNumber": "33271",\n          "faculty": \n          [\n          ],\n          "meetingTime": {\n            "beginTime": "1030",\n            "building": "BK",\n            "buildingDescription": "Behrakis Health Sciences Cntr",\n            "campus": "BOS",\n            "campusDescription": "Boston",\n            "category": "01",\n            "class": "net.hedtech.banner.general.overall.MeetingTimeDecorator",\n            "courseReferenceNumber": "33271",\n            "creditHourSession": 4.0,\n            "endDate": "04/19/2023",\n            "endTime": "1135",\n            "friday": false,\n            "hoursWeek": 3.25,\n            "meetingScheduleType": "LEC",\n            "meetingType": "CLAS",\n            "meetingTypeDescription": "Class",\n            "monday": true,\n            "room": "105",\n            "saturday": false,\n           "startDate": "01/09/2023",\n            "sunday": false,\n            "term": "202330",\n            "thursday": true,\n            "tuesday": false,\n            "wednesday": true\n          },\n          "term": "202330"\n        }\n      ],\n      "reservedSeatSummary": null,\n      "sectionAttributes": \n      [\n        {\n          "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",\n          "code": "UBBA",\n          "courseReferenceNumber": "33271",\n          "description": "Business Admin",\n          "isZTCAttribute": false,\n          "termCode": "202330"\n        }\n      ]\n    },\n    {\n      "id": 359294,\n      "term": "202330",\n      "termDesc": "Spring 2023 Semester",\n      "courseReferenceNumber": "33682",\n      "partOfTerm": "1",\n      "courseNumber": "4380",\n      "subject": "FINA",\n      "subjectDescription": "Finance &amp; Insurance",\n      "sequenceNumber": "02",\n      "campusDescription": "Boston",\n      "scheduleTypeDescription": "Lecture",\n      "courseTitle": "Financial Data Analytics",\n      "creditHours": null,\n      "maximumEnrollment": 40,\n      "enrollment": 40,\n      "seatsAvailable": 0,\n      "waitCapacity": 0,\n      "waitCount": 0,\n      "waitAvailable": 0,\n      "crossList": null,\n      "crossListCapacity": null,\n      "crossListCount": null,\n      "crossListAvailable": null,\n      "creditHourHigh": null,\n      "creditHourLow": 4,\n      "creditHourIndicator": null,\n      "openSection": false,\n      "linkIdentifier": null,\n      "isSectionLinked": false,\n      "subjectCourse": "FINA4380",\n      "faculty": \n      [\n        {\n          "bannerId": "2803501",\n          "category": null,\n          "class": "net.hedtech.banner.student.faculty.FacultyResultDecorator",\n          "courseReferenceNumber": "33682",\n          "displayName": "Popescu, Marius",\n          "emailAddress": null,\n          "primaryIndicator": true,\n          "term": "202330"\n        }\n      ],\n      "meetingsFaculty": \n      [\n        {\n          "category": "01",\n          "class": "net.hedtech.banner.student.schedule.SectionSessionDecorator",\n          "courseReferenceNumber": "33682",\n          "faculty": \n          [\n          ],\n          "meetingTime": {\n            "beginTime": "0915",\n            "building": "DG",\n            "buildingDescription": "Dodge Hall",\n            "campus": "BOS",\n            "campusDescription": "Boston",\n            "category": "01",\n            "class": "net.hedtech.banner.general.overall.MeetingTimeDecorator",\n            "courseReferenceNumber": "33682",\n            "creditHourSession": 4.0,\n            "endDate": "04/19/2023",\n            "endTime": "1020",\n            "friday": false,\n            "hoursWeek": 3.25,\n            "meetingScheduleType": "LEC",\n            "meetingType": "CLAS",\n            "meetingTypeDescription": "Class",\n            "monday": true,\n            "room": "230",\n            "saturday": false,\n            "startDate": "01/09/2023",\n            "sunday": false,\n            "term": "202330",\n            "thursday": true,\n            "tuesday": false,\n            "wednesday": true\n          },\n          "term": "202330"\n        }\n      ],\n      "reservedSeatSummary": null,\n      "sectionAttributes": \n      [\n        {\n          "class": "net.hedtech.banner.student.schedule.SectionDegreeProgramAttributeDecorator",\n          "code": "UBBA",\n          "courseReferenceNumber": "33682",\n          "description": "Business Admin",\n          "isZTCAttribute": false,\n          "termCode": "202330"\n        }\n      ]\n    }\n  ],\n  "pageOffset": 0,\n  "pageMaxSize": 20,\n  "sectionsFetchedCount": 2,\n  "pathMode": "search",\n  "searchResultsConfigs": null,\n  "ztcEncodedImage": "data:image/png"\n}'
    
    
    
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_isSearchSuccess(self):
        
        result1 = SearchResult(self.RESULT_1)
        result2 = SearchResult(self.RESULT_2)
        self.assertTrue(result1.isSearchSuccess())
        self.assertTrue(result2.isSearchSuccess())
    
    def test_getTotalCount(self):
        result1 = SearchResult(self.RESULT_1)
        result2 = SearchResult(self.RESULT_2)
        self.assertEquals(result1.getTotalCount(), 0)
        self.assertEquals(result2.getTotalCount(), 2)
    
    def test_getCourseList(self):
        result2 = SearchResult(self.RESULT_2)
        self.assertEquals(result2.getTotalCount(), 2)
        
        courselist = result2.getCourseList()
        
        class1 = courselist[0]
        class2 = courselist[1]
        
        
    
if __name__ == "__main__":
	unittest.main()