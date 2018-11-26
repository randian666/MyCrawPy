#!/usr/bin/env python3
import json

class Recruit(object):

    def __init__(self):
        self.url=None
        self.suggestCity=None
        self.source=None
        self.created=None
        self.title=None
        self.salary=None
        self.job_url=None
        self.job_type=None
        self.place=None
        self.experience=None
        self.education=None
        self.company=None
        self.company_url=None
        self.company_type=None
        self.company_financing=None
        self.company_size=None
        self.publis_time=None
        self.keyword=None
        self.remark=None


if __name__ == '__main__':
    r=Recruit()
    r.url="100"
    print(r.url)
    print(r.__dict__)
