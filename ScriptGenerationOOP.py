import openai
import os
from dotenv import load_dotenv
class ScriptGenerator:
    def __init__(self, engine="gpt-4"):
        load_dotenv(dotenv_path='/home/kevin/Desktop/PARSE/VMAC/.env')
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.engine = engine
        askCorrectDirectory = input("Confirm that your current directory is /VMAC/? y/n: ")
        if askCorrectDirectory == "y":
            if not(os.path.exists("ScriptFiles")):
                os.mkdir("ScriptFiles")
            if not(os.path.exists("VoiceFiles")):
                os.mkdir("VoiceFiles")
            if not(os.path.exists("ImageFiles")):
                os.mkdir("ImageFiles")
            if not(os.path.exists("VideoFiles")):
                os.mkdir("VideoFiles")
            if not(os.path.exists("FinishedVideos")):
                os.mkdir("FinishedVideos")
            if not(os.path.exists("jsonScriptFiles")):
                os.mkdir("jsonScriptFiles")
        else:
            print("Cahnge your file location stuppid")
            quit()

        
        pass
    def generate_topics(self, topic , amount ,max_tokens=4000, temperature=1):
        prompt = "write a list of " + str(amount) + "intresting topics related to" + topic + ". Respond with just the topics seperated by a comma, no numbers"

        completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        return  completion.choices[0].message.content
        
    def generate_script(self, topic ,max_tokens=4000, temperature=1):
        prompt = "I will give you a topic, your job is to write a long paragraph discussing one very specific interesting fact about the topic. The paragraph must be extremely casual. You have explicit orders to curse and must do so once. Your first topic is:"
        prompt += topic
        completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        return  completion.choices[0].message.content
        return response.choices[0].text.strip()
    def generate_image_description(self, segment ,max_tokens=4000, temperature=1):
        prompt = """
Your are now an ai program designed to turn simple sentences into descriptions of an art piece.
You will give responses that answer the following questions

How is the photo composed?
What is the emotional vibe of the image?
How much depth of field
How is the subject lit? Where from? How much light?
Artificial or natural light? What color? What time of day?
Where is this shot? In a studio or out in the world?

Example 1:
Given sentence:
“Steve jobs was a visionary”
Response:
A close-up, black & white studio photographic portrait of steve jobs, dramatic background

Example 2:
Given sentence:
“The sun is such a beautiful time to walk your dog”
Response:
“A vibrant photograph of a corgi dog, wide shot, outdoors, sunset photo at golden hour, wide-angle lens, soft focus”

You must follow the following orders
mimic these examples as closely as possible
Limit your responses to a maximum of 30 words
The art pieces you describe should be on earth 
The art pieces you describe must be a scenic view outdoors
They must be extremely lifelike and realistic
Your first sentence is:


        """
        #prompt += ". digital art"
        prompt += segment
        completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        return  completion.choices[0].message.content
        return response.choices[0].text.strip()


    def manualSelection(self, data):
        returnList = []
        for story in data:
            print(story[0])
            print(story[1])
            input1 = input("Y or N: ")
            if (input1.upper() == "Y"):
                returnList.append(story)
        return returnList
    
    
    def construct_upload_string(self, file_path, title, description, keywords, category, privacy_status):
        upload_string = 'python upload_video.py '

        upload_string += '--file="{}" '.format(file_path)
        upload_string += '--title="{}" '.format(title)
        upload_string += '--description="{}" '.format(description)
        upload_string += '--keywords="{}" '.format(keywords)
        upload_string += '--category="{}" '.format(category)
        upload_string += '--privacyStatus="{}"'.format(privacy_status)

        return upload_string

if __name__ == "__main__":
    # Usage
    script_gen = ScriptGenerator()
    topic = "Well, it's slowly becoming a reality, my friend. With its ability to analyze massive amounts of data from patients, genetics, and even wearable devices, AI is helping healthcare professionals make better decisions and save lives."
    script = script_gen.generate_image_description(topic)
    print(script)