import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import ast

load_dotenv()


openai.api_key = os.environ.get("OPENAI_API_KEY")


app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def askGPT(text):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 1000,
    )
    return response.choices[0].text

@app.post("/get_job/")
async def get_job(info : Request):

  print(await info.body())
  infoDict = await info.json()
  infoDict = dict(infoDict)

  Role = infoDict['Role']
  Organisation = infoDict['Organisation']
  Stipend = infoDict['Stipend']
  Qualification = infoDict['Qualification']
  Contact = infoDict['Contact']


  prompt = ( "You have been tasked with creating a job description for a new role at your organization. "
            "The following attributes have been provided: \n"
            f"1. Role: {Role} \n"
            f"2. Organization: {Organisation}  \n"
            f"3. Stipend : {Stipend} \n"
            f"4. Qualification : {Qualification} \n"
            f"5. Contact {Contact} \n\n"
            "Using Text-Davinci-003, write a job description that highlights the responsibilities and requirements of the role, as well as the benefits of working at the organization. "
            "Make sure to include the stipend, necessary qualifications, and contact information for interested applicants. "
            "Your job description should be clear, concise, and engaging, and should attract top talent to your organization.")

  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=2500,
      n=1,
      stop=None,
  )

  job_description = response.choices[0].text.strip()
  
  return {"Job_Description" : job_description}



@app.post("/get_course/")
async def get_course(info : Request):
  print(await info.body())
  infoDict = await info.json()
  infoDict = dict(infoDict)

  Course_Title = infoDict['Course_Title']
  Course_Duration = infoDict['Course_Duration']
  Instructor_Name = infoDict['Instructor_Name']
  Course_Structure = infoDict['Course_Structure']

  prompt = ( "Create a comprehensive course content that covers the following attributes:"
           "The following attributes have been provided: \n"
           f"1. Course_Title: {Course_Title} \n"
           f"2. Course Duration: {Course_Duration}  \n"
           f"3. Instructor_Name: {Instructor_Name} \n"
           f"4. Course_Structure  : {Course_Structure} \n\n"
           "Use the Davinci003 model to generate a complete and coherent course content that includes all of the above attributes. The content should be well-structured and easy to follow, catering to both beginners and experts in the field. Ensure that the content is informative, engaging, and covers all the necessary topics to give students a comprehensive understanding of the subject matter.")
  
  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=3000,
      n=1,
      stop=None,
  )

  Course_description = response.choices[0].text.strip()

  # TagPrompts = (
  #     "Can you generate only technical tags for content give below at max 5 tags in an array format"
  #     f"Course Content : {Course_description}"
  #     "Want the response in the below format"
  #     "Array = [List of all the tags]"
  # )

  # response = openai.Completion.create(
  #     engine="text-davinci-003",
  #     prompt=TagPrompts,
  #     temperature=0.5,
  #     max_tokens=100,
  #     n=1,
  #     stop=None,
  # )

  # Course_Tags = response.choices[0].text.strip()
  # TagList = ast.literal_eval(Course_Tags.split('=')[1][1:])

  return {"Course_description" : Course_description}  



@app.post("/get_Mentor/")
async def get_Mentor(info : Request):
  print(await info.body())
  infoDict = await info.json()
  infoDict = dict(infoDict)

  Mentor_Name = infoDict['Mentor_Name']
  Qualification = infoDict['Qualification']
  Organisation = infoDict['Organisation']
  Expertise = infoDict['Expertise']
  Contact = infoDict['Contact']

  prompt = (
      "Generate a description for a mentor using the following attributes:"
      f"Mentor Name : {Mentor_Name}"
      f"Qualification : {Qualification}"
      f"Organisation : {Organisation}"
      f"Expertise : {Expertise}"
      f"Contact : {Contact}"
      "Please use these attributes to create a detailed and informative description for the mentor. The description should highlight the mentor's achievements and experience, as well as their commitment to helping others. Please make sure that the language is professional and engaging, catering to both beginners and experts in the field"
  )


  response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=1024,
      n=1,
      stop=None,
  )

  Mentor_description = response.choices[0].text.strip()

  return {"Mentor_description" : Mentor_description }

@app.post("/get_chat/")
async def get_chat(info : Request):
  print(await info.body())
  infoDict = await info.json()
  infoDict = dict(infoDict)

  print(infoDict['Question'])

  return askGPT(infoDict['Question'])




@app.get("/getInformation")
def getInformation(info : Request):
  return FileResponse("obama.mp4")










