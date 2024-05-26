"""
Extracts information from a resume string using regular expressions. extractResumeInfo returns a dictionary containing the extracted information.

EXAMPLE USAGE:
patternExported = extractResumeInfo(contextResume)
# Save to JSON file
with open('/Users/Evelyn/Documents/Progayer/Projects/ProfileAI/basicExamples/verybasic/resume_info.json', 'w') as file:
    json.dump(patternExported, file, indent=4)
"""

import re
import json 

def getSingularPattern(pattern, resumeinfo): 
    try:
        pattern = re.compile(pattern)
        result = pattern.findall(resumeinfo)
        return result[0] if result else None
    except:
        return "ASDLFJAOWEHBASJEWNEWJEANS"
def extractResumeInfo(resumeinfo):
    print("THIS IS THE INPUT Resume Info: ", resumeinfo)

def extractResumeInfo(resumeinfo):
    resumeExtract = {
        "name": r"NAME: (.*)",
        "contact": r"CONTACT: (.*)",
        "website": r"WEBSITE: \[(.*)\]\((.*)\)",
        "description": r"DESCRIPTION: (.*)",
        "location": r"LOCATION: (.*)",
        # Education 
        "school": r"SCHOOL: (.*)",
        "year": r"YEAR: (.*)",
        "major": r"MAJOR\(S\): (.*)", 
        # Job Experiences
        "jobNames": [],
        "jobContent": [],
        # Other Experience and Interests
        "otherExperience": [],
        # Rating for Job
        "rating": r"## Rating for Job of (.*?)\n\n(.*?)(?=$|/10)"

    }
    print("Resume Info: ", resumeinfo)
    resumeExtract["name"] = getSingularPattern(resumeExtract["name"], resumeinfo)
    resumeExtract["contact"] = getSingularPattern(resumeExtract["contact"], resumeinfo)
    resumeExtract["website"] = getSingularPattern(resumeExtract["website"], resumeinfo)
    resumeExtract["description"] = getSingularPattern(resumeExtract["description"], resumeinfo)
    resumeExtract["location"] = getSingularPattern(resumeExtract["location"], resumeinfo)
    resumeExtract["school"] = getSingularPattern(resumeExtract["school"], resumeinfo)
    resumeExtract["year"] = getSingularPattern(resumeExtract["year"], resumeinfo)
    resumeExtract["major"] = getSingularPattern(resumeExtract["major"], resumeinfo)

    # Add job experiences 
    job_pattern = re.compile(r"### (.*?)(?=(###|$|---|Other Experience))", re.DOTALL) # gets the ### up till another ### or end of string or --- or Other Experience
    jobs = job_pattern.findall(resumeinfo) # jobs in tuples 
    job_data = [] 
    for job in jobs:    

        job_title, job_content = job[0].split('\n', 1)
        print("Job Title: ", job_title)
        print("Job Content: ", job_content)
        
        job_data.append({"jobName": job_title.strip(), "jobContent": job_content.strip()})
        # add to patterns
        resumeExtract["jobNames"].append(job_title)
        resumeExtract["jobContent"].append(job_content)
    
    # Add other experience
    other_pattern = re.compile(r"## Other Experience and Interests\n\n(.*?)(?=(---|Rating))", re.DOTALL) 
    other_experience = other_pattern.findall(resumeinfo)
    if other_experience: 
        for experience in other_experience[0]:
            resumeExtract["otherExperience"].append(experience)
            print("Other Experience: ", experience)

    # Add rating 
    rating_pattern = re.compile(r"## Rating for Job of (.*?)\n\n(.*?)(?=$)", re.DOTALL)
    rating = rating_pattern.findall(resumeinfo)
    rating_jobName, rating_content = rating[0]
    print("Rating Job Name: ", rating_jobName)
    print("Rating Content: ", rating_content)
    
    return resumeExtract
