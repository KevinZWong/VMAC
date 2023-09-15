from ScriptGenerationOOP import ScriptGenerator
from ScriptProcessingOOP import ScriptProcessing
from moviePyOOP import VideoGenerator
from HF_TTS import TextToSpeech
from ImageGnenerationOOP import ImageCreator
import openai
import time
import os
from moviepy.audio.io.AudioFileClip import AudioFileClip


script_gen = ScriptGenerator()
script_process = ScriptProcessing()
currentFolder = os.getcwd()
audioFilePath = currentFolder + "/VoiceFiles/"
imageFilePath = currentFolder + "/ImageFiles/"
videoFilePath = currentFolder + "/VideoFiles/"
scriptFilePath = currentFolder +"/scriptFiles/"
FinishedPath = currentFolder +"/FinishedVideos/"
data = []
'''
print("1. Generate One Video")
print("2. Mass Generation")
print("---------------------------")

userSelectNum = int(input("Please make a numerical selection: "))

if userSelectNum == 1:
    print("Single Video Generation Commencing ")
    topicsList = [input("Enter a Topic: ")] # This is in a list cause im lazy


    # Display to user
    for index,topic in enumerate(topicsList):
        print(index, ".", topic)
    print("---------------------------")
    #--------------------------------------
    for i in topicsList:
        print("Generating Script:", i)
        while True:
            try:
                rawScript = script_gen.generate_script(i)
                break  
            except openai.error.RateLimitError:
                time.sleep(10)
        data.append([i, rawScript])
        print("Raw Script: ", rawScript)
        print("============================================")
    
    print("\n\n\nRunning Manuel Selection...\n----------------------------------------------\n\n")
    data = script_gen.manualSelection(data)


elif userSelectNum == 2:
    print("Mass Video Generation Commencing ")
    topic = input("Enter a Topic: ")
    numTopics = int(input("Ender number of Videos: "))
    print("Generating ", numTopics, "Topics...")
    
    while True:
        try:
            topicsList = script_gen.generate_topics(topic, numTopics)
            break
        except openai.error.RateLimitError:
            time.sleep(10)
    print("Sucessfully Generated Topics")
    topicsList = topicsList.split(",")

    # Display to user
    for index,topic in enumerate(topicsList):
        print(index, ".", topic)
    print("---------------------------")
    #--------------------------------------
    for i in topicsList:
        print("Generating Script:", i)
        while True:
            try:
                rawScript = script_gen.generate_script(i)
                break  
            except openai.error.RateLimitError:
                time.sleep(10)
        data.append([i, rawScript])
        print("Raw Script: ", rawScript)
        print("============================================")
    
    print("\n\n\nRunning Manuel Selection...\n----------------------------------------------\n\n")
    data = script_gen.manualSelection(data)

    #data = [['Artificial intelligence in healthcare', "Yo, let's talk about artificial intelligence in healthcare, cuz that shit's mind-blowing! So, check this out. Did you know that AI can now help doctors diagnose illnesses better than some puny human brains? Yeah, fuckin' incredible, right? AI algorithms analyze tons of medical data to identify patterns and predict diseases with insane accuracy. It's like having a super smart 'puter that's seen a gazillion patients and knows all the fuckin' symptoms and shit. And here's the sickest part: it doesn't get tired or make dumbass mistakes like us mortals! This AI tech is like the ultimate sidekick for doctors, helping them not only diagnose but also personalize treatment plans for patients. It's revolutionizing the healthcare game, man. Can you fuckin' imagine a world where AI assists in preventing diseases before they even fuckin' happen? Well, it's slowly becoming a reality, my friend. With its ability to analyze massive amounts of data from patients, genetics, and even wearable devices, AI is helping healthcare professionals make better decisions and save lives. So, forget those old-school diagnoses, bro, 'cause AI is the new fuckin' boss in town!"]]

for i in range(0, len(data)):
    print("Producing ", data[i][1])
    print("Formatting Script")
    rawStory = data[i][1]
    Title = data[i][0]
    FinalTitle = script_process.titleFormater(data[i][0], 5)
    script = script_process.ScriptSpliterV2(data[i][1])
    for i in range(0, len(script), 1):
        script[i] = script_process.titleFormater(script[i], 6)
    script.insert(0, FinalTitle)
    audioScript = script_process.ScriptSpliterV2(rawStory)
    audioScript.insert(0, Title)
    print("Finished Formatting Script")
    
    audioFileNames = []
    # Voice files generation
    print("Starting Audio File Generation")
    print("Files to Generate: ", len(audioScript))
    TTSGenerate = TextToSpeech()
    for i, v in enumerate(audioScript):
        TTSGenerate.generate_speech(audioFilePath + "Audio" + str(i) + ".wav", v)
        print("Generated", "Audio" + str(i) + ".wav")
        audioFileNames.append(audioFilePath + "Audio" + str(i) + ".wav")

    VideoGenerator1 = VideoGenerator()
    VideoGenerator1.combine_audio_files(audioFileNames, audioFilePath + "Audio" + ".wav")
    print("Audio Files combined into one")
    print("Audio Generation Done")
    # Audio generation done
    i = data[0]
    #Image generation
    print("Beginning Image Generation")
    imageDescription = script_process.imageScriptGen(i)
    print("Images Scripts Parsed")
    print("Images to Generate: ", len(imageDescription))
    imageFiles = []
    image_creator = ImageCreator()
    for index ,segment in enumerate(imageDescription):
        description = script_gen.generate_image_description(segment)
        imagePath = image_creator.create_image(description)
        print("Image", index + 1, "Generated")
        imageFiles.append(imagePath)
    # image generation done
    print("Image Generation Done")
    print("Beginning Video Generation")
    VideoGenerator1 = VideoGenerator() 
    AudioFileLengthsList = []
    for i in audioFileNames:
        audioFileLength = VideoGenerator1.getLengthAudioFile(i)
        AudioFileLengthsList.append(audioFileLength)

    print("imageFiles =", imageFiles)
    print("AudioFileLengthsList =", AudioFileLengthsList)
    print("script =", script)

'''
Title = "cars"
VideoGenerator1 = VideoGenerator() 
imageFiles = ['/home/kevin/Desktop/PARSE/VMAC/ImageFiles/1694417835-0.png', '/home/kevin/Desktop/PARSE/VMAC/ImageFiles/1694417848-0.png', '/home/kevin/Desktop/PARSE/VMAC/ImageFiles/1694417862-0.png', '/home/kevin/Desktop/PARSE/VMAC/ImageFiles/1694417875-0.png', '/home/kevin/Desktop/PARSE/VMAC/ImageFiles/1694417887-0.png', '/home/kevin/Desktop/PARSE/VMAC/ImageFiles/1694417899-0.png', '/home/kevin/Desktop/PARSE/VMAC/ImageFiles/1694417914-0.png']
AudioFileLengthsList = [0.65, 3.41, 4.44, 4.41, 5.12, 1.71, 2.58, 4.87, 3.2, 4.1, 3.07, 9.62, 3.91, 5.0, 4.56]
script = ['cars ', 'Check this out, cars, right? So, \nwe all know about cars. ', 'They’re cool, they’re fast and they \nget us from point A to \npoint B, right? ', 'But did you know that the \nman who actually invented cruise control \nwas blind? ', 'No shit, his name was Ralph \nTeetor, and he was a mechanical \nengineer who lost ', 'his sight at the age of \nfive. ', 'But man, this guy was smart \nas hell, though. ', 'He invented cruise control in 1945 \nbecause his lawyer, who used to \ndrive him around, ', 'was so unpredictably fast and slow \non the road. ', "He'd speed up when he was \ntalking and slow down when he \nwas listening. ", "That shit gave him car sickness. \nCan y'all believe it? ", 'So Teetor got like "Fuck this \nmotion sickness.", pulled up his mechanical \ngenius pants and ', 'literally invented a solution. I mean \nhow badass is that? ', 'So the next time you’re cruising \ndown the freeway, give a little \nmental high five ', 'to Ralph, the blind inventor who \nmade our road trips a whole \nlot smoother. ']

totalVideolength = 0
for i in AudioFileLengthsList:
    totalVideolength += i
print("Video length:", totalVideolength)
VideoClip = VideoGenerator1.generateBackgroundFootageImages(imageFiles, totalVideolength )
print("Video Generated from Images")
VideoClip = VideoGenerator1.cropVideo(VideoClip)
print("Video Croped")
VideoClip = VideoGenerator1.overlay_audio_video(VideoClip,  "/home/kevin/Desktop/PARSE/VMAC/VoiceFiles/" + "Audio" + ".wav")
print("Audio Added to Video")
StartEndTImes = VideoGenerator1.ScriptSplitterV2_times(script , AudioFileLengthsList)
VideoClip = VideoGenerator1.add_text_overlay(VideoClip, StartEndTImes)
print("Text Overlay Added")
audio = AudioFileClip(audioFilePath + "Audio" + ".wav")
if VideoClip.duration > audio.duration:
    VideoClip = VideoClip.subclip(0, audio.duration)
VideoClip.write_videofile(FinishedPath + Title + ".mp4", fps=24)
VideoClip.close()
print(Title, "sucessfully generated")
