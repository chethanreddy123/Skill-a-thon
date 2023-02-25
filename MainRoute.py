import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

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
      max_tokens=1024,
      n=1,
      stop=None,
  )

  job_description = response.choices[0].text.strip()
  
  return {"Job_Description" : job_description}



@app.get("/getInformation")
def getInformation(info : Request):
  return FileResponse("obama.mp4")


