from locust import HttpUser, task, between

bundle_document = {
    "resourceType": "Bundle",
    "id": "bc1c02d6-4799-11ee-be56-0242ac120002",
    "identifier": {
        "system": "https://r7.myhealthbank.nhi.gov.tw",
        "value": "ABCD.BHMIHN.L152277270.r7.20230723.01"
    },
    "type": "document",
    "timestamp": "2023-07-23T06:00:03+08:00",
    "entry": [
        {
            "fullUrl": "urn:uuid:c6da3e7c-4799-11ee-be56-0242ac120002",
            "resource": {
                "resourceType": "Composition",
                "id": "c6da3e7c-4799-11ee-be56-0242ac120002",
                "identifier": {
                    "system": "https://r7.myhealthbank.nhi.gov.tw",
                    "value": "ABCD.BHMIHN.L152277270.r7.20230723.01"
                },
                "status": "final",
                "type": {
                    "coding": [
                        {
                            "system": "http://loinc.org",
                            "code": "30954-2",
                            "display": "Relevant diagnostic tests/laboratory data Narrative"
                        }
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "https://myhealthbank.nhi.gov.tw",
                                "code": "r7"
                            }
                        ]
                    }
                ],
                "subject": {
                    "reference": "urn:uuid:7736a208-10b6-4880-a344-b6745955d37c"
                },
                "date": "2023-07-23",
                "title": "健康存摺-檢驗（查）結果資料",
                "author": [
                    {
                        "reference": "urn:uuid:83c38cb2-817c-4c35-a013-977de42f41de",
                        "display": "PHI"
                    }
                ],
                "event": [
                    {
                        "period": {
                            "start": "2023-07-08T16:00:03+08:00"
                        }
                    }
                ],
                "section": [
                    {
                        "entry": [
                            {
                                "reference": "urn:uuid:83c38cb2-817c-4c35-a013-977de42f41de"
                            },
                            {
                                "reference": "urn:uuid:7736a208-10b6-4880-a344-b6745955d37c"
                            },
                            {
                                "reference": "urn:uuid:28181c98-4af8-11ee-be56-0242ac120002"
                            },
                            {
                                "reference": "urn:uuid:e92f1394-f49f-47dd-9761-75d2b02ee40a"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "fullUrl": "urn:uuid:83c38cb2-817c-4c35-a013-977de42f41de",
            "resource": {
                "resourceType": "Organization",
                "id": "83c38cb2-817c-4c35-a013-977de42f41de",
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "PRN"
                                }
                            ]
                        },
                        "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw",
                        "value": "1101020018"
                    }
                ],
                "address": [
                    {
                        "use": "work",
                        "text": "臺北市仁愛路十段123號"
                    }
                ],
                "telecom": [
                    {
                        "use": "work",
                        "system": "phone",
                        "value": "01-23456789"
                    }
                ],
                "active": "true",
                "name": "PHI",
                "alias": [
                    "PHI"
                ]
            }
        },
        {
            "fullUrl": "urn:uuid:7736a208-10b6-4880-a344-b6745955d37c",
            "resource": {
                "resourceType": "Patient",
                "id": "7736a208-10b6-4880-a344-b6745955d37c",
                "identifier": [
                    {
                        "use": "official",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "NNxxx"
                                }
                            ]
                        },
                        "system": "http://www.moi.gov.tw/",
                        "value": "L152277270"
                    },
                    {
                        "use": "official",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR"
                                }
                            ]
                        },
                        "system": "https://www.cgh.org.tw/",
                        "value": "Z0221X8S"
                    },
                    {
                        "value": "PATT.1101020018.L152277270"
                    }
                ],
                "active": "true",
                "name": [
                    {
                        "text": "波吉"
                    }
                ],
                "gender": "male",
                "birthDate": "2002-10-15",
                "deceasedBoolean": "false",
                "address": [
                    {
                        "use": "home",
                        "type": "physical",
                        "text": "123456臺北市松仁路700號"
                    }
                ],
                "managingOrganization": {
                    "reference": "urn:uuid:83c38cb2-817c-4c35-a013-977de42f41de"
                }
            }
        },
        {
            "fullUrl": "urn:uuid:28181c98-4af8-11ee-be56-0242ac120002",
            "resource": {
                "resourceType": "Person",
                "id": "28181c98-4af8-11ee-be56-0242ac120002",
                "identifier": [
                    {
                        "use": "official",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "NNxxx"
                                }
                            ]
                        },
                        "system": "http://www.moi.gov.tw/",
                        "value": "L152277270"
                    }
                ],
                "active": "true",
                "name": [
                    {
                        "text": "波吉"
                    }
                ],
                "gender": "male",
                "birthDate": "2002-10-15",
                "address": [
                    {
                        "use": "home",
                        "type": "physical",
                        "text": "123456臺北市松仁路700號"
                    }
                ],
                "link": [
                    {
                        "target": {
                            "reference": "urn:uuid:7736a208-10b6-4880-a344-b6745955d37c"
                        }
                    }
                ]
            }
        },
        {
            "fullUrl": "urn:uuid:e92f1394-f49f-47dd-9761-75d2b02ee40a",
            "resource": {
                "resourceType": "Observation",
                "status": "final",
                "id": "e92f1394-f49f-47dd-9761-75d2b02ee40a",
                "identifier": [
                    {
                        "system": "https://r7.myhealthbank.nhi.gov.tw",
                        "value": "ABCD.BHMIHN.L152277270.r7.20230723.01"
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "code": "09006C",
                            "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw",
                            "display": "醣化血紅素"
                        }
                    ],
                    "text": "醣化血紅素"
                },
                "effectivePeriod": {
                    "start": "2023-07-08T12:12:00+08:00",
                    "end": "2023-07-08T16:00:00+08:00"
                },
                "issued": "2022-07-09T17:30:00+08:00",
                "subject": {
                    "reference": "urn:uuid:7736a208-10b6-4880-a344-b6745955d37c"
                },
                "performer": [
                    {
                        "reference": "urn:uuid:83c38cb2-817c-4c35-a013-977de42f41de"
                    }
                ],
                "valueString": "4.5%",
                "referenceRange": [
                    {
                        "text": "4.0%–5.6%"
                    }
                ]
            }
        }
    ]
}

bundle_transaction = {
    "resourceType": "Bundle",
    "identifier": {
        "system": "https://r7.myhealthbank.nhi.gov.tw",
        "value": "ABCD.BHMIHN.L152277270.r7.20230723.01"
    },
    "type": "transaction",
    "timestamp": "2023-07-23T06:00:03+08:00",
    "entry": [
        {
            "fullUrl": "Organization/83c38cb2-817c-4c35-a013-977de42f41de",
            "resource": {
                "resourceType": "Organization",
                "id": "83c38cb2-817c-4c35-a013-977de42f41de",
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "PRN"
                                }
                            ]
                        },
                        "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/organization-identifier-tw",
                        "value": "1101020018"
                    }
                ],
                "address": [
                    {
                        "use": "work",
                        "text": "臺北市仁愛路十段123號"
                    }
                ],
                "telecom": [
                    {
                        "use": "work",
                        "system": "phone",
                        "value": "01-23456789"
                    }
                ],
                "active": "true",
                "name": "PHI",
                "alias": [
                    "PHI"
                ]
            },
            "request": {
                "url": "Organization/83c38cb2-817c-4c35-a013-977de42f41de",
                "method": "PUT"
            }
        },
        {
            "fullUrl": "Patient/7736a208-10b6-4880-a344-b6745955d37c",
            "resource": {
                "resourceType": "Patient",
                "id": "7736a208-10b6-4880-a344-b6745955d37c",
                "identifier": [
                    {
                        "use": "official",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "NNxxx"
                                }
                            ]
                        },
                        "system": "http://www.moi.gov.tw/",
                        "value": "L152277270"
                    },
                    {
                        "use": "official",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MR"
                                }
                            ]
                        },
                        "system": "https://www.cgh.org.tw/",
                        "value": "Z0221X8S"
                    },
                    {
                        "value": "PATT.1101020018.L152277270"
                    }
                ],
                "active": "true",
                "name": [
                    {
                        "text": "波吉"
                    }
                ],
                "gender": "male",
                "birthDate": "2002-10-15",
                "deceasedBoolean": "false",
                "address": [
                    {
                        "use": "home",
                        "type": "physical",
                        "text": "123456臺北市松仁路700號"
                    }
                ],
                "managingOrganization": {
                    "reference": "Organization/83c38cb2-817c-4c35-a013-977de42f41de"
                }
            },
            "request": {
                "url": "Patient/7736a208-10b6-4880-a344-b6745955d37c",
                "method": "PUT"
            }
        },
        {
            "fullUrl": "Person/28181c98-4af8-11ee-be56-0242ac120002",
            "resource": {
                "resourceType": "Person",
                "id": "28181c98-4af8-11ee-be56-0242ac120002",
                "identifier": [
                    {
                        "use": "official",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "NNxxx"
                                }
                            ]
                        },
                        "system": "http://www.moi.gov.tw/",
                        "value": "L152277270"
                    }
                ],
                "active": "true",
                "name": [
                    {
                        "text": "波吉"
                    }
                ],
                "gender": "male",
                "birthDate": "2002-10-15",
                "address": [
                    {
                        "use": "home",
                        "type": "physical",
                        "text": "123456臺北市松仁路700號"
                    }
                ],
                "link": [
                    {
                        "target": {
                            "reference": "Patient/7736a208-10b6-4880-a344-b6745955d37c"
                        }
                    }
                ]
            },
            "request": {
                "url": "Person/28181c98-4af8-11ee-be56-0242ac120002",
                "method": "PUT"
            }
        },
        {
            "fullUrl": "Observation/e92f1394-f49f-47dd-9761-75d2b02ee40a",
            "resource": {
                "resourceType": "Observation",
                "status": "final",
                "id": "e92f1394-f49f-47dd-9761-75d2b02ee40a",
                "identifier": [
                    {
                        "system": "https://r7.myhealthbank.nhi.gov.tw",
                        "value": "ABCD.BHMIHN.L152277270.r7.20230723.01"
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "code": "09006C",
                            "system": "https://twcore.mohw.gov.tw/ig/twcore/CodeSystem/medical-service-payment-tw",
                            "display": "醣化血紅素"
                        }
                    ],
                    "text": "醣化血紅素"
                },
                "effectivePeriod": {
                    "start": "2023-07-08T12:12:00+08:00",
                    "end": "2023-07-08T16:00:00+08:00"
                },
                "issued": "2022-07-09T17:30:00+08:00",
                "subject": {
                    "reference": "Patient/7736a208-10b6-4880-a344-b6745955d37c"
                },
                "performer": [
                    {
                        "reference": "Organization/83c38cb2-817c-4c35-a013-977de42f41de"
                    }
                ],
                "valueString": "4.5%",
                "referenceRange": [
                    {
                        "text": "4.0%–5.6%"
                    }
                ]
            },
            "request": {
                "url": "Observation/e92f1394-f49f-47dd-9761-75d2b02ee40a",
                "method": "PUT"
            }
        },
        {
            "fullUrl": "Composition/c6da3e7c-4799-11ee-be56-0242ac120002",
            "resource": {
                "resourceType": "Composition",
                "id": "c6da3e7c-4799-11ee-be56-0242ac120002",
                "identifier": {
                    "system": "https://r7.myhealthbank.nhi.gov.tw",
                    "value": "ABCD.BHMIHN.L152277270.r7.20230723.01"
                },
                "status": "final",
                "type": {
                    "coding": [
                        {
                            "system": "http://loinc.org",
                            "code": "30954-2",
                            "display": "Relevant diagnostic tests/laboratory data Narrative"
                        }
                    ]
                },
                "category": [
                    {
                        "coding": [
                            {
                                "system": "https://myhealthbank.nhi.gov.tw",
                                "code": "r7"
                            }
                        ]
                    }
                ],
                "subject": {
                    "reference": "Patient/7736a208-10b6-4880-a344-b6745955d37c"
                },
                "date": "2023-07-23",
                "title": "健康存摺-檢驗（查）結果資料",
                "author": [
                    {
                        "reference": "Organization/83c38cb2-817c-4c35-a013-977de42f41de",
                        "display": "PHI"
                    }
                ],
                "event": [
                    {
                        "period": {
                            "start": "2023-07-08T16:00:03+08:00"
                        }
                    }
                ],
                "section": [
                    {
                        "entry": [
                            {
                                "reference": "Organization/83c38cb2-817c-4c35-a013-977de42f41de"
                            },
                            {
                                "reference": "Patient/7736a208-10b6-4880-a344-b6745955d37c"
                            },
                            {
                                "reference": "Person/28181c98-4af8-11ee-be56-0242ac120002"
                            },
                            {
                                "reference": "Observation/e92f1394-f49f-47dd-9761-75d2b02ee40a"
                            }
                        ]
                    }
                ]
            },
            "request": {
                "url": "Composition/c6da3e7c-4799-11ee-be56-0242ac120002",
                "method": "PUT"
            }
        }
    ]
}


class BurniUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_patient(self):
        self.client.get("/Patient", name="Get Patient")

    @task
    def post_bundle_transaction(self):
        self.client.post("/Bundle", name="Post Bundle Transaction", json=bundle_transaction)
    
    @task
    def post_bundle_document(self):
        self.client.post("/Bundle", name="Post Bundle Document", json=bundle_document)
    
    @task
    def get_bundle_by_identifier(self):
        self.client.get(
            f"/Bundle?identifier={bundle_document['identifier']['value']}",
            name="Get Bundle by identifier"
        )
